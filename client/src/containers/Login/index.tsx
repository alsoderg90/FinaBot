import { useState } from 'react'
import {
  Button,
  Card,
  CardContent,
  CardActions,
  Avatar,
  Typography,
  Box,
  createTheme
} from '@mui/material'
import {
  Logout as LogoutIcon,
  Settings as SettingsIcon,
  Email as EmailIcon
} from '@mui/icons-material'
import { LoginResponse } from './types'
import { CredentialResponse, GoogleLogin } from '@react-oauth/google'
import { useMutation } from '@tanstack/react-query'
import { postRequest } from './requests'
import { AxiosError } from 'axios'
import { ErrorResponse, handleError } from '../../api/api-utils'
import ErrorModal from '../../components/ErrorComponent'
import { ACCESS_TOKEN, tokenStorage } from '../../api/tokenStorage'
import { useUser } from '../../userContext'

export const Login = () => {
  const [error, setError] = useState<ErrorResponse | null>(null)

  const { setUser, user } = useUser()

  const login = useMutation({
    mutationFn: postRequest,
    onSuccess: (response: LoginResponse) => {
      setUser(response.user)
      tokenStorage.setToken(ACCESS_TOKEN, response.access_token)
    },
    onError: (error: unknown) => {
      if (error instanceof AxiosError) {
        const errorResponse = handleError(error)
        setError(errorResponse)
      }
    }
  })

  if (error) {
    return (
      <ErrorModal
        onClose={() => setError(null)}
        open={true}
        statusCode={error.statusCode}
        title={error.statusText}
        message={error.message}
      />
    )
  }

  const theme = createTheme({
    // You can customize your theme here
    palette: {
      mode: 'light' // or 'dark'
    }
  })

  return (
    <>
      {user ? (
        <Card sx={{ maxWidth: 345, width: '100%' }}>
          <CardContent
            sx={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center'
            }}
          >
            <Avatar
              src={user.picture}
              alt={user.name}
              sx={{
                width: 100,
                height: 100,
                mb: 2,
                border: `4px solid ${theme.palette.primary.main}`
              }}
            />
            <Typography variant='h5' component='div' gutterBottom>
              {user.name}
            </Typography>
            <Box display='flex' alignItems='center' mb={2}>
              <EmailIcon fontSize='small' sx={{ mr: 1 }} />
              <Typography variant='body2' color='text.secondary'>
                {user.email}
              </Typography>
            </Box>
            <Typography
              variant='body2'
              color='text.secondary'
              textAlign='center'
            >
              Welcome back! You're now signed in.
            </Typography>
          </CardContent>
          <CardActions
            sx={{ justifyContent: 'space-between', px: 2, pb: 2 }}
          >
            <Button
              variant='outlined'
              startIcon={<SettingsIcon />}
              //component={Link}
              //href='/settings'
            >
              Settings
            </Button>
            <Button
              variant='contained'
              color='error'
              startIcon={<LogoutIcon />}
            >
              Sign Out
            </Button>
          </CardActions>
        </Card>
      ) : (
        <GoogleLogin
          onSuccess={(credentialResponse: CredentialResponse) => {
            login.mutate(credentialResponse)
          }}
          theme='filled_blue'
          onError={() => {
            setError({
              statusCode: 500,
              statusText: 'Internal Server Error',
              message: 'Login failed'
            })
          }}
        />
      )}
    </>
  )
}
