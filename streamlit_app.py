import streamlit as st

# --- 1. Custom CSS for Global Styles (No specific colors here) ---
# We define global styles (size, font, shadow) but leave color to the dynamic block (Section 4).
st.markdown("""
<style>
    /* Global style for all buttons */
    .stButton > button {
        height: 3.5em; /* Taller button */
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        width: 100%;
        margin: 5px 0; /* Add slight vertical margin */
        /* Ensure all buttons respond to hover */
        opacity: 1; 
    }
    .stButton > button:hover {
        opacity: 0.85;
    }
</style>
""", unsafe_allow_html=True)


# --- 2. Initialize Session State ---
# is_speaking now controls the color state for ALL buttons.
if 'is_speaking' not in st.session_state:
    st.session_state.is_speaking = False
if 'last_pressed' not in st.session_state:
    st.session_state.last_pressed = "App Initialized"

# --- 3. Define Callback Functions ---
def toggle_speak_stop():
    """Toggles the state, which changes the color of all buttons."""
    st.session_state.is_speaking = not st.session_state.is_speaking
    if st.session_state.is_speaking:
        st.session_state.last_pressed = "Toggled to SPEAK mode. All buttons are now RED."
    else:
        st.session_state.last_pressed = "Toggled to STOP mode. All buttons are now LIGHT GREEN."

def instructions_clicked():
    """Records the Instructions button press."""
    st.session_state.last_pressed = f"Instructions button pressed. Current mode: {'SPEAK (RED)' if st.session_state.is_speaking else 'STOP (GREEN)'}."

def chatgpt_clicked():
    """Records the ChatGPT button press."""
    st.session_state.last_pressed = f"ChatGPT button pressed. Current mode: {'SPEAK (RED)' if st.session_state.is_speaking else 'STOP (GREEN)'}."


# --- 4. Dynamic CSS (Applies color to ALL buttons based on state) ---
# This block generates a new style tag on every run to dynamically change the color of all buttons.
if st.session_state.is_speaking:
    # State: SPEAK (Button 1 label is "Speak"), Color: RED/White (for all buttons)
    button1_label = "Speak"
    dynamic_css = """
        <style>
        /* Target ALL Streamlit buttons by their shared class attribute */
        div[data-testid*="stButton"] button {
            background-color: #EF4444 !important; /* RED */
            color: white !important;
            border: 2px solid #EF4444 !important;
        }
        </style>
    """
else:
    # State: STOP (Button 1 label is "Stop"), Color: Light Green/Black (for all buttons)
    button1_label = "Stop"
    dynamic_css = """
        <style>
        /* Target ALL Streamlit buttons by their shared class attribute */
        div[data-testid*="stButton"] button {
            background-color: #A7F3D0 !important; /* LIGHT GREEN */
            color: black !important;
            border: 2px solid #A7F3D0 !important;
        }
        </style>
    """
st.markdown(dynamic_css, unsafe_allow_html=True)


# --- 5. Application Layout ---
st.title("Custom Streamlit Button Layout")
st.markdown("All buttons switch between **RED** (Speak) and **LIGHT GREEN** (Stop) states.")

# --- ROW 1: Toggle Button ---
st.header("Row 1: Toggle Button")
st.button(
    button1_label,
    on_click=toggle_speak_stop,
    key="speak_stop_button",
    use_container_width=True,
)

# --- ROW 2: Side-by-Side Buttons ---
st.header("Row 2: Side-by-Side Buttons")
col1, col2 = st.columns(2)

with col1:
    st.button(
        "Instructions",
        on_click=instructions_clicked,
        key="instructions_button",
        use_container_width=True,
    )

with col2:
    st.button(
        "ChatGPT",
        on_click=chatgpt_clicked,
        key="chatgpt_button",
        use_container_width=True,
    )


# --- 6. Status Display (Proof of Functionality) ---
st.markdown("---")
st.subheader("Button Status (Proof of Functionality)")

if st.session_state.is_speaking:
    st.success(f"Current Global Color Mode: **RED (Speak)**")
else:
    st.warning(f"Current Global Color Mode: **LIGHT GREEN (Stop)**")

st.info(f"Last Action: **{st.session_state.last_pressed}**")

st.markdown("---")
st.caption("Press the toggle button to change the color of all three buttons.")
