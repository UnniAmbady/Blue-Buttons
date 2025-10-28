import streamlit as st

# --- 1. Custom CSS for Styling (Static Colors) ---
# We make the CSS for buttons 2 and 3 more specific (using their keys) 
# to prevent the dynamic CSS from overriding them.
st.markdown("""
<style>
    /* Global style for all custom buttons */
    .stButton > button {
        height: 3.5em; /* Taller button */
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    }

    /* --- BUTTON 2: Instructions (Dark Blue) --- */
    /* We use the button's unique key container: st-emotion-cache-[hash]-Instructions-button */
    /* Target the container of the Instructions button using its key */
    [data-testid="stFormSubmitButton"] + div > button, 
    div[data-testid*="Instructions-button"] button {
        background-color: #1D4ED8 !important; /* Dark Blue */
        color: white !important;
        border: 2px solid #1D4ED8 !important;
        width: 100%;
    }

    /* --- BUTTON 3: ChatGPT (Dark Purple) --- */
    /* Target the container of the ChatGPT button using its key */
    [data-testid="stFormSubmitButton"] + div + div > button,
    div[data-testid*="chatgpt_button"] button {
        background-color: #7E22CE !important; /* Dark Purple */
        color: white !important;
        border: 2px solid #7E22CE !important;
        width: 100%;
    }

    /* Ensure buttons 2 & 3 retain their color on hover/focus */
    div[data-testid*="Instructions-button"] button:hover,
    div[data-testid*="chatgpt_button"] button:hover {
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)


# --- 2. Initialize Session State ---
if 'is_speaking' not in st.session_state:
    st.session_state.is_speaking = False
if 'last_pressed' not in st.session_state:
    st.session_state.last_pressed = "App Initialized"

# --- 3. Define Callback Functions ---
def toggle_speak_stop():
    """Toggles the state and updates the last pressed message."""
    st.session_state.is_speaking = not st.session_state.is_speaking
    if st.session_state.is_speaking:
        st.session_state.last_pressed = "Speak (Red) button was pressed. Now toggled to 'Stop'."
    else:
        st.session_state.last_pressed = "Stop (Light Green) button was pressed. Now toggled to 'Speak'."

def instructions_clicked():
    """Records the Instructions button press."""
    st.session_state.last_pressed = "Instructions (Dark Blue) button was pressed."

def chatgpt_clicked():
    """Records the ChatGPT button press."""
    st.session_state.last_pressed = "ChatGPT (Dark Purple) button was pressed."


# --- 4. Dynamic CSS for Button 1 (Toggle) ---
# This block generates a new style tag on every run to dynamically change the first button's color.
# We now use the unique data-testid to target this button explicitly, making the CSS highly specific.
if st.session_state.is_speaking:
    # State: STOP (Button label is "Stop"), Color: Light Green/Black
    button1_label = "Stop"
    button1_css = """
        <style>
        /* Target the Speak/Stop button using its unique key test ID */
        div[data-testid*="speak_stop_button"] button {
            background-color: #A7F3D0 !important; /* Light Green */
            color: black !important;
            border: 2px solid #A7F3D0 !important;
        }
        </style>
    """
else:
    # State: SPEAK (Button label is "Speak"), Color: Red/White
    button1_label = "Speak"
    button1_css = """
        <style>
        /* Target the Speak/Stop button using its unique key test ID */
        div[data-testid*="speak_stop_button"] button {
            background-color: #EF4444 !important; /* Red */
            color: white !important;
            border: 2px solid #EF4444 !important;
        }
        </style>
    """
st.markdown(button1_css, unsafe_allow_html=True)


# --- 5. Application Layout ---
st.title("Custom Streamlit Button Layout")
st.markdown("This application uses custom CSS to style native Streamlit buttons.")

# --- ROW 1: Toggle Button ---
st.header("Row 1: Toggle Button")
st.button(
    button1_label,
    on_click=toggle_speak_stop,
    key="speak_stop_button",
    use_container_width=True,
    # Setting type="primary" to give it a distinct CSS anchor
    type="primary"
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
        type="secondary" # Used to distinguish from the primary button type
    )

with col2:
    st.button(
        "ChatGPT",
        on_click=chatgpt_clicked,
        key="chatgpt_button",
        use_container_width=True,
        type="secondary" # Used to distinguish from the primary button type
    )


# --- 6. Status Display (Proof of Functionality) ---
st.markdown("---")
st.subheader("Button Status (Proof of Functionality)")

if st.session_state.is_speaking:
    st.success(f"Current Status: **Speaking** (Toggle button shows **Stop**)")
else:
    st.warning(f"Current Status: **Stopped** (Toggle button shows **Speak**)")

st.info(f"Last Action: **{st.session_state.last_pressed}**")

st.markdown("---")
st.caption("Press any button to update the 'Last Action' status above.")
