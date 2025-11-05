import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(dept):
    try:
        response = requests.get(f'https://www.{dept}.ruet.ac.bd/teacher_list', timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        teachers = soup.find_all('tr')[1:]

        name_en, designation, phone, email, deptt = [], [], [], [], []

        for teacher in teachers:
            tds = teacher.find_all('td')
            if len(tds) < 7:
                continue
            name_en.append(tds[1].text.strip())
            designation.append(tds[3].text.strip())
            phone.append(tds[6].text.strip())
            email.append(tds[5].text.strip())
            deptt.append(tds[4].text.strip())

        data = pd.DataFrame({
            'Name': name_en,
            'Designation': designation,
            'Phone': phone,
            'Email': email,
            'Department': deptt
        })
        return data

    except Exception as e:
        st.error(f"Failed to fetch data for {dept.upper()} department: {e}")
        return pd.DataFrame()

def main():
    st.title("RUET Teachers' Information")

    # Department section
    depts = ['EEE', 'CSE', 'CHEM', 'MATH', 'PHY', 'SCI']
    dept = st.sidebar.selectbox('Select Department', depts).lower()

    if dept:
        data = get_data(dept)

        if not data.empty:
            # --- Add designation checkboxes ---
            st.sidebar.subheader("Filter by Designation")
            designations = sorted(data['Designation'].unique())

            selected_designations = []
            for des in designations:
                if st.sidebar.checkbox(des, value=True):
                    selected_designations.append(des)

            # Filter the dataframe
            filtered_data = data[data['Designation'].isin(selected_designations)]
            st.dataframe(filtered_data)

# Run the app
if __name__ == "__main__":
    main()
