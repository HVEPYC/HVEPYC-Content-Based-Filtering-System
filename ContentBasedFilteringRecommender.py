#Created by HVEPYC

#Required Imports
import pandas

#Importing the Dataset that contains the movies which the Movie Recommendation system will use.
print("IMPORTS HAPPENING HERE #####################################")
MoviesAndGenreDF = pandas.read_csv(".\\ml-25m\\movies.csv", usecols=["movieId","title","genres"], dtype={"movieId":"int32","title":"str","genres":"str"})

#Putting every movie next to the Genre it is listed with into a new Dataframe
print("MOVIE NEXT TO GENRE IN DIFFERENT ROWS HAPPENING HERE #####################################")
MoviesWithEachGenreDF = MoviesAndGenreDF.set_index(["movieId","title"]).apply(lambda x: x.str.split("|").explode()).reset_index()

#Removing the movies which have (No Genres Listed) in the genre tab
print("REMOVAL OF (NO GENRES LISTED) HAPPENING HERE #####################################")
MoviesWithEachGenreDFtoDelete = MoviesWithEachGenreDF[ (MoviesWithEachGenreDF["genres"] == "(no genres listed)") ].index
MoviesWithEachGenreDF.drop(MoviesWithEachGenreDFtoDelete, inplace=True)

#Creation of Movie Database with Average Ratings for Each Movie from the movies in MoviesWithEachGenreDF
print("MOVIES AND RATINGS DATAFRAME BEING CREATED HERE ####################################")
#Importing The Reviews Dataset:
ratingsDF = pandas.read_csv(".\\ml-25m\\ratings.csv", usecols=["userId","movieId","rating"],dtype={"userId":"int32","movieId":"int32","rating":"float32"})

#Merging RatingsDF with the MoviesWithEachGenreDF:
MoviesAndAllRatingsDF = MoviesWithEachGenreDF.merge(ratingsDF, on="movieId")

#Finding Average Rating for each movie:
MoviesAndAvgRatingsDF = MoviesAndAllRatingsDF.groupby(["title"])["rating"].mean().sort_values(ascending=False).reset_index().rename(columns={"rating":"avgrating"})

#Creation of a Pivot Table containing Movies to Genres
print("PIVOT TABLE CREATION HAPPENING HERE #####################################")

#Addition of 1s in the table for Pivot Table 1 and 0 Differentiation
MoviesWithEachGenreDF["exists"] = 1

#Creating a Pivot table using MoviesWithEachGenreDF
MoviesWithEachGenrePivotTable = MoviesWithEachGenreDF.pivot_table(index="title", columns="genres", values="exists").fillna(0)

#Converting the Pivot Table back to a normal Dataframe
#We first remove "genres" which will give:
MoviesWithEachGenrePivotTable.columns.name = None

#Convert the Titles to have an index of their own:
MoviesWithEachGenreFinalDF = MoviesWithEachGenrePivotTable.reset_index()

#Content Based Recommendation Model Processes Here (Sample of Implementation):
print("Content Based Recommendation HAPPENING HERE #####################################\n")

#Simple Prototype Menu to enter Genres
print("Here are the Genres: ")
print("1. Action\n2. Adventure\n3. Animation\n4. Children\n5. Comedy\n6. Crime\n7. Documentary\n8. Drama\n9. Fantasy\n10. Film-Noir\n11. Horror\n12. IMAX\n13. Musical\n14. Mystery\n15. Romance\n16. Sci-Fi\n17. Thriller\n18. War\n19. Western")

InputGenreList=[]

while True:
    try:
        a=int(input("Enter Genre Number one by one, press enter after each genre input. Enter -1 to Stop: "))
        if a == -1:
            break
        elif a<-1 or a>19:
            print("Invalid Input")
        else:
            InputGenreList.append(a)
    except ValueError:
        continue

InputGenreList = list(dict.fromkeys(InputGenreList))
#Test Output (to be ignored)
print(InputGenreList,"\n")

#Dictionary of Genre to corresponding number:
GenreDict = {1:"Action",2:"Adventure",3:"Animation",4:"Children",5:"Comedy",6:"Crime",7:"Documentary",8:"Drama",9:"Fantasy",10:"Film-Noir",11:"Horror",12:"IMAX",13:"Musical",14:"Mystery",15:"Romance",16:"Sci-Fi",17:"Thriller",18:"War",19:"Western"}

#Generating List with Corresponding Genres as per selection
RealGenreList = []
for i in InputGenreList:
    z = GenreDict[i]
    RealGenreList.append(z)
print(RealGenreList,"\n\n")

#Finding the "Score" of specific Columns based on the given RealGenreList Input
print("FINDING SCORE AND RATINGS HAPPENING HERE ##########################################\n")
MoviesWithEachGenreFinalDF["Score"] = MoviesWithEachGenreFinalDF[RealGenreList].sum(axis=1)

#Removing Genre Columns after Finding the Score
MoviesWithEachGenreFinalDF.drop(MoviesWithEachGenreFinalDF.columns[1:20], axis=1, inplace=True)

#Merging the Average Ratings along with the MoviesWithEachGenreFinalDF Dataframe to get results
MoviesScoreAndRatingsDF = MoviesWithEachGenreFinalDF.merge(MoviesAndAvgRatingsDF, on="title")

#Sorting the Table on the basis of Highest Score and Highest Ratings
MoviesScoreAndRatingsDF.sort_values(by = ["Score","avgrating"], inplace=True, ascending=[False, False])

#Print out the Movies in a more Readable Manner:
print("The Movies Recommended based on your Genre Choices are as follows: \n")
Movies = MoviesScoreAndRatingsDF.head(10)["title"].values.tolist()
for i in Movies:
    print(i)


#Bibliography:
# https://grouplens.org/datasets/movielens/25m/
# https://www.includehelp.com/python/split-cell-into-multiple-rows-in-pandas-dataframe.aspx
# https://www.geeksforgeeks.org/drop-rows-from-the-dataframe-based-on-certain-condition-applied-on-a-column/
# https://stackoverflow.com/questions/24039023/add-column-with-constant-value-to-pandas-dataframe
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# https://www.youtube.com/watch?v=7flWNolPhsc
# https://www.statology.org/pandas-sum-specific-columns/
# https://www.geeksforgeeks.org/how-to-drop-one-or-multiple-columns-in-pandas-dataframe/
# https://sparkbyexamples.com/pandas/conver-pandas-column-to-list/
# https://sparkbyexamples.com/pandas/pandas-sort-dataframe-by-multiple-columns/