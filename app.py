import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["About", "Skills", "Projects", "Contact"],
        icons=["person", "tools", "diagram-3", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Load profile image
profile_pic = Image.open("profile_pic.png")

import streamlit.components.v1 as components

# About Section
if selected == "About":
    st.image(profile_pic, width=250)
    st.title("👋 Hi, I'm Sohail Nawaz")

    # Typing animation using HTML + JS
    st.markdown("""
        <style>
        .typewriter h3 {
          overflow: hidden;
          border-right: .15em solid #4CAF50;
          white-space: nowrap;
          margin: 0 auto;
          letter-spacing: .10em;
          animation: typing 3.5s steps(38, end), blink-caret .75s step-end infinite;
          font-family: 'Courier New', monospace;
          color: #4CAF50;
        }

        @keyframes typing {
          from { width: 0 }
          to { width: 100% }
        }

        @keyframes blink-caret {
          from, to { border-color: transparent }
          50% { border-color: #4CAF50; }
        }
        </style>

        <div class="typewriter">
            <h3>Full Stack Developer | AI Enthusiast | Designer</h3>
        </div>
    """, unsafe_allow_html=True)

    st.write("""
    I am passionate about building modern websites and apps using Python, TypeScript, and AI tools.
    This is my portfolio created using **Streamlit**.
    """)


# Skills Section
if selected == "Skills":
    st.header("🛠️ My Skills")
    st.write("- Python, JavaScript, TypeScript, HTML, CSS, Next.js, React")
    st.write("- Streamlit, TailwindCss, Chainlit")
    st.write("- Canva, Figma, UI/UX")
    st.write("- AI Tools (ChatGPT, chainlit, etc.)")

# Projects Section
if selected == "Projects":
    st.header("📂 My Projects")
    col1, col2 = st.columns(2)

    with col1:
        st.image("assets/project1.png", use_container_width=True)
        st.subheader("🔐 Password Strength Generator")
        st.markdown("[password_strength_meter ∙ main ∙ psm.py](https://password-strength-meter.streamlit.app)")
        st.write(
            "A Password Strength Meter is a user interface feature that evaluates the strength of a password in real-time. "
            "It provides visual feedback (e.g., color-coded bars or strength labels) to help users create secure passwords."
        )

    with col2:
        st.image("assets/project2.png", use_container_width=True)
        st.subheader("🧮 Simple Calculator")
        st.markdown("[simple_calculator_streamlit ∙ main ∙ main.py](https://simple-calculator-app.streamlit.app)")
        st.write(
            "A beginner-friendly calculator built with Streamlit that supports basic arithmetic operations: "
            "addition, subtraction, multiplication, and division. Enter numbers and instantly get results."
        )

# ---- Contact Section ----
if selected == "Contact":
    st.header("📞 Contact Me")

    # Custom CSS
    st.markdown("""
        <style>
        .contact-form {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 600px;
            margin: auto;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 12px 15px;
            margin: 10px 0 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
        }
        .contact-form button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .contact-form button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    # Contact Form
    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    with st.form(key='contact_form'):
        name = st.text_input("👤 Your Name")
        email = st.text_input("📧 Your Email")
        message = st.text_area("💬 Your Message")
        submit_button = st.form_submit_button(label='📨 Send')
        if submit_button:
            st.success("✅ Thank you! I will get back to you soon.")
    st.markdown('</div>', unsafe_allow_html=True)
