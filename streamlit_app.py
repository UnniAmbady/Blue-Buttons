#Ver-11
import streamlit as st

st.set_page_config(page_title="4-Color Buttons Demo", layout="wide")
st.title("Four differently colored buttons (no theme changes)")

# --- Scoped CSS: only affects the first 4 columns in THIS row ---
st.markdown("""
<style>
/* Target the 4 buttons in the next horizontal block (the 4 columns below) */
div[data-testid="stHorizontalBlock"] > div:nth-of-type(1) button {
    background-color: #e74c3c;  /* red */
    color: #ffffff;
    border-color: #e74c3c;
}
div[data-testid="stHorizontalBlock"] > div:nth-of-type(2) button {
    background-color: #27ae60;  /* green */
    color: #ffffff;
    border-color: #27ae60;
}
div[data-testid="stHorizontalBlock"] > div:nth-of-type(3) button {
    background-color: #2980b9;  /* blue */
    color: #ffffff;
    border-color: #2980b9;
}
div[data-testid="stHorizontalBlock"] > div:nth-of-type(4) button {
    background-color: #f39c12;  /* orange */
    color: #000000;
    border-color: #f39c12;
}

/* Simple hover/active tweaks so it feels native */
div[data-testid="stHorizontalBlock"] > div button:hover { filter: brightness(0.95); }
div[data-testid="stHorizontalBlock"] > div button:active { transform: translateY(1px); }
</style>
""", unsafe_allow_html=True)

# --- 4 columns with 4 normal Streamlit buttons ---
c1, c2, c3, c4 = st.columns(4)

with c1:
    red_clicked = st.button("Red", key="btn_red")
with c2:
    green_clicked = st.button("Green", key="btn_green")
with c3:
    blue_clicked = st.button("Blue", key="btn_blue")
with c4:
    orange_clicked = st.button("Orange", key="btn_orange")

# --- Show which button was pressed (for testing) ---
clicked = []
if red_clicked: clicked.append("Red")
if green_clicked: clicked.append("Green")
if blue_clicked: clicked.append("Blue")
if orange_clicked: clicked.append("Orange")

if clicked:
    st.success("You clicked: " + ", ".join(clicked))
else:
    st.info("Click any button to test.")

st.caption("Note: This demo keeps the default theme palette unchanged and only styles these four buttons.")
