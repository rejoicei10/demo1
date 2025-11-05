import streamlit as st
from datetime import datetime

# ----- PAGE CONFIG -----
st.set_page_config(
    page_title="Demo Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----- SIDEBAR -----
st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to:", ["🏠 Home", "📈 Dashboard", "💬 About"])

# Add footer info in sidebar
st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Created by [Your Name](https://github.com/yourprofile)")
st.sidebar.write(datetime.now().strftime("%A, %d %B %Y"))

# ----- MAIN CONTENT -----
if page == "🏠 Home":
    st.title("Welcome to the Demo Streamlit App! 👋")
    st.markdown("""
    ### ✨ Overview
    This is a simple yet **good-looking Streamlit web app** demo.
    
    - Built with 🐍 Python & Streamlit  
    - Clean, minimal UI design  
    - Responsive layout with sidebar navigation  
    """)
    st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", use_column_width=True)

elif page == "📈 Dashboard":
    st.title("📈 Interactive Dashboard")
    st.write("Here's an example of a data visualization section:")

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Example data
    data = pd.DataFrame({
        'x': np.arange(1, 21),
        'y': np.random.randint(10, 100, 20)
    })

    # Show dataframe
    st.dataframe(data, use_container_width=True)

    # Plot chart
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'], marker='o')
    ax.set_title("Sample Line Chart")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

elif page == "💬 About":
    st.title("💬 About This App")
    st.markdown("""
    **Streamlit** makes it simple to build data apps in Python.

    **Features:**
    - 📊 Interactive charts  
    - 🧠 Machine learning integration  
    - 💾 Easy deployment (Streamlit Cloud / GitHub / Azure / etc.)

    ---
    💡 *Tip:* You can edit this page in `app.py` and instantly see updates!
    """)

# ----- FOOTER -----
st.markdown("---")
st.markdown("<center>🚀 Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
