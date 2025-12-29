/**
 * Base API client with auth header injection and error handling
 */

import { ApiError } from "./types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

/**
 * Custom error class for API errors
 */
export class ApiRequestError extends Error {
  public status: number;
  public error: ApiError;

  constructor(status: number, error: ApiError) {
    super(error.message);
    this.name = "ApiRequestError";
    this.status = status;
    this.error = error;
  }
}

/**
 * Get the stored auth token
 */
export function getAuthToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("access_token");
}

/**
 * Set the auth token in storage
 */
export function setAuthToken(token: string): void {
  if (typeof window === "undefined") return;
  localStorage.setItem("access_token", token);
}

/**
 * Clear the auth token from storage
 */
export function clearAuthToken(): void {
  if (typeof window === "undefined") return;
  localStorage.removeItem("access_token");
}

/**
 * Build headers for API requests
 */
function buildHeaders(
  includeAuth: boolean = true,
  contentType: string = "application/json"
): HeadersInit {
  const headers: HeadersInit = {
    "Content-Type": contentType,
  };

  if (includeAuth) {
    const token = getAuthToken();
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
  }

  return headers;
}

/**
 * Parse API response and handle errors
 */
async function handleResponse<T>(response: Response): Promise<T> {
  const contentType = response.headers.get("content-type");
  const isJson = contentType?.includes("application/json");

  if (!response.ok) {
    let error: ApiError;

    if (isJson) {
      const body = await response.json();
      error = body.detail || body;
    } else {
      error = {
        error: "unknown_error",
        message: `Request failed with status ${response.status}`,
      };
    }

    throw new ApiRequestError(response.status, error);
  }

  if (isJson) {
    return response.json();
  }

  return {} as T;
}

/**
 * Make a GET request
 */
export async function get<T>(
  endpoint: string,
  includeAuth: boolean = true
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "GET",
    headers: buildHeaders(includeAuth),
  });

  return handleResponse<T>(response);
}

/**
 * Make a POST request
 */
export async function post<T, B = unknown>(
  endpoint: string,
  body: B,
  includeAuth: boolean = true
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "POST",
    headers: buildHeaders(includeAuth),
    body: JSON.stringify(body),
  });

  return handleResponse<T>(response);
}

/**
 * Make a PUT request
 */
export async function put<T, B = unknown>(
  endpoint: string,
  body: B,
  includeAuth: boolean = true
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "PUT",
    headers: buildHeaders(includeAuth),
    body: JSON.stringify(body),
  });

  return handleResponse<T>(response);
}

/**
 * Make a PATCH request
 */
export async function patch<T, B = unknown>(
  endpoint: string,
  body?: B,
  includeAuth: boolean = true
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "PATCH",
    headers: buildHeaders(includeAuth),
    body: body ? JSON.stringify(body) : undefined,
  });

  return handleResponse<T>(response);
}

/**
 * Make a DELETE request
 */
export async function del<T>(
  endpoint: string,
  includeAuth: boolean = true
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "DELETE",
    headers: buildHeaders(includeAuth),
  });

  return handleResponse<T>(response);
}

/**
 * API client object for convenient access
 */
export const api = {
  get,
  post,
  put,
  patch,
  delete: del,
};

export default api;
