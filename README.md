# 🌍 Travel & Tourism Recommendation System

## 📌 Overview
This project implements a **Travel & Tourism Recommendation System** that combines **content-based** and **collaborative filtering** techniques to deliver **highly personalized travel destination suggestions** based on user preferences and behavior.  

## ✨ Features
- **Content-Based Filtering**: Recommends destinations based on features such as type, state, best time to visit, and user preferences — using **TF-IDF** and **cosine similarity**.  
- **Collaborative Filtering**: Analyzes user ratings and behaviors to find similar users and suggest destinations they enjoyed.  
- **Hybrid Recommendation Engine**: Combines the strengths of both approaches for improved accuracy.  
- **Flask Web App**: Interactive web interface for real-time personalized recommendations.  
- **Predictive Model**: Estimates destination popularity based on user profiles and preferences.  
- **Data Integration**: Seamlessly integrates multiple datasets, including destinations, reviews, user histories, and profiles.  

## 📂 Project Structure
```
├── app.py                                  # Main Flask application
├── Travel & Tourism Recommendation System Using.ipynb  # Jupyter Notebook for preprocessing & training
├── model.pkl                               # Trained ML model
├── data/                                   # Dataset files
│   ├── Expanded_Destinations.csv
│   ├── Final_Updated_Expanded_UserHistory.csv
│   └── final_df.csv
└── README.md                               # Project documentation
```

## 🛠 Requirements
- Python **3.13.5**  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zaid-mian/travel-Recomandation-system.git
   cd travel-Recomandation-system
   ```

2. Install the required packages:
   ```bash
   pip install Flask pandas numpy scikit-learn
   ```

3. Place the dataset files (`Expanded_Destinations.csv`, `Final_Updated_Expanded_UserHistory.csv`, `final_df.csv`) in the `data/` directory.  

4. Train the model and save it as `model.pkl` using the Jupyter Notebook.  

## 🚀 Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and go to:  
   👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  

3. Use the web interface to input user preferences and receive recommendations.  

## 📊 Data
- **Expanded_Destinations.csv**: Contains detailed information about travel destinations.  
- **Final_Updated_Expanded_UserHistory.csv**: Stores user visit history and ratings.  
- **final_df.csv**: Final dataset used for training the model.  

## 🤖 Model Training
The model is trained using a **hybrid approach** of collaborative filtering and content-based filtering.  
The Jupyter Notebook (`Travel & Tourism Recommendation System Using.ipynb`) provides step-by-step details on:  
- Data preprocessing  
- Feature engineering  
- Model training  
- Evaluation  

## 🤝 Contributing
Contributions are welcome! 🎉  
- Open an issue to suggest features or report bugs.  
- Submit a pull request with your changes.  

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

👨‍💻 Developed by [Zaid Mian](https://github.com/zaid-mian)  
🔗 GitHub Repo: [Travel & Tourism Recommendation System](https://github.com/zaid-mian/travel-Recomandation-system.git)
