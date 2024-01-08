import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Type of Dogs")
col1,col2,=st.columns(2)
with col1:
  st.subheader("Pomeranian")
  st.image(""C:\Users\harsh\OneDrive\Desktop\Dog1.jpg"",caption="Pomeranian",width=300,use_column_width=True)
  st.write("The Pomeranian is a tiny dog")
with col2:
  st.subheader("Shih Tzu")
  st.image(""C:\Users\harsh\OneDrive\Desktop\Shih Tzu.jpg",caption="Shih Tzu",width=300,use_column_width=True)
  st.write("Shih Tzu means “little lion,” but there’s nothing fierce about this dog breed.")
