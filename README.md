Travel & Tourism Recommendation System
Overview
This project implements a Travel & Tourism Recommendation System that combines content-based and collaborative filtering techniques to deliver highly personalized travel destination suggestions based on user preferences and behavior.
Features
Content-Based Filtering: Recommends destinations based on features such as type, state, best time to visit, and user preferences. These features are converted to numeric vectors using TF-IDF and cosine similarity.
Collaborative Filtering: Analyzes user ratings and behaviors to find similar users and suggest destinations they enjoyed.
Hybrid Recommendation Engine: Combines the strengths of both content-based and collaborative filtering.
Flask Web App: Provides an interactive user interface for real-time personalized recommendations.
Predictive Model: Estimates destination popularity based on user profile and preferences.
Data Integration: Seamlessly integrates multiple datasets, including destinations, reviews, user histories, and profiles.
Project Structure
app.py: The main application file that sets up the Flask web server and defines the recommendation logic.
Travel & Tourism Recommendation System Using.ipynb: The Jupyter Notebook containing the data preprocessing, model training, and evaluation steps.
model.pkl: The trained machine learning model used for making predictions.
data: Directory containing the dataset files such as Expanded_Destinations.csv, Final_Updated_Expanded_UserHistory.csv, and final_df.csv.
Requirements
Python 3.13.5
Flask
Pandas
NumPy
Scikit-learn
Pickle
Installation
Clone the repository:
bash
git clone https://github.com/your-username/travel-recommendation-system.git
Install the required packages:
bash
pip install Flask pandas numpy scikit-learn
Place the dataset files (Expanded_Destinations.csv, Final_Updated_Expanded_UserHistory.csv, final_df.csv) in the data directory.
Train the model and save it as model.pkl using the Jupyter Notebook.
Usage
Run the Flask application:
bash
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/.
Use the web interface to input user preferences and get recommendations.
Data
Expanded_Destinations.csv: Contains detailed information about various travel destinations.
Final_Updated_Expanded_UserHistory.csv: Contains user visit history and ratings.
final_df.csv: The final dataset used for training the model.
Model Training
The model is trained using a combination of collaborative filtering and content-based filtering techniques. The Jupyter Notebook (Travel & Tourism Recommendation System Using.ipynb) provides a step-by-step guide to data preprocessing, feature engineering, model training, and evaluation.
Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
