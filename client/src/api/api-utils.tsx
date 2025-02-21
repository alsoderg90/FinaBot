import { AxiosError } from 'axios'

interface ApiConfig {
  backendUrl: string | undefined
}

export interface ErrorResponse {
  statusCode: number
  statusText: string
  message: string
}

export interface ServerError {
  error: string
}

export const apiConfig: ApiConfig = {
  backendUrl: import.meta.env.VITE_BACKEND_API
}

export const handleError = (error: AxiosError): ErrorResponse => {
  if (error.response) {
    const responseData = error.response.data as ServerError
    return {
      statusCode: error.request.status || 500,
      statusText: error.request.statusText || 'Internal Server Error',
      message: responseData.error
    }
  }

  return {
    statusCode: 500,
    statusText: 'Internal Server Error',
    message: 'An error occurred while processing the request'
  }
}
