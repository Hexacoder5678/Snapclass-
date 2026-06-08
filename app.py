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

    # 🛠️ THE ULTIMATE FULL-APP THEME & GLOBAL CONTRAST FIX
    st.markdown(
        """
        <style>
        /* 1. TOAST NOTIFICATIONS FIX: Toasts ka background dark aur text white lock karo */
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

        /* 2. DIALOG / POPUP MODALS FIX: Modals ka background white aur text black */
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

        /* 3. INPUT BOXES FIX: Background white aur typed text pure black */
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

        /* 4. WIDGET LABELS & TITLES FIX: 'Enter username' aur 'Enter password' ko forceful black karo */
        label[data-testid="stWidgetLabel"] p, 
        .stWidgetLabel p,
        div[data-testid="stWidgetLabel"] span,
        .stTextInput label p,
        div[data-testid="stWidgetLabel"] p span {
            color: #111111 !important;
            font-weight: 600 !important;
            opacity: 1 !important;
        }

        /* 5. HEADINGS & MARKDOWN FIX: Badi headings aur baaki ke normal texts ko sharp black karo */
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] p,
        span[data-font="sans serif"],
        div[data-testid="stVerticalBlock"] p,
        .stApp h1, .stApp h2, .stApp p, .stApp h3 {
            color: #111111 !important;
        }

        /* 6. BUTTONS SOLID STYLE FIX: Restore full solid colors and override look */
        .stButton>button {
            border-width: 1px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }
        
        /* Buttons text inside wrappers will automatically adapt safely to button types */
        .stButton>button p, 
        .stButton>button span,
        div[data-testid="stBaseButton-primary"] p,
        div[data-testid="stBaseButton-secondary"] p {
            color: #ffffff !important;
        }
        
        /* Tertiary or border-only buttons fallback to safe visible dark states if transparent */
        div[data-testid="stBaseButton-tertiary"] p {
            color: #111111 !important;
        }

        .stButton>button:active {
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