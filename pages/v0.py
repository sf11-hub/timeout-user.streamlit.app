import streamlit as st
import pathlib


st.markdown(f"<script> {pathlib.readtext('static/timeout.js')}</script>")