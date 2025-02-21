from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os


class DocumentSearchService:

    def __init__(self, documents_folder='../../articles'):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.documents_folder = os.path.abspath(os.path.join(self.script_dir, documents_folder))
        self.documents = self.__load_documents()
        self.vectorizer = TfidfVectorizer()
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.tfidf_vectors = None
        self.sentence_embeddings = None

    def search_relevant_document(self, input_query, vector_type='sentence'):
        """Search for the most relevant document to a query."""
        # Example of finding the most similar document using TF-IDF vectors
        most_similar_document_tfidf, similarity_score_tfidf = self.__find_most_similar_documents(input_query, vector_type='tfidf')
        # Example of finding the most similar document using Sentence Embeddings
        most_similar_document_sentence, similarity_score_sentence = self.__find_most_similar_documents(input_query, vector_type='sentence')
        return most_similar_document_sentence if similarity_score_sentence < similarity_score_tfidf else most_similar_document_tfidf

    def __load_documents(self):
        """Load documents from the specified folder."""
        documents = []
        for filename in os.listdir(self.documents_folder):
            file_path = os.path.join(self.documents_folder, filename)
            if file_path.endswith(".md"):
                with open(file_path, "r", encoding="utf-8") as file:
                    documents.append(file.read())
        return documents

    def __vectorize_documents_tfidf(self):
        """Vectorize documents using TF-IDF."""
        self.tfidf_vectors = self.vectorizer.fit_transform(self.documents)
        return self.tfidf_vectors

    def __vectorize_documents_sentence(self):
        """Vectorize documents using Sentence Transformers."""
        self.sentence_embeddings = self.sentence_model.encode(self.documents)
        return self.sentence_embeddings

    def __find_most_similar_documents(self, query, vector_type='tfidf'):
        """Find the most similar documents to a query."""
        if vector_type == 'tfidf':
            if self.tfidf_vectors is None:
                self.__vectorize_documents_tfidf()
            query_vector = self.vectorizer.transform([query])
            similarities = cosine_similarity(query_vector, self.tfidf_vectors)
        elif vector_type == 'sentence':
            if self.sentence_embeddings is None:
                self.__vectorize_documents_sentence()
            query_embedding = self.sentence_model.encode([query])
            similarities = cosine_similarity(query_embedding, self.sentence_embeddings)
        else:
            raise ValueError("Invalid vector type. Choose 'tfidf' or 'sentence'.")

        # Get the index of the most similar document
        most_similar_idx = similarities.argmax()
        return self.documents[most_similar_idx], similarities[0][most_similar_idx]


if __name__ == "__main__":
    service = DocumentSearchService()
    query = "Mitä dimensiot ovat?"
    service.search_relevant_document(query, vector_type='sentence')
