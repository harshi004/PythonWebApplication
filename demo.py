import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Type of Dogs")
col1,col2,=st.columns(2)
with col1:
  st.subheader("Pomeranian")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F754423375072546533%2F&psig=AOvVaw1PHKaSoGiZ5Cl-oA3wy-CO&ust=1704782417236000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDnh8iXzYMDFQAAAAAdAAAAABAY",caption="Pomeranian",width=300,use_column_width=True)
  st.write("The Pomeranian is a tiny dog")
with col2:
  st.subheader("Shih Tzu")
  st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dogster.com%2Flifestyle%2Ffacts-about-shih-tzu&psig=AOvVaw3W4Cdu0k-C9JMIrHlsAi4m&ust=1704782265993000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOC5iv6WzYMDFQAAAAAdAAAAABAY",caption="Shih Tzu",width=300,use_column_width=True)
  st.write("Shih Tzu means “little lion,” but there’s nothing fierce about this dog breed.")
