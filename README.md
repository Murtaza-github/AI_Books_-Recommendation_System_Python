# AI_Books_-Recommendation_System_Python
The Books Recommendation System is an AI-driven application designed to enhance the book discovery experience. It provides users with personalized book recommendations based on either a specific book title or a selected category. By leveraging machine learning algorithms, the system offers curated book suggestions, helping readers find their next favorite book effortlessly. The system uses a machine learning approach to deliver personalized book recommendations. For book name-based recommendations, the system leverages the cosine similarity algorithm to compare user-provided input with existing book data. For category-based recommendations, the system filters books by genre and suggests top-rated books within that category.

# Features

The Books Recommendation System is an AI-powered application that provides personalized book suggestions. It offers two key features:

	1 Recommendation by Book Name:
		•	Users can input the name of thier favourite book, and the system will recommend similar books that the user may like to read.
		• 	The recommendation is based on an AI algorithm that evaluates similarity between books using "Cosine similarity".
 
	2.	Recommendation by Book Category:
		• 	Users can select a book category (e.g., Classic, Action, Fantasy, Horror, or Fiction) and receive recommendations for books within the chosen genre.

 # Main Modules:

	1.	AiBooks Module: Handles book recommendations based on user-provided book names using similarity algorithms.
	2.	AiBookType Module: Filters and recommends books based on the selected category.

 # Technologies Used

	•	Python: Core programming language for building the application.
	•	Tkinter: Used for creating the graphical user interface (GUI).
	•	Pandas: For managing and processing book, user, and rating data from CSV files.
	•	NumPy: For numerical computations, including matrix operations in the recommendation algorithm.
	•	Scikit-learn: Provides the cosine similarity function for measuring similarity between books based on user ratings.
	•	Cosine Similarity Algorithm: The AI algorithm used to find similar books based on ratings.

# Database Schema

The system uses CSV files as a lightweight database to store book data, user information, and user ratings:

	•	books.csv: Contains book details such as ISBN, title, and author.
	•	users.csv: Stores user information.
	•	ratings.csv: Contains user ratings for books, which is used in the recommendation algorithm.
	•	books2.csv: Includes additional details like book categories, enabling category-based recommendations.

These datasets are pre-processed and analyzed to generate relevant book suggestions for the users.

# How to Use
	1.	Clone the Repository
	2.	Install Dependencies: Ensure that all required Python packages are installed. You can install the dependencies using 
 		• 	pip:pip install numpy pandas scikit-learn tkinter
	3.	Using the Book Recommendation System:
		• 	Book by Name: Enter a book name in the input field and click “Search Book” to get a list of similar books that you may enjoy.
  		• 	Some names of book can be find in "sample_books_tested.txt" file 
		• 	Book by Category: Choose a category (e.g., Action, Fantasy, Fiction) from the dropdown and click “Search Book” to receive recommendations within that genre.
	4.	Clear Search:
		•	Both features allow users to clear the search and results using the “Clear Search” button.
