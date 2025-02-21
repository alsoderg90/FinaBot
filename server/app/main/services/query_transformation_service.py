# generat class for query transformation service

class QueryTransformationService:
    def __init__(self):
        pass

    def default_query(self, relevant_document, user_input):
        template = """Answer the question based only on the following context:
        %s

        Question: %s
        """ % (relevant_document, user_input)
        return template


