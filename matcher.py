from sklearn.feature_extraction.text import (
    TfidfVectorizer,
    CountVectorizer
)

from sklearn.metrics.pairwise import cosine_similarity




# TF-IDF SIMILARITY

def calculate_tfidf_similarity(
    resume_text,
    job_text
):

    texts = [resume_text, job_text]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return similarity[0][0] * 100




# BAG OF WORDS SIMILARITY

def calculate_bow_similarity(
    resume_text,
    job_text
):

    texts = [resume_text, job_text]

    vectorizer = CountVectorizer()

    bow_matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        bow_matrix[0:1],
        bow_matrix[1:2]
    )

    return similarity[0][0] * 100