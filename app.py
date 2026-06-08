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

    # 🛠️ THE ULTIMATE FULL-APP DESIGN CONFIG (Fixes everything: Inputs, Modals, Toasts & ALL Buttons)
    st.markdown(
        """
        <style>
        /* 1. TOAST NOTIFICATIONS FIX */
        div[data-testid="stToast"] {
            background-color: #1e222b !important;
            border: 1px solid #ff4b4b !important;
            border-radius: 8px !important;
        }
        div[data-testid="stToast"] div, 
        div[data-testid="stToast"] span, 
        div[data-testid="stToast"] p {
            color: #ffffff !important;
            font-weight: 500 !important;
        }

        /* 2. DIALOG / POPUP MODALS FIX */
        div[role="dialog"], 
        div[data-testid="stModal"],
        div[data-testid="stDialog"] div,
        div[role="dialog"] div[data-testid="stVerticalBlock"] {
            background-color: #ffffff !important;
        }
        div[role="dialog"] h1, div[role="dialog"] h2, div[role="dialog"] h3, 
        div[role="dialog"] p, div[role="dialog"] span, div[data-testid="stModal"] p,
        div[data-testid="stModal"] h3, div[data-testid="stModal"] span {
            color: #111111 !important;
        }

        /* 3. INPUT BOXES FIX */
        .stTextInput input {
            color: #111111 !important; 
            background-color: #ffffff !important; 
            border: 1px solid #cccccc !important; 
            font-size: 1rem !important;
            border-radius: 6px !important;
        }
        .stTextInput input:focus {
            border-color: #ff4b4b !important;
            box-shadow: 0 0 0 1px #ff4b4b !important;
        }

        /* 4. WIDGET LABELS & TITLES FIX */
        label[data-testid="stWidgetLabel"] p, 
        .stWidgetLabel p,
        div[data-testid="stWidgetLabel"] span,
        .stTextInput label p,
        div[data-testid="stWidgetLabel"] p span {
            color: #111111 !important;
            font-weight: 600 !important;
            opacity: 1 !important;
        }

        /* 5. HEADINGS & MARKDOWN FIX */
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] p,
        span[data-font="sans serif"],
        div[data-testid="stVerticalBlock"] p,
        .stApp h1, .stApp h2, .stApp p, .stApp h3 {
            color: #111111 !important;
        }

        /* 6. BUTTONS SOLID STYLE FIX: Targets Normal Buttons, File Uploaders, and Camera/Snapshot Buttons */
        .stButton>button, 
        div[data-testid="stFileUploader"] button,
        div[data-testid="stCameraInput"] button,
        button[data-testid="baseButton-secondary"],
        button[data-testid="baseButton-primary"] {
            border-width: 1px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }
        
        /* Force background fill and text contrast on ALL types of buttons */
        .stButton>button p, 
        .stButton>button span,
        div[data-testid="stFileUploader"] button p,
        div[data-testid="stFileUploader"] button span,
        div[data-testid="stCameraInput"] button p,
        div[data-testid="stCameraInput"] button span,
        button[data-testid="baseButton-secondary"] p,
        button[data-testid="baseButton-primary"] p {
            color: #ffffff !important;
        }
        
        /* Tertiary (borderless) buttons fallback safely to dark grey text */
        button[data-testid="baseButton-tertiary"] p {
            color: #111111 !important;
        }

        /* Clean active/click scaling effect */
        .stButton>button:active, div[data-testid="stFileUploader"] button:active, div[data-testid="stCameraInput"] button:active {
            transform: scale(0.98) !important;
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