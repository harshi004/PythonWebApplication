import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Type of Dogs")
col1,col2,=st.columns(2)
with col1:
  st.subheader("Pomeranian")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fzeenews.india.com%2Fhindi%2Findia%2Fdelhi-ncr-haryana%2Fphoto-gallery-pomeranian-breed-dog-photos-price-colour-and-size-dog-which-is-not-dangerous-rncr%2F1345328&psig=AOvVaw32VnmjqEF7dEc1RC2d7qEN&ust=1704782177406000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMi5xt2WzYMDFQAAAAAdAAAAABAI",caption="Pomeranian",width=300,use_column_width=True)
  st.write("The Pomeranian is a tiny dog")
with col2:
  st.subheader("Shih Tzu")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fdogtime.com%2Fdog-breeds%2Fshih-tzu&psig=AOvVaw3W4Cdu0k-C9JMIrHlsAi4m&ust=1704782265993000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOC5iv6WzYMDFQAAAAAdAAAAABAD",caption="Shih Tzu",width=300,use_column_width=True)
  st.write("Shih Tzu means “little lion,” but there’s nothing fierce about this dog breed.")
