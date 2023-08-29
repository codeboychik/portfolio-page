import streamlit as st
import csv
import pandas

st.set_page_config('My portfolio page', 'expanded')

col1, col2 = st.columns(2)
with col1:
    st.image('images/photo.JPG')

with col2:
    st.title('Andrey Chernenko')
    content = """Hey there, I'm Andrey Chernenko, a junior Python developer thrilled to be diving into the world of 
    programming headfirst. I've always been fascinated by the power of code to create, innovate, and solve real-world 
    problems. My journey started with a solid grasp of computer science fundamentals, and since then, I've been on a 
    quest to turn my passion into purposeful projects. Whether it's untangling complex coding puzzles or exploring 
    new libraries, I'm all in. I believe in the beauty of clean and efficient code and strive to make every line 
    count. Collaborative by nature, I'm not just looking to contribute, but to learn from experienced minds around 
    me. Joining the league of Python developers, I'm excited to embrace challenges, soak up knowledge, and chart my 
    course in this ever-evolving realm of technology. """
    st.info(content)

description = "On this page, I have placed the projects I have worked on." \
              " In case of any questions, feel free to contact me using the form below."
st.write(description)

col3, col4 = st.columns(2)

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    data = [row for row in reader]

df = pandas.read_csv('data.csv', sep=';')
half = int(len(df) / 2)


def get_layout(begin: int, end: int):
    for index, row in df.iloc[begin:end].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.write(f'[Source code]({row["url"]})')
        st.image(f'images/{row["image"]}')
        st.divider()


with col3:
    get_layout(0, half - 1)

with col4:
    get_layout(half, len(df))
