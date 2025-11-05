import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# ----- PAGE SETTINGS -----
st.set_page_config(page_title="Web Scraping Example", page_icon="🕸️", layout="wide")

st.title("🕸️ Web Scraping Example")
st.header("🏒 NHL Team Performance Data")

# ----- SCRAPE DATA -----
url = "https://www.scrapethissite.com/pages/forms/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Extract table rows (skip the header row)
rows = soup.find_all("tr")[1:]

team_name = []
year = []
wins = []
losses = []

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 4:  # prevent index errors
        team_name.append(cols[0].text.strip())
        year.append(cols[1].text.strip())
        wins.append(cols[2].text.strip())
        losses.append(cols[3].text.strip())

# Create DataFrame
df = pd.DataFrame({
    "Team Name": team_name,
    "Year": year,
    "Wins": wins,
    "Losses": losses
})

# ----- DISPLAY -----
st.dataframe(df, use_container_width=True)
st.success(f"✅ Successfully scraped {len(df)} rows of data!")
