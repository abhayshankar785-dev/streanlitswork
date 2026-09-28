import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("delete Specific Record")
id = st.text_input("Enter Book ID")
btn = st.button("delete")
if btn:
    if id:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.delete(id)
        if record==True:

            st.success("Book Deleted Successfully")
        else:
            st.error("Book Not Found")

    else:
        st.error("Book Not Found")
    # st.table(record)
