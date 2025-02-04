export interface IMessage {
  content: string
  role: string
  id: string
}

export interface PostDataInput {
  [key: string]: string
}
