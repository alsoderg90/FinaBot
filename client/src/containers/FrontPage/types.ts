export interface IMessage {
  content: string
  role: string
  id: string
}

export interface PostDataInput {
  input: string
  history: IMessage[]
}
