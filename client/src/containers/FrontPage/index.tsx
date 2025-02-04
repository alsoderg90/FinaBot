import { SyntheticEvent, useState } from 'react'
import { useMutation } from '@tanstack/react-query'
import { postRequest } from './hooks'
import {
  Box,
  Container,
  TextField,
  Button,
  Paper,
  List,
  ListItem,
  ListItemText
} from '@mui/material'
import CssBaseline from '@mui/material/CssBaseline'
import { v4 as uuidv4 } from 'uuid'
import { IMessage } from './types'

const initialPOCState: IMessage[] = [
  {
    content: 'Mitä kuuluu',
    id: '123-123',
    role: 'user'
  },
  {
    content: 'Hyväää kiitos.',
    id: '123-124',
    role: 'ai'
  }
]

function FrontPage() {
  const [input, setInput] = useState<string>('')
  const [messages, setMessages] =
    useState<IMessage[]>(initialPOCState)
  const [loading, setLoading] = useState<boolean>(false)

  const newChatMessage = useMutation({
    mutationFn: postRequest,
    onSuccess: (data) => {
      setMessages((prev) => prev.concat(data))
      setLoading(false)
    },
    onError: (error) => console.log(error)
  })

  const onSubmit = (e: SyntheticEvent) => {
    e.preventDefault()
    setLoading(true)
    setMessages((prev) =>
      prev.concat({
        content: input,
        role: 'user',
        id: uuidv4()
      })
    )
    newChatMessage.mutate({ input })
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
                    m.role === 'user' ? 'flex-end' : 'flex-start'
                }}
              >
                <Paper
                  elevation={1}
                  sx={{
                    p: 2,
                    maxWidth: '70%',
                    bgcolor:
                      m.role === 'user'
                        ? 'primary.light'
                        : 'background.default',
                    color:
                      m.role === 'user'
                        ? 'primary.contrastText'
                        : 'text.primary',
                    borderRadius:
                      m.role === 'user'
                        ? '20px 20px 5px 20px'
                        : '20px 20px 20px 5px'
                  }}
                >
                  <ListItemText
                    primary={m.content}
                    sx={{
                      '& .MuiListItemText-primary': {
                        whiteSpace: 'pre-wrap'
                      }
                    }}
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
