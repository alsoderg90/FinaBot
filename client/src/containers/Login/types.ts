import { User } from '../../types'

export interface LoginResponse {
  user: User
  access_token: string
}
