import './App.css'
import {
  QueryClient,
  QueryClientProvider
} from '@tanstack/react-query'
import { Container } from '@mui/material'
import {
  ThemeProvider,
  createTheme,
  styled
} from '@mui/material/styles'
import FrontPage from './containers/FrontPage'
import ResponsiveNavBar from './components/NavBar'

const queryClient = new QueryClient()

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

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingLeft: '0px',
  paddingRight: '0px',
  [theme.breakpoints.up('sm')]: {
    paddingLeft: '0px',
    paddingRight: '0px',
    maxWidth: '100%'
  }
}))

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider theme={theme}>
        <CustomContainer sx={{ padding: 0, margin: 0 }}>
          <ResponsiveNavBar />
          <FrontPage />
        </CustomContainer>
      </ThemeProvider>
    </QueryClientProvider>
  )
}

export default App
