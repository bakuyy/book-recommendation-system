import streamlit as st
import pickle

books = pickle.load(open("books_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
books_list = books['title'].values


st.header("Book Recommendation System")
select_value= st.selectbox("Select books from dropdown", books_list)


def recommend(book):
    index = books[books['title'] == book].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True, key=lambda vector:vector[1])
    book_recs=[]
    for i in distance[1:6]:
        book_recs.append((books.iloc[i[0]].title))
    return book_recs

if st.button("Show recommendations"):
    book_name = recommend(select_value)
    for i in range(5):
        st.text(book_name[i])