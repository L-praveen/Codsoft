import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    'title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Prestige', 'Memento'],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'Batman sets out to dismantle the remaining criminal organizations.',
        'A team travels through a wormhole in space to ensure humanity\'s survival.',
        'Two magicians engage in a battle to create the ultimate illusion.',
        'A man with short-term memory loss attempts to track down his wife\'s murderer.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert text to feature vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute cosine similarity between all movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies
def recommend(title):
    # Get the index of the movie that matches the title
    idx = df[df['title'] == title].index[0]

    # Get similarity scores for all movies
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 3 similar movies (excluding itself)
    top_movies = sim_scores[1:4]

    # Get movie titles
    movie_indices = [i[0] for i in top_movies]
    return df['title'].iloc[movie_indices]

# Test the recommender
movie = "Inception"
print(f"Recommended for '{movie}':")
print(recommend(movie))
