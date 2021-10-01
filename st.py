import streamlit as st
import requests

user = st.text_input('Write your country name')
btn = st.button('Enter')
if btn:
    r = requests.get(f'https://newsapi.org/v2/top-headlines?country={user}&category=sports&apiKey=ceb6c5d4169e4d928e146047d5cf4f30')
    res = r.json()
    data = res['articles']
    for i in data:     
        if i['author']:
            st.write("Author: ",i['author'])
        st.write('###',i['title'])
        st.write("Source: \n",i['source']['name'])
        st.write("Date: \n",i['publishedAt'].replace('T', ' ').replace('Z', ''))
        st.write("Link: \n",i['url'])
        if i['description']:
            st.write("Summary: \n",i['description'])
        if i['urlToImage']:
            st.image(i['urlToImage'])

