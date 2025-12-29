"use client";

interface LoadingProps {
  size?: "sm" | "md" | "lg";
  text?: string;
  fullScreen?: boolean;
}

const sizeStyles = {
  sm: "h-5 w-5",
  md: "h-10 w-10",
  lg: "h-14 w-14",
};

export default function Loading({
  size = "md",
  text,
  fullScreen = false,
}: LoadingProps) {
  const spinner = (
    <div className="flex flex-col items-center justify-center gap-4">
      <div className="relative">
        <div
          className={`${sizeStyles[size]} rounded-full border-4 border-purple-200 border-t-purple-600 animate-spin`}
        />
        <div
          className={`absolute inset-0 ${sizeStyles[size]} rounded-full border-4 border-transparent border-r-pink-500 animate-spin`}
          style={{ animationDirection: "reverse", animationDuration: "1.5s" }}
        />
      </div>
      {text && (
        <p className="text-sm font-medium bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
          {text}
        </p>
      )}
    </div>
  );

  if (fullScreen) {
    return (
      <div className="fixed inset-0 flex items-center justify-center bg-gradient-to-br from-indigo-50/90 via-purple-50/90 to-pink-50/90 backdrop-blur-sm z-50">
        {spinner}
      </div>
    );
  }

  return spinner;
}
