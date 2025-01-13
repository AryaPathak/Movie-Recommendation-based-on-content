
# Movie Recommendation System  

This project builds a **Movie Recommendation System** using natural language processing (NLP) techniques and machine learning algorithms. It processes metadata from movies and provides recommendations based on user preferences.

Live Link: https://movie-recommendation-based-on-content.onrender.com/
---

## Features  
- **Data Merging and Cleaning**: Combines `movies` and `credits` datasets into a unified dataset. Handles missing values and cleans up fields like genres, cast, keywords, and crew.  
- **Tags Creation**: Generates a consolidated "tags" column for each movie by combining its overview, cast, crew, genres, and keywords.  
- **Text Preprocessing**: Includes converting text to lowercase, removing spaces, and stemming for efficient text analysis.  
- **Recommendation Model**: Recommends similar movies based on processed data using cosine similarity.  

---

## Dataset  
The project uses the [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle.  

- `tmdb_5000_movies.csv`  
- `tmdb_5000_credits.csv`  

---

## Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/yourusername/movie-recommendation-system.git  
   cd movie-recommendation-system  
   ```  
2. Install dependencies:  
   ```bash  
   pip install numpy pandas matplotlib nltk  
   ```  
3. Place the dataset in the `data/` directory:  
   ```
   data/
   ├── tmdb_5000_movies.csv  
   ├── tmdb_5000_credits.csv  
   ```  

---

## Usage  
1. Run the preprocessing script to clean and transform the data:  
   ```bash  
   python preprocess.py  
   ```  
2. Build the recommendation model using similarity:  
   ```bash  
   python recommend.py  
   ```  
3. Interact with the system to get movie recommendations.  

---

## Key Python Modules  
- **NumPy**: For numerical operations.  
- **Pandas**: For data manipulation and preprocessing.  
- **Matplotlib**: For data visualization (optional).  
- **NLTK**: For text preprocessing (lowercasing, stemming).  

---

## Future Enhancements  
- Integrate a front-end interface (e.g., Flask or Django).  
- Add advanced recommendation algorithms (e.g., collaborative filtering).  
- Improve tag generation with advanced NLP models (e.g., BERT).  

---

## License  
This project is licensed under the MIT License. See the LICENSE file for details.  

---

## Acknowledgments  
- Datasets provided by [Kaggle](https://www.kaggle.com).  
- Inspiration from various machine learning projects and online tutorials.  
