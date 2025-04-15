from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_texts, job_description):
    documents = resume_texts + [job_description]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)
    
    job_vector = tfidf_matrix[-1]
    resume_vectors = tfidf_matrix[:-1]

    similarities = cosine_similarity(resume_vectors, job_vector)
    ranked = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)

    return ranked
