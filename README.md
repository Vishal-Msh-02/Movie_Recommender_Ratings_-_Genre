🎬 Movie Recommendation System using Machine Learning

A personalized movie recommendation web app that suggests top-rated similar movies based on a selected title or genre. Built using Machine Learning (TF-IDF + Cosine Similarity) and deployed with Streamlit.

🔗 Live App: https://movierecommenderratings-genre-ds4rsdgzpk3rq2vrafqk4b.streamlit.app/

📌 Features
🔍 Movie-based Recommendations
   Select a movie to get 5 similar recommendations, sorted by rating.

🎭 Genre-based Recommendations
  Choose a genre to discover the top 5 highest-rated movies in that category.

🖼️ Poster Display using TMDb API
    Fetches and displays movie posters alongside recommendations.

⚡ Lightweight TF-IDF engine
Uses text vectorization on movie genres and titles for fast, relevant suggestions.

📊 How It Works
1. Data Sources:
IMDb Datasets: title.basics.tsv, title.ratings.tsv

TMDb API: For movie poster retrieval

2. Preprocessing:
Merged title and rating data

Created a tags column from primaryTitle + genres

Filtered to movies with numVotes > 1000 for quality

3. ML Technique:
Vectorized text using TF-IDF

Calculated similarity using cosine similarity

Returned top matches by rating and relevance

🛠 Tech Stack
Tool	Purpose
Python	Core language
Pandas	Data preprocessing
scikit-learn	TF-IDF + Cosine similarity
Streamlit	Web app framework
TMDb API	Fetching movie posters

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app locally
bash
Copy
Edit
streamlit run app.py
Or visit the live app — no setup needed!
https://movierecommenderratings-genre-ds4rsdgzpk3rq2vrafqk4b.streamlit.app/

📷 Screenshots
Movie-based	
![image](https://github.com/user-attachments/assets/5aed86cb-c670-4cfe-ab43-98c0ef154ea9)

Genre-based
![image](https://github.com/user-attachments/assets/c95a049f-96b7-47f0-86bb-1173d3d1f9d5)


💡 Future Enhancements
🔍 Add search bar with autocomplete

📈 Include synopsis or reviews from TMDb

🌐 Deploy using Hugging Face Spaces or Heroku for broader options

💾 Use a compressed similarity.npz to speed up cold starts

👨‍💻 Author
Vishal Maheshwary
GitHub : https://github.com/Vishal-Msh-02 

LinkedIn : www.linkedin.com/in/vishal-maheshwary

