import streamlit as st

# --- 1. Custom CSS for Global Styles and STATIC COLORS (Violet and Gray) ---
# This block defines global button styling and the static colors for buttons 2 and 3.
# We are now targeting specific data-testid AND button type for higher specificity.
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
        opacity: 1; 
        /* Ensure default text color for custom buttons is white unless specified */
        color: white !important; 
    }
    .stButton > button:hover {
        opacity: 0.85;
    }

    /* --- BUTTON 2: Instructions (STATIC Violet) --- */
    /* Target by key and specifically for 'secondary' type */
    div[data-testid*="instructions_button"] button[data-testid="stButton-secondary"] {
        background-color: #7B68EE !important; /* MediumSlateBlue (approx Violet) */
        border: 2px solid #7B68EE !important;
        color: white !important;
    }

    /* --- BUTTON 3: ChatGPT (STATIC Gray/Grey) --- */
    /* Target by key and specifically for 'secondary' type */
    div[data-testid*="chatgpt_button"] button[data-testid="stButton-secondary"] {
        background-color: #808080 !important; /* Gray */
        border: 2px solid #808080 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)


# --- 2. Initialize Session State ---
# is_speaking controls the color state for Button 1 only.
if 'is_speaking' not in st.session_state:
    st.session_state.is_speaking = False
if 'last_pressed' not in st.session_state:
    st.session_state.last_pressed = "App Initialized (Toggle button is Speak/Red)"

# --- 3. Define Callback Functions ---
def toggle_speak_stop():
    """Toggles the state, which changes the color of Button 1."""
    st.session_state.is_speaking = not st.session_state.is_speaking
    if st.session_state.is_speaking:
        st.session_state.last_pressed = "Toggled to SPEAK mode. Button 1 is now RED."
    else:
        st.session_state.last_pressed = "Toggled to STOP mode. Button 1 is now GREEN."

def instructions_clicked():
    """Records the Instructions button press."""
    st.session_state.last_pressed = "Instructions (Violet) button pressed."

def chatgpt_clicked():
    """Records the ChatGPT button press."""
    st.session_state.last_pressed = "ChatGPT (Gray) button pressed."


# --- 4. Dynamic CSS (Applies color to BUTTON 1 only based on state) ---
# This block ensures only the toggle button switches between Red and Green.
# We are now targeting specific data-testid AND button type for higher specificity.
if st.session_state.is_speaking:
    # State: SPEAK (Button 1 label is "Speak"), Color: RED/White
    button1_label = "Speak"
    dynamic_css = """
        <style>
        /* Target BUTTON 1 ONLY for the dynamic RED color, using its primary type */
        div[data-testid*="speak_stop_button"] button[data-testid="stButton-primary"] {
            background-color: #EF4444 !important; /* RED */
            color: white !important;
            border: 2px solid #EF4444 !important;
        }
        </style>
    """
else:
    # State: STOP (Button 1 label is "Stop"), Color: GREEN/Black
    button1_label = "Stop"
    dynamic_css = """
        <style>
        /* Target BUTTON 1 ONLY for the dynamic GREEN color, using its primary type */
        div[data-testid*="speak_stop_button"] button[data-testid="stButton-primary"] {
            background-color: #10B981 !important; /* GREEN */
            color: black !important; /* Black text for green button */
            border: 2px solid #10B981 !important;
        }
        </style>
    """
st.markdown(dynamic_css, unsafe_allow_html=True)


# --- 5. Application Layout ---
st.title("Custom Streamlit Button Layout (4 Colors)")
st.markdown("Button 1 toggles between **RED** (Speak) and **GREEN** (Stop). Buttons 2 & 3 are **Violet** and **Gray**.")

# --- ROW 1: Toggle Button (Red/Green) ---
st.header("Row 1: Toggle Button (Red/Green)")
st.button(
    button1_label,
    on_click=toggle_speak_stop,
    key="speak_stop_button",
    use_container_width=True,
    type="primary", # This button will be primary
)

# --- ROW 2: Side-by-Side Buttons (Violet/Gray) ---
st.header("Row 2: Static Buttons (Violet/Gray)")
col1, col2 = st.columns(2)

with col1:
    st.button(
        "Instructions",
        on_click=instructions_clicked,
        key="instructions_button",
        use_container_width=True,
        type="secondary", # This button will be secondary
    )

with col2:
    st.button(
        "ChatGPT",
        on_click=chatgpt_clicked,
        key="chatgpt_button",
        use_container_width=True,
        type="secondary", # This button will be secondary
    )


# --- 6. Status Display (Proof of Functionality) ---
st.markdown("---")
st.subheader("Button Status (Proof of Functionality)")

toggle_color = "RED (Speak)" if st.session_state.is_speaking else "GREEN (Stop)"
st.info(f"Button 1 Status: **{toggle_color}**")

st.success(f"Last Action: **{st.session_state.last_pressed}**")

st.markdown("---")
st.caption("Press any button to update the 'Last Action' status.")
