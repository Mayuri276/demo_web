import streamlit as st
## streamlit run main.py
name = st.text_input("Enter your Name : ")
fname = st.text_input("Enter your Father Name : ")
adr = st.text_area("Enter your Text : ")
Classdata = st.selectbox("Enter your Class :", (1,2,3,4,5,6))

button = st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    address : {adr}
    class : {Classdata}
 """)
