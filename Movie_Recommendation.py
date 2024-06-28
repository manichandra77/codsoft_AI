#Dataset - https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
ratings_file = '/kaggle/input/movielens-dataset/ratings.csv'
movies_file = '/kaggle/input/movielens-dataset/movies.csv'

df_ratings = pd.read_csv(ratings_file)
df_movies = pd.read_csv(movies_file)

# Merge ratings and movies data
movie_data = pd.merge(df_ratings, df_movies, on='movieId')

# Calculate rating counts and average rating for each movie
ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())

# Create user-item matrix
user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')

# Collaborative filtering function to recommend movies similar to a given movie
def recommend_similar_movies(movie_title, top_n=10):
    movie_ratings = user_movie_rating[movie_title]
    similar_movies = user_movie_rating.corrwith(movie_ratings)
    corr_movie = pd.DataFrame(similar_movies, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(ratings_mean_count['rating_counts'])
    recommendations = corr_movie[corr_movie['rating_counts'] > 50].sort_values('Correlation', ascending=False).head(top_n)
    return recommendations

# Function to recommend top-rated movies in specified genres
def recommend_movies_by_genre(genres, top_n=10):
    genre_movies = movie_data[movie_data['genres'].str.contains(genres, case=False)]
    top_rated_genre_movies = genre_movies.groupby('title')['rating'].mean().sort_values(ascending=False).head(top_n)
    return top_rated_genre_movies

# Example usage:
# Ask user for input
user_input = input("Enter a movie title or genre: ")

# Check if input matches a movie in the dataset
if user_input in user_movie_rating.columns:
    recommendations = recommend_similar_movies(user_input)
    print(f"Recommended movies based on '{user_input}':")
    print(recommendations)
else:
    # If input is a genre, recommend top-rated movies in that genre
    recommendations = recommend_movies_by_genre(user_input)
    print(f"Top-rated movies in the genre '{user_input}':")
    print(recommendations)
