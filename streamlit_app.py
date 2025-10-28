import streamlit as st

# --- 2. Initialize Session State (Set to SPEAK/RED state on first run) ---
if 'is_speaking' not in st.session_state:
    st.session_state.is_speaking = True # Start in SPEAK (RED) mode
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


# --- 4. Dynamic/Static CSS Injection (Combined into one block for consistency) ---
if st.session_state.is_speaking:
    # State: SPEAK (Button 1 label is "Speak"), Color: RED/White
    button1_label = "Speak"
    dynamic_toggle_style = """
        /* Target BUTTON 1 ONLY for the dynamic RED color, using its primary type */
        div[data-testid*="speak_stop_button"] button[data-testid="stButton-primary"] {
            background-color: #EF4444 !important; /* RED */
            color: white !important;
            border: 2px solid #EF4444 !important;
        }
    """
else:
    # State: STOP (Button 1 label is "Stop"), Color: GREEN/Black
    button1_label = "Stop"
    dynamic_toggle_style = """
        /* Target BUTTON 1 ONLY for the dynamic GREEN color, using its primary type */
        div[data-testid*="speak_stop_button"] button[data-testid="stButton-primary"] {
            background-color: #10B981 !important; /* GREEN */
            color: black !important; /* Black text for green button */
            border: 2px solid #10B981 !important;
        }
    """

# Combine Global, Static, and Dynamic CSS into one style block for consistent rendering
full_css = f"""
<style>
    /* Global style for all buttons */
    .stButton > button {{
        height: 3.5em; 
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        width: 100%;
        margin: 5px 0;
        opacity: 1; 
    }}
    .stButton > button:hover {{
        opacity: 0.85;
    }}

    /* --- BUTTON 2: Instructions (STATIC Violet) --- */
    div[data-testid*="instructions_button"] button[data-testid="stButton-secondary"] {{
        background-color: #7B68EE !important; /* MediumSlateBlue (approx Violet) */
        border: 2px solid #7B68EE !important;
        color: white !important; /* Explicitly set white text */
    }}

    /* --- BUTTON 3: ChatGPT (STATIC Gray/Grey) --- */
    div[data-testid*="chatgpt_button"] button[data-testid="stButton-secondary"] {{
        background-color: #808080 !important; /* Gray */
        border: 2px solid #808080 !important;
        color: white !important; /* Explicitly set white text */
    }}

    {dynamic_toggle_style}
</style>
"""
st.markdown(full_css, unsafe_allow_html=True)


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
