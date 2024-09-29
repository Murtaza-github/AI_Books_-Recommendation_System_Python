import pandas as pd

books = pd.read_csv('books.csv')
users = pd.read_csv('users.csv')
ratings = pd.read_csv('ratings.csv')
books2 = pd.read_csv('books2.csv')

ratings_with_name = ratings.merge(books,on='ISBN')

num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)
    # num_rating_df

avg_rating_df = ratings_with_name.groupby('Book-Title').mean()['Book-Rating'].reset_index()
avg_rating_df.rename(columns={'Book-Rating':'avg_rating'},inplace=True)
    # avg_rating_df

popular_df = num_rating_df.merge(avg_rating_df,on='Book-Title')
    # popular_df

popular_df = popular_df[popular_df['num_ratings']>=200]
    # popular_df
popular_df.shape

popular_df=popular_df.merge(books2,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title',
                                                                                   'ISBN',
                                                                                   'Book-Author',
                                                                                   "Year-Of-Publication",
                                                                                   "Type","num_ratings",
                                                                                   "avg_rating"]]
def BookTypeRecommend(Book_Type):
    Books_Genre= popular_df[popular_df['Type']==Book_Type].head(10)
    x=Books_Genre.values.tolist()

    category = pd.read_csv("Books2.csv", usecols=["Type"])
    data1 = category.value_counts()
    print(data1)
    data=[]

    for i in x:
        data.append(i[0])
    return data
