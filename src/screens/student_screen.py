import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import base_layout, background_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import get_face_embeddings,train_classifier,predict_attendance
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student,get_student_subjects,get_student_attendance,unenroll_student_to_subject,enroll_student_to_subject
import time
from src.components.dailog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    
    student_data = st.session_state.student_data
    student_id=student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')

    with c1:
        header_dashboard()

    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)

    with c1:
        st.header('Your Enrolled Subjects')


    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
          enroll_dialog()


    st.divider()

    with st.spinner('Loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)
        # st.write(logs[0] if logs else "no logs")
  
    stats_map = {}
    for log in logs:
        sid = log['subject_id']
    
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1
        import pandas as pd

    table_data = []

    for log in logs:
        table_data.append({
            "Date": pd.to_datetime(log.get("timestamp")).strftime("%Y-%m-%d %I:%M %p"),
            "Status": "✅ Present" if log.get("is_present") else "❌ Absent"
        })

    df = pd.DataFrame(table_data)

    st.dataframe(df, use_container_width=True)
    # stats_map[sid]['attended'] += 1


    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid, {"total": 0, "attended": 0})
        def unenroll_button():
            if st.button("unenroll from this course",type='tertiary',width='stretch'):
                unenroll_student_to_subject(student_id,sid)
                st.toast(f'unenrolled from {sub['name']} sucessfully')
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ]

            )        






    footer_dashboard()


def student_screen():
    background_dashboard()
    base_layout()

    if"student_data" in st.session_state:
        student_dashboard()
        return()




   
    c1, c2 = st.columns(2, gap="small", vertical_alignment="center")
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back home", type="secondary", key="bckbtn"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login using Face ID", anchor="faceid")
    st.space()
    st.space()
    show_registration=False


    photo_source = st.camera_input("Position your face in center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
          detected,all_ids,num_faces=predict_attendance(img)

          if num_faces==0:
              st.warning('face not found')
          elif num_faces>1:
              st.warning('Multiple faces detected')
          else:
              if detected:
                  student_id =list(detected.keys())[0]
                  all_students=get_all_students()
                  student=next((s for s in all_students if s['student_id']==student_id),None)

                  if student:
                      st.session_state.is_logged_in=True
                      st.session_state.user_role='student'
                      st.session_state.student_data=student
                      st.toast(f'welcome back{student['name']}')
                      time.sleep(1)
                      st.rerun()

              else:
                   st.info('face not recognised')
                   show_registration=True

    if show_registration:
        with st.container(border=True):
            st.header('Register new profile')
            new_name=st.text_input("Enter your name",placeholder='E.g.= Rohan Thanvi')


            st.subheader('optional:Voice Enrollment')
            st.info("Enroll for voice only attendence")


            audio_data=None

            try:
                audio_data=st.audio_input('Record a short phrase like I am present,My name is akash.')
            except Exception:
                st.error('audio data failed')

            if st.button('create account',type='primary'):
               if new_name:
                   with st.spinner('creating profile'):
                       img=np.array(Image.open(photo_source))
                       encodings=get_face_embeddings(img)
                       if encodings:
                           face_emb=encodings[0].tolist()

                           voice_emb=None
                           if audio_data:
                               voice_emb=get_voice_embedding(audio_data.read())

                           response_data=create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)

                           if response_data:
                               train_classifier()
                               st.session_state.is_logged_in=True
                               st.session_state.user_role='student'
                               st.session_state.student_data=response_data[0]
                               st.toast('f profile created! Hi {new_name}!')
                               time.sleep(1)
                               st.rerun()
                           else:
                               st.error("couldnt capture your facial feature for  registration")



                               
               else:
                   st.warning('please enter your name')
                   
                   
                   footer_dashboard()