import { SyntheticEvent, useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import {
  Box,
  Container,
  TextField,
  Button,
  Paper,
  List,
  ListItem,
  ListItemText,
  Typography
} from '@mui/material'
import CssBaseline from '@mui/material/CssBaseline'
import { v4 as uuidv4 } from 'uuid'
import { IMessage } from './types'
import {
  ErrorResponse,
  handleError,
  postRequest
} from '../../api/api-utils'
import { AxiosError } from 'axios'
import ErrorModal from '../../components/ErrorComponent'
import ReactMarkdown from 'react-markdown'

const USER_ROLE = 'User'

function FrontPage() {
  const [input, setInput] = useState<string>('')
  const [messages, setMessages] = useState<IMessage[]>([])
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<ErrorResponse>()
  const newChatMessage = useMutation({
    mutationFn: postRequest,
    onSuccess: (data) => {
      setMessages((prev) => prev.concat(data as IMessage))
      setLoading(false)
    },
    onError: (error: unknown) => {
      if (error instanceof AxiosError) {
        const errorResponse = handleError(error)
        setError(errorResponse)
      }
      setLoading(false)
    }
  })

  const onSubmit = (e: SyntheticEvent) => {
    e.preventDefault()
    setLoading(true)
    newChatMessage.mutate({
      data: { data: input, history: messages },
      url: 'chat'
    })
    setMessages((prev) =>
      prev.concat({
        content: input,
        role: USER_ROLE,
        id: uuidv4()
      })
    )
    setInput('')
  }

  if (error) {
    return (
      <ErrorModal
        onClose={() => setError(undefined)}
        open={true}
        statusCode={error.statusCode}
        title={error.statusText}
        message={error.message}
      />
    )
  }

  return (
    <>
      <CssBaseline />
      <Container
        maxWidth='md'
        sx={{
          height: '85vh',
          minWidth: '50vh',
          display: 'flex',
          flexDirection: 'column',
          py: 4
        }}
      >
        <Paper
          elevation={3}
          sx={{
            flexGrow: 1,
            mb: 2,
            overflow: 'auto',
            maxHeight: 'calc(100vh - 200px)',
            bgcolor: 'background.paper'
          }}
        >
          <List>
            {messages.map((m) => (
              <ListItem
                key={m.id}
                sx={{
                  justifyContent:
                    m.role === USER_ROLE ? 'flex-end' : 'flex-start'
                }}
              >
                <Paper
                  elevation={1}
                  sx={{
                    p: 2,
                    maxWidth: '70%',
                    bgcolor:
                      m.role === USER_ROLE
                        ? 'primary.light'
                        : 'background.default',
                    color:
                      m.role === USER_ROLE
                        ? 'primary.contrastText'
                        : 'text.primary',
                    borderRadius:
                      m.role === USER_ROLE
                        ? '20px 20px 5px 20px'
                        : '20px 20px 20px 5px'
                  }}
                >
                  <ListItemText
                    primary={
                      <Typography
                        component='div'
                        sx={{
                          '& p': { margin: 0 }, // Poistaa ylimääräiset marginaalit
                          '& code': {
                            backgroundColor: '#f5f5f5',
                            padding: '2px 4px',
                            borderRadius: '4px',
                            fontFamily: 'monospace'
                          },
                          '& pre': {
                            backgroundColor: '#f5f5f5',
                            padding: '10px',
                            borderRadius: '4px',
                            overflowX: 'auto'
                          },
                          '& blockquote': {
                            borderLeft: '4px solid #ccc',
                            paddingLeft: '10px',
                            fontStyle: 'italic',
                            color: '#666'
                          }
                        }}
                      >
                        <ReactMarkdown>{m.content}</ReactMarkdown>
                      </Typography>
                    }
                  />
                </Paper>
              </ListItem>
            ))}
            {loading && (
              <ListItem sx={{ justifyContent: 'flex-start' }}>
                <Paper
                  elevation={1}
                  sx={{
                    p: 2,
                    bgcolor: 'background.default',
                    borderRadius: '20px 20px 20px 5px'
                  }}
                >
                  <ListItemText primary='Typing...' />
                </Paper>
              </ListItem>
            )}
          </List>
        </Paper>
        <Box
          component='form'
          onSubmit={onSubmit}
          sx={{ display: 'flex', gap: 1 }}
        >
          <TextField
            fullWidth
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder='Ask a question...'
            variant='outlined'
            size='small'
            sx={{
              '& .MuiOutlinedInput-root': {
                borderRadius: '20px',
                bgcolor: 'background.default'
              }
            }}
          />
          <Button
            type='submit'
            variant='contained'
            disabled={loading}
            sx={{
              borderRadius: '20px',
              minWidth: '100px'
            }}
          >
            Send
          </Button>
        </Box>
      </Container>
    </>
  )
}

export default FrontPage
