import type React from 'react'
import {
  Modal,
  Box,
  Typography,
  Button,
  ThemeProvider,
  createTheme
} from '@mui/material'
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline'

// Define the theme
const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#3f51b5',
      light: '#757de8'
    },
    secondary: {
      main: '#f50057'
    },
    background: {
      default: 'white',
      paper: '#f5f5f5'
    }
  }
})

interface ErrorModalProps {
  open: boolean
  onClose: () => void
  title: string
  message: string
  statusCode: number
}

const ErrorModal: React.FC<ErrorModalProps> = ({
  open,
  onClose,
  title,
  statusCode,
  message
}) => {
  return (
    <ThemeProvider theme={theme}>
      <Modal
        open={open}
        onClose={onClose}
        aria-labelledby='error-modal-title'
        aria-describedby='error-modal-description'
      >
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 400,
            bgcolor: 'background.paper',
            boxShadow: 24,
            p: 4,
            borderRadius: 2,
            textAlign: 'center'
          }}
        >
          <ErrorOutlineIcon
            sx={{ fontSize: 60, color: 'secondary.main', mb: 2 }}
          />
          <Typography
            id='error-modal-title'
            variant='h5'
            component='h2'
            gutterBottom
          >
            {`${statusCode} : ${title}`}
          </Typography>
          <Typography
            id='error-modal-description'
            sx={{ mt: 2, mb: 3 }}
          >
            {message}
          </Typography>
          <Button
            variant='contained'
            onClick={onClose}
            sx={{
              bgcolor: 'primary.main',
              '&:hover': {
                bgcolor: 'primary.light'
              }
            }}
          >
            Close
          </Button>
        </Box>
      </Modal>
    </ThemeProvider>
  )
}

export default ErrorModal
