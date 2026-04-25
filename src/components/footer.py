import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;align-items:center;">
            <p>Created with ❤️ by rohan</p>
        </div>
    """, unsafe_allow_html=True)