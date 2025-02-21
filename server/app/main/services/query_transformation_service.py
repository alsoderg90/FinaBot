# generat class for query transformation service

class QueryTransformationService:
    def __init__(self):
        pass

    def default_query(self, relevant_documents, user_input):
        print(len(relevant_documents))
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


