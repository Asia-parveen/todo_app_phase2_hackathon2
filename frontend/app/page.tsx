"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { isAuthenticated } from "@/lib/auth";
import Loading from "@/components/ui/Loading";

export default function HomePage() {
  const router = useRouter();

  useEffect(() => {
    // Redirect based on auth state
    if (isAuthenticated()) {
      router.replace("/tasks");
    } else {
      router.replace("/login");
    }
  }, [router]);

  // Show loading while checking auth and redirecting
  return (
    <div className="min-h-screen flex items-center justify-center">
      <Loading size="lg" text="Loading..." />
    </div>
  );
}
