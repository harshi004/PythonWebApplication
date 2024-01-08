import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Crazy Things")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("DOREMON")
  st.image("https://m.media-amazon.com/images/M/MV5BNTkzNjJhYjQtNjU0Yy00Y2M3LWI2ZDgtNDRhZmNlNDFjMjQ5XkEyXkFqcGdeQXVyODk2ODI3MTU@._V1_FMjpg_UX1000_.jpg",caption="DOREMON",width=300,use_column_width=True)
  st.write("Doremon is a cartoon character,which helps to Nobita")
with col2:
  st.subheader("DOREMON Gif")
  st.image("https://i.pinimg.com/originals/59/30/74/593074c302700c41ae6fdfeca3d51563.gif",caption="GIF",width=300,use_column_width=True)
  st.write("Kiddo Doremon.")
with col3:
  st.subheader("Doremon")
  st.video("https://youtu.be/J4E1JH2nprs?si=WIE3ynga20IDwzCC")
  st.write("Doraemon is the name of a robot cat that came from the future to help a boy named Nobita Nobi.")   
