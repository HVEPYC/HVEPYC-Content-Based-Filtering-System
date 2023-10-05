# HVEPYC-Content-Based-Filtering-System
 
 This is a Content-Based Filtering System which was initially designed as part of a Data Science project for Semester 1 2022/23. This code was initially created to supplement the recommendation system of a Movie Recommendations website.

 The code in this example uses the dataset from MovieLens.org (https://grouplens.org/datasets/movielens/25m/) as an example for Content Based Filtering. This Filtering method can also be adapted to other Datasets, as long as information regarding Genres/Class/Type of data are present for the given unit of Data.

 The Code can be tested by Downloading the MovieLens dataset from the above link, and placing the unzipped "ml-25m" folder next to the Python Script. The Folder should contain both movies.csv and ratings.csv files.

 This code also includes a sample implementation where the user is asked to input their desired Genres, and the Program Generates the Top 10 movies which meet those criterias, arranged from highest to lowest Rating.

 This code can be adapted to be implemented in various other scenarios, and will work on any kind of data, as long as the user is given choice to select between different types of the item which is being recommended, and the dataset contains uniform genre/class/type information, along with a rating for each item. The rating could be generated as an aggregate of multiple user ratings, as shown in the example given, or can be sourced from a dataset which provides predefined ratings for each item.
 
 This Filtering system has the following prerequisites:
 - Requires a Modern version of Python (Tested on Python 3.10)
 - Requires a significant amount of RAM, which can vary by Dataset (Above example requires a minimum of 6GB available RAM space (Or RAM + Swap Memory))
 - A Modern CPU, to achieve reasonable runtimes for the processing of Data.

 This code is created completely by Harishankar Vinod (HVEPYC), and can be used under the MIT License as stated in this repository.

 References:
 - Dataset Obtained from: https://grouplens.org/datasets/movielens/25m/
 - Code-Specific references provided within thre ContentBasedFilteringRecommender.py Python file.
