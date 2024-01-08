import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Type of Dogs")
col1,col2,col3,col4=st.columns(4)
with col1:
  st.subheader("Pomeranian")
  st.image("https://www.dailypaws.com/thmb/MGYnlOlOgW-14ZBI0ouXKJuQWeE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/pomeranian-white-puppy-921029690-2000-3ca2fdb56d144450a05c6990efdfd40e.jpg",caption="Pomeranian",width=300,use_column_width=True)
  st.write("Pomeranian dogs are small in stature but big in personality. Alert and confident, Pomeranians have a beautiful coat and charm to match.")
with col2:
  st.subheader("Shih Tzu")
  st.image("https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-178920540-e1689348859523.jpg?w=1024",caption="Shih Tzu",width=300,use_column_width=True)
  st.write("Shih Tzu means “little lion,” but there’s nothing fierce about this dog breed.")
with col3:
  st.subheader("Havanese")
  st.image("https://media4.giphy.com/media/S8rf64OiYYuCpESD9V/giphy.gif?cid=6c09b952c0k4hvsy9sg98zuzw9atnnbgxjdt3opdo9tanzoq&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g",caption="Havanese",width=300,use_column_width=True)
  st.write("The Havanese is a charming small dog breed with a long, silky coat, known for its playful demeanor, intelligence, and affectionate nature.")
with col4:
  st.subheader("Doremon")
  st.video("https://youtu.be/J4E1JH2nprs?si=WIE3ynga20IDwzCC")
  st.write("Doraemon is the name of a robot cat that came from the future to help a boy named Nobita Nobi.") 

 

