import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get(f'https://www.scrapethissite.com/pages/forms/').text
soup = BeautifulSoup(url, 'lxml')
players = soup.find_all('tr')
st.title("Web Scraping Example")
st.header("Scraped Player Data")
# print(players)
# st.write(players)

players = soup.find_all('tr')[1:]
# st.write(players[0])
# team_name = players[0].find_all('td')[0].text
# year = players[0].find_all('td')[1].text
# wins = players[0].find_all('td')[2].text
# losses = players[0].find_all('td')[3].text
# st.write(team_name, year, wins, losses)\
team_name = []
year = []
wins = []
losses = []

for i in players:
    team_name.append(i.find_all('td')[0].text.strip())
    year.append(i.find_all('td')[1].text.strip())
    wins.append(i.find_all('td')[2].text.strip())
    losses.append(i.find_all('td')[3].text.strip())
    # st.write(team_name, year, wins, losses)
    


# data = pd.DataFrame(columns=['Team Name', 'Year', 'Wins', 'Losses'])
data = {'Team Name': team_name, 'Year': year, 'Wins': wins, 'Losses': losses}
df = pd.DataFrame(data)
st.write(df)
