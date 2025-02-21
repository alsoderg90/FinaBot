export const ACCESS_TOKEN = 'access_token'

export const tokenStorage = {
  setToken: (tokenType: string, token: string) => {
    localStorage.setItem(tokenType, token)
  },
  getToken: (tokenType: string) => {
    return localStorage.getItem(tokenType)
  },
  removeToken: (tokenType: string) => {
    localStorage.removeItem(tokenType)
  }
}
