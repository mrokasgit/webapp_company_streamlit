import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')
st.title('The Best Company')
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.header("Our Team")

col1, col2, col3 = st.columns(3, gap ='small',vertical_alignment ='center')

df = pd.read_csv(r'C:\Users\mrokas\PycharmProjects\WebdesignSoloproject\data1.csv', sep = ',')

with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        path = r"C:\\Users\\mrokas\PycharmProjects\WebdesignSoloproject\images2\\" + row['image']
        st.image(path)
        st.write(row['role'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        path = r"C:\\Users\\mrokas\PycharmProjects\WebdesignSoloproject\images2\\" + row['image']
        st.image(path)
        st.write(row['role'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        path = r"C:\\Users\\mrokas\PycharmProjects\WebdesignSoloproject\images2\\" + row['image']
        st.image(path)
        st.write(row['role'])