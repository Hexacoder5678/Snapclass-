import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png",
        layout="wide"  
    )
    st.markdown(
        """
        <style>
        /* Sirf white rounded columns aur cards ke andar ke text ko charcoal black karo */
        div[style*="background-color"] p,
        div[style*="background-color"] h1,
        div[style*="background-color"] h2,
        div[style*="background-color"] h3,
        .stHeadingContainer h2,
        .stHeadingContainer h3 {
            color: #1a1a1a !important;
        }
        
        /* Main blue screen ke headings aur welcome text ko white rehne do */
        .stApp h1, .stApp h2, .stApp p {
            text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
        }

        /* Buttons ke text ko white pe lock rakho aur cursor pointer banao */
        .stButton>button {
            color: #ffffff !important;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

if __name__ == "__main__":
    main()