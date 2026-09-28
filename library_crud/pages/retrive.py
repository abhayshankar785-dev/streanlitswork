import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Read Specific Record")
id=st.text_input("Enter Book ID")
btn=st.button("Show Details")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.retrieve(id)

    st.table(record)
