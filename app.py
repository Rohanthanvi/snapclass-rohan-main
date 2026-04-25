import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

# st.header("This is the title of the app")
# name = st.text_input("enter your name")
# col1,col2 = st.columns(2, gap="medium")
# with col1:
#  if st.button("this is button1",key='button1"'):
#     st.write("hello",name)#THIS WILL WRITE IN STREAMLIT APP 
#     print(f"hello{name}") #this will print name in the terminal
# with col2:
#     if st.button("this is button2",key="button2"):
#        st.write("hurrayaa")
#        print("hurrayyyy")

#        st.markdown("""<div>
#                    img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" alt="gif" width="200"/>
#             </div>
#                    """,unsafe_allow_html=True)


# statefullness in stramlit where all the variables are reset to default value when the app is rerun but we can use session state to store the value of variable and it will not reset to default value when the app is rerun
if'login_type'not in st.session_state:
    st.session_state['login_type'] =None

match st.session_state['login_type']:
    case 'teacher':
        teacher_screen()
    case 'student':
        student_screen()
    case None:
        home_screen()
