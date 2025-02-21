import { useEffect } from 'react'
import { useUser } from '../userContext'
import { ACCESS_TOKEN } from '../api/tokenStorage'
import { apiConfig } from '../api/api-utils'
import axios from 'axios'

const useUserData = () => {
  const { setUser } = useUser()

  useEffect(() => {
    const token = localStorage.getItem(ACCESS_TOKEN)

    if (token) {
      axios
        .get(`${apiConfig.backendUrl}/login/user`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then((res) => {
          if (res.status !== 200) {
            throw new Error('Network response was not ok')
          }
          return res.data
        })
        .then((data) => {
          if (data.user) {
            setUser(data.user) // Set user data in context
          } else {
            console.error('Failed to retrieve user data')
          }
        })
        .catch((err) => {
          console.error('Error fetching user data', err)
        })
    }
  }, [setUser])
}

export default useUserData
