import axios from 'axios'
import { apiConfig } from '../../api/api-utils'
import { CredentialResponse } from '@react-oauth/google'
import { LoginResponse } from './types'

export const postRequest = async (
  data: CredentialResponse
): Promise<LoginResponse> => {
  if (!apiConfig.backendUrl) {
    throw new Error('Backend URL is not defined')
  }

  const response = await axios.post(
    `${apiConfig.backendUrl}/login/callback`,
    {
      data
    }
  )

  return response.data
}
