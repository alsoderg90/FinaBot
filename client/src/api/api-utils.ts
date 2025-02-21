import { AxiosError } from 'axios'
import { ACCESS_TOKEN } from './tokenStorage'
import axios from 'axios'

export interface ErrorResponse {
  statusCode: number
  statusText: string
  message: string
}

export interface ServerError {
  error: string
}

export const apiConfig = {
  backendUrl: import.meta.env.VITE_BACKEND_API as string
}

export const googleClientId: string = import.meta.env
  .VITE_GOOGLE_OAUTH_CLIENT_ID as string

export const getAuthHeaders = () => {
  const token = localStorage.getItem(ACCESS_TOKEN)
  return {
    headers: {
      Authorization: `Bearer ${token}`
    }
  }
}

export const postRequest = async ({
  data,
  url
}: {
  data: Record<string, unknown>
  url: string
}): Promise<unknown> => {
  if (!apiConfig.backendUrl) {
    throw new Error('Backend URL is not defined')
  }
  const response = await axios.post(
    `${apiConfig.backendUrl}/${url}`,
    data,
    getAuthHeaders()
  )
  return response.data
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
