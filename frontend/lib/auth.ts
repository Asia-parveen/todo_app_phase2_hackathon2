/**
 * Authentication client for Better Auth integration
 * Handles registration, login, logout, and token management
 */

import { api, setAuthToken, clearAuthToken, getAuthToken } from "./api";
import {
  AuthResponse,
  RegisterResponse,
  User,
  UserCreate,
  UserLogin,
} from "./types";

/**
 * Register a new user
 */
export async function register(data: UserCreate): Promise<RegisterResponse> {
  const response = await api.post<RegisterResponse>(
    "/api/auth/register",
    data,
    false
  );
  return response;
}

/**
 * Login with email and password
 */
export async function login(data: UserLogin): Promise<AuthResponse> {
  const response = await api.post<AuthResponse>("/api/auth/login", data, false);

  // Store the token
  if (response.access_token) {
    setAuthToken(response.access_token);
  }

  return response;
}

/**
 * Logout the current user
 */
export async function logout(): Promise<void> {
  try {
    // Call logout endpoint if authenticated
    const token = getAuthToken();
    if (token) {
      await api.post("/api/auth/logout", {}, true);
    }
  } finally {
    // Always clear the token locally
    clearAuthToken();
  }
}

/**
 * Check if user is authenticated (has token)
 */
export function isAuthenticated(): boolean {
  return getAuthToken() !== null;
}

/**
 * Get the current user from the stored token
 * Note: This decodes the JWT client-side for display purposes
 * The backend validates the full token on each request
 */
export function getCurrentUser(): User | null {
  const token = getAuthToken();
  if (!token) return null;

  try {
    // Decode JWT payload (base64)
    const payload = token.split(".")[1];
    const decoded = JSON.parse(atob(payload));

    return {
      id: decoded.sub,
      email: decoded.email,
      created_at: decoded.created_at || new Date().toISOString(),
    };
  } catch {
    return null;
  }
}

/**
 * Auth client object for convenient access
 */
export const auth = {
  register,
  login,
  logout,
  isAuthenticated,
  getCurrentUser,
  getToken: getAuthToken,
  setToken: setAuthToken,
  clearToken: clearAuthToken,
};

export default auth;
