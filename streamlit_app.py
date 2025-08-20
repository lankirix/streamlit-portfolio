import streamlit as st
import os
from PIL import Image

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
BASE_DIR = os.path.dirname(__file__)
logo_path = os.path.join(BASE_DIR, "public", "lankirix_logo.jpeg")

st.logo(Image.open(logo_path))
st.sidebar.markdown("Made with ❤️ by [Lankirix Automations](https://www.linkedin.com/in/lankirix/)")

# --- RUN NAVIGATION ---
pg.run()

