#AI-POWERED-RECOMMENDATION-SYSTEM:


#PROJECT OVERVIEW:

the AI-POWERED-RECOMMENDATION-SYSTEM s a machine learning application which recommends movies on the basis of user's interest and different users' similar likes.

this project contains streamlit interface for user interaction which allow user to search their choice of movie and it would provide the top recommended movies to user along with their posters.


#features of this system: 
      -movie recommendation based on content similarity
      -interactive streamlit web application
      -movie poster display
      -fast recommendation 
      -easy to use interface


#dataset information:
      -dataset used is "TMDB 5000 Movie Dataset" 
      -files used are : 
                      -"tmdb_5000_movies.csv.zip"   
                      -"tmdb_5000_credits.csv.zip"


      -Dataset Columns Used:
                         -movie_id
                         -title
                         -genres
                         -cast
                         -crew
                         -keywords
      -datasets are merged on column 'title'


#Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle    


#Installation Requirements

Install the required Python libraries:
                   pip3 install pandas numpy scikit-learn streamlit requests

                   and install requirements.txt :
                         pip3 install -r requirements.txt


#run the project:
        -open the folder ai-movie-recommendation-system
        -now in terminal run, pythin3 -m streamlit run app.py
        -now your application is open in browser and you can browse the movies and can get recommendation on your interest basis                         


#folder structure of this project:
AI-MOVIE-RECOMMENDATION-SYSTEM:
|---motebook
         |-eda_and_model_building
         |-movies.pickle
         |-similarity.pkl
         |-datasets:--tmdb_5000_credits.csv.zip
                    --tmdb_5000_movie.csv.zip
|---pages
        |--about.py
        |--home.py
        |--recommendation.py
        |--search.py
|---project synopsis
|---app.py
|---movies.pickle
|---readme.md
|---requirements.txt
|---similarity.pkl
|---utlis.py



#working:
1. user enters or selects a movie.
2. application searches for the movie.
3. cosine similarity is calculates using trained similarity matrix
4. top 5 movies are recommended
5. posters are fetched using TMDB API


#Future Improvements:
- Collaborative filtering
- User login system
- Genre-based recommendations
- Personalized recommendations
- Deployment on Streamlit Cloud

