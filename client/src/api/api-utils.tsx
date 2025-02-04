interface ApiConfig {
  backendUrl: string | undefined
}

export const apiConfig: ApiConfig = {
  backendUrl: import.meta.env.VITE_BACKEND_API
}
