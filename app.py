import streamlit as st
import time
from threading import Timer

# Function to reset the timer on user activity
def reset_timer():
    global timer
    timer.cancel()
    timer = Timer(timeout_seconds, timeout_callback)
    timer.start()

# Function to handle user inactivity timeout
def timeout_callback():
    st.session_state.is_timed_out = True
    st.experimental_rerun()

# Set timeout duration in seconds
timeout_seconds = st.sidebar.slider("Set Timeout (seconds)", 10, 300, 60)

# Initialize timer
timer = Timer(timeout_seconds, timeout_callback)
timer.start()

# Check if the session is timed out
if hasattr(st.session_state, "is_timed_out") and st.session_state.is_timed_out:
    st.warning("Session timed out due to inactivity. Refresh the page to start a new session.")
else:
    # Listen for user activity and reset the timer
    st.session_state.is_timed_out = False
    st.set_page_config(page_title="Inactivity Timeout", page_icon="⏰")

    st.write("# Streamlit App with Timeout")

    # Add your app content here
    st.write("This is your Streamlit app content.")

    # Reset the timer on user activity
    st.text("Interact with the app to reset the timer.")
    reset_timer()
