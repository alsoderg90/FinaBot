from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import numpy as np
import faiss


class DocumentSearchService:

    def __init__(self, documents_folder='../../articles', chunk_size=500, chunk_overlap=50):
        self.chunk_overlap = chunk_overlap
        self.chunk_size = chunk_size
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.documents_folder = os.path.abspath(os.path.join(self.script_dir, documents_folder))
        self.documents = []
        self.split_documents = []
        self.vectorizer = TfidfVectorizer()
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.use_split_documents = False
        self.__load_documents()

        # Initialize the vectorizers
        self.tfidf_vectors = None
        self.sentence_embeddings = None
        self.faiss_index = None

    def search_relevant_documents(self, input_query, vector_type='sentence', split=False):
        """Search for the most relevant document(s) to a query."""
        self.use_split_documents = split
        # Find the most similar documents using TF-IDF vectors
        most_similar_documents_tfidf = self.__find_most_similar_documents(input_query, vector_type='tfidf')

        # Find the most similar documents using Sentence Embeddings
        most_similar_documents_sentence = self.__find_most_similar_documents(input_query, vector_type='sentence')

        # Get the highest similarity score for each set of documents
        highest_score_tfidf = max([score for _, score in most_similar_documents_tfidf])
        highest_score_sentence = max([score for _, score in most_similar_documents_sentence])

        print("highest_score_tfidf", highest_score_tfidf)
        print("highest_score_sentence", highest_score_sentence)

        if highest_score_tfidf == 0.2 and highest_score_sentence == 0.2:
            return []

        # Return the most relevant documents based on the highest similarity score
        if highest_score_sentence > highest_score_tfidf:
            return most_similar_documents_sentence
        else:
            return most_similar_documents_tfidf

    def __load_documents(self):
        """Load and split documents from the specified folder."""
        documents = []
        split_documents = []
        splitter = RecursiveCharacterTextSplitter(chunk_overlap=self.chunk_overlap, chunk_size=self.chunk_size)
        for filename in os.listdir(self.documents_folder):
            file_path = os.path.join(self.documents_folder, filename)
            if file_path.endswith(".md"):
                with open(file_path, "r", encoding="utf-8") as file:
                    document = file.read()
                    documents.append(document)
                    chunks = splitter.split_text(document)
                    split_documents.extend(chunks)
        self.documents = documents
        self.split_documents = split_documents

    def __vectorize_documents_tfidf(self):
        """Vectorize documents using TF-IDF."""
        documents = self.split_documents if self.use_split_documents else self.documents
        self.tfidf_vectors = self.vectorizer.fit_transform(documents)
        return self.tfidf_vectors

    def __vectorize_documents_sentence(self):
        """Vectorize documents using Sentence Transformers."""
        documents = self.split_documents if self.use_split_documents else self.documents
        self.sentence_embeddings = self.sentence_model.encode(documents, convert_to_numpy=True)

        # Create a FAISS index (L2 distance, assuming dense vectors) for fast similarity search
        dimension = self.sentence_embeddings.shape[1]
        self.faiss_index = faiss.IndexFlatL2(dimension)
        self.faiss_index.add(self.sentence_embeddings)

    def __find_most_similar_documents(self, query, vector_type='tfidf', top_k=5):
        """Find the most similar documents to a query."""
        documents = self.split_documents if self.use_split_documents else self.documents
        if vector_type == 'tfidf':
            if self.tfidf_vectors is None:
                self.__vectorize_documents_tfidf()
            query_vector = self.vectorizer.transform([query])
            similarities = cosine_similarity(query_vector, self.tfidf_vectors)
            most_similar_indices = np.argsort(similarities[0])[-top_k:][::-1]

            # Return the top k most similar documents and their similarity scores
            most_similar_documents = [(documents[idx], float(similarities[0][idx])) for idx in most_similar_indices]
            return most_similar_documents

        elif vector_type == 'sentence':
            if self.sentence_embeddings is None:
                self.__vectorize_documents_sentence()
            query_embedding = self.sentence_model.encode([query], convert_to_numpy=True)

            distances, most_similar_indices = self.faiss_index.search(query_embedding, top_k)

            # Return the top k most similar documents and their similarity scores
            most_similar_documents = [
                (documents[i], float(distances[0][j]))
                for j, i in enumerate(most_similar_indices[0])
            ]
            return most_similar_documents

        else:
            raise ValueError("Invalid vector type. Choose 'tfidf' or 'sentence'.")


if __name__ == "__main__":
    service = DocumentSearchService()
    query = "Mitä dimensiot ovat?"
    service.search_relevant_documents(query, vector_type='sentence')
