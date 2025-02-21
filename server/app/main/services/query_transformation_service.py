# generat class for query transformation service

class QueryTransformationService:
    def __init__(self):
        pass

    @staticmethod
    def rephrase_query(conversation_history, new_question):
        history = "\n\n".join([
            f"{msg['role'].capitalize()}: {msg['content']}"
            for msg in conversation_history
        ])
        template = f"""
        You are an AI assistant that answers questions based strictly on provided documents.
        You need rewrite this question so that it makes sense on its own, without the previous 
        conversation. If the new question makes sense on its own without the previous conversation,
        return it unchanged. Do not add any extra information. 
        Here is a conversation history:

        {history}

        Now, the user asks: "{new_question}"

        ## Instructions
        - Rewrite the question so that it makes sense on its own.
        - Do not add any extra information.
        - Use the same language as the question.
        - Do not provide document references.
        - Keep the question as short as possible.
        - If the question is already clear, return it unchanged.
        """
        return template

    @staticmethod
    def default_query(relevant_documents, user_input):
        context = "\n\n---\n\n".join([f"Document {i + 1}:\n{doc}" for i, (doc, _) in enumerate(relevant_documents)])

        template = f"""
        You are an AI assistant that answers questions based strictly on provided documents.

        ## Context
        Below are the relevant documents retrieved from a knowledge base:
        {context}

        ## Instructions
        - **Provide the most detailed, well-structured, and informative answer possible.**
        - **Include key details, explanations, and examples if possible.**
        - Do not use external knowledge beyond the provided documents.
        - If multiple documents provide different information, summarize the key points.
        - Ignore links and images.
        - If there is uncertainty, mention the limitations instead of making assumptions.
        - Use the same language as the question.
        - Avoid short answers and yes/no responses.
        - Do not provide document references.

        ## Question
        {user_input}

        ## Answer
        """
        return template


