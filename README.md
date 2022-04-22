# Books You Would Like
## Project Overview 
* Develop an end-to-end project that recommends the five books you would like according to relevant users’ ratings and book popularity.
* I have used 116 MB of data for this project.
* Engineered features by merging books, rating, and user datasets to get the number_of_rating column.
* For this Clustering project I have used Nearest Neighbors for accurate results. 
* Build the front-end of the project using streamlit.
* Deploy model using Heroku.
 

## Credit to youtube channel
[CampusX](https://www.youtube.com/channel/UCCWi3hpnq_Pe03nGxuS7isg)

## Data Collection
I used the following link to get data for books:
*	[IIF  Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)

The above data set contains three CSV files namely:
*	BX-Book-Ratings (1149780 rows)
*	BX-Books        (271360 rows)
*	BX-Users        (278858 rows)

## Data Cleaning
After collecting the required data, I have to clean it up to make it in the form I can use for my machine learning model. I did the following steps:

*	I loaded datasets by using error_bad_lines = false because data contains some erroneous lines.
*	Correctly label the columns so that it does not have space in their name.
*	Remove duplicate rows.
*	Correct the data type of columns.
*	Fill NaN values of the pivot table with 0.

## Collaborative Filtering
I narrowed my data sets by choosing those users who give ratings greater than 200. I merge the books and rating dataset to get the number_of_rating column and select only those books which have a number_of_ratings greater than and equal to 50. I made a pivot table whose columns contain user_id, index is book title and values are ratings. I created a sparse CSR matrix out of the pivot table to save memory for efficient model building.
![alt text](https://github.com/amber-asad25/books_you_would_like/blob/main/pivot-table.png "Pivot Table")  

## Model Building 

I used **Nearest Neighbors**for building my machine learning model, from sklearn because it is a very efficient clustering algorithm for unsupervised learning. I pass brute as an algorithm in the argument parameter because I want to calculate the total distance for every possible data point and then select the shortest one.  After fitting the model I find out 5 books I would like the most if I like certain books also.

## Application User Interface
I used streamlit to create the UI of this machine learning application.
![alt text](https://github.com/amber-asad25/books_you_would_like/blob/main/frond-end.png "Front-end")

## Model Deployment
In this step, I built a web application for my project by using Heroku. 
[link of web app](https://bywlamberasad.herokuapp.com/)
