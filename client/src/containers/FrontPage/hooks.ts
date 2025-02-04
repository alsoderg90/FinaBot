import axios from 'axios'
import { apiConfig } from '../../api/api-utils'
import { IMessage, PostDataInput } from './types'

export const postRequest = async (
  data: PostDataInput
): Promise<IMessage> => {
  if (!apiConfig.backendUrl) {
    throw new Error('Backend URL is not defined')
  }
  const response = await axios.post(`${apiConfig.backendUrl}/chat`, {
    data
  })

  return response.data
}
