import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Type of Dogs")
col1,col2,=st.columns(2)
with col1:
  st.subheader("Pomeranian")
  st.image("https://i.pinimg.com/736x/d5/c1/3a/d5c13a12e7af47674c253a2b4dab14d8.jpg",caption="Pomeranian",width=300,use_column_width=True)
  st.write("The Pomeranian is a tiny dog")
with col2:
  st.subheader("Shih Tzu")
  st.image("https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-178920540-e1689348859523.jpg?w=1024",caption="Shih Tzu",width=300,use_column_width=True)
  st.write("Shih Tzu means “little lion,” but there’s nothing fierce about this dog breed.")
