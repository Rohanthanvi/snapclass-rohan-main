import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import base_layout, background_home
from src.components.footer import footer_home


def home_screen():
    base_layout()

    header_home()
    background_home()
    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I am teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-teacher.png",width=145)
        if st.button('Teacher Portal',type='primary'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.header("I am student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png",width=110)
        if st.button('Student Portal',type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    footer_home()