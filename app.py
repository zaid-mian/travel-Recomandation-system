from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))
features = ['Name_x', 'State', 'Type', 'BestTimeToVisit', 'Preferences', 'Gender', 'NumberOfAdults', 'NumberOfChildren']

# Load data
destinations_df = pd.read_csv("Expanded_Destinations.csv")
userhistory_df = pd.read_csv("Final_Updated_Expanded_UserHistory.csv")
df = pd.read_csv("final_df.csv")

# Collaborative Filtering Setup
user_item_matrix = userhistory_df.pivot(index='UserID', columns='DestinationID', values='ExperienceRating')
user_item_matrix.fillna(0, inplace=True)
user_similarity = cosine_similarity(user_item_matrix)


def collaborative_recommend(user_id, user_similarity, user_item_matrix, destinations_df):
    if user_id - 1 >= len(user_similarity):
        return pd.DataFrame()

    similar_users = user_similarity[user_id - 1]
    similar_users_idx = np.argsort(similar_users)[::-1][1:6]
    similar_user_ratings = user_item_matrix.iloc[similar_users_idx].mean(axis=0)
    recommended_destinations_ids = similar_user_ratings.sort_values(ascending=False).head(5).index

    recommendations = destinations_df[destinations_df['DestinationID'].isin(recommended_destinations_ids)][[
        'DestinationID', 'Name', 'State', 'Type', 'Popularity', 'BestTimeToVisit'
    ]]

    return recommendations


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')


@app.route("/recommend", methods=['GET', 'POST'])
def recommend():
    if request.method == "POST":
        user_id = int(request.form['user_id'])

        user_input = pd.DataFrame([{
            'Name_x': request.form['name'],
            'Type': request.form['type'],
            'State': request.form['state'],
            'BestTimeToVisit': request.form['best_time'],
            'Preferences': request.form['preferences'],
            'Gender': request.form['gender'],
            'NumberOfAdults': int(request.form['adults']),
            'NumberOfChildren': int(request.form['children'])
        }])

        predicted_popularity = model.predict(user_input)[0]

        recommended_destinations = collaborative_recommend(user_id, user_similarity, user_item_matrix, destinations_df)

        return render_template('recommendation.html',
                               predicted_popularity=predicted_popularity,
                               recommended_destinations=recommended_destinations)

    return render_template('recommendation.html')


if __name__ == '__main__':
    app.run(debug=True)
