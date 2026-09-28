import streamlit as st

from library_db import  BookListCreateRetrieveUpdateDelete

st.title('ADD BOOK')

title=st.text_input("title")
author=st.text_input("author")
price=st.number_input ("price",min_value=0)
pages=st.number_input("pages",min_value=0)
language=st.text_input("language")
btn = st.button("Add book")
if btn:
    b= BookListCreateRetrieveUpdateDelete()
    b.create(title,author,price,pages,language)
    st.success("Book added")
