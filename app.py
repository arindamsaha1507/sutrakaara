"""Main app file for the streamlit app."""

import streamlit as st
from prakriya_maker import Prakriya


def app():
    """Main app function."""

    if "stage" not in st.session_state:
        st.session_state["stage"] = 1
        st.session_state["pp"] = Prakriya()
        st.session_state["dhaatu"] = ""
        st.session_state["upasarga"] = ""
        st.session_state["pratyaya"] = ""

    st.write("# धातु-प्रत्यय-संज्ञा-प्रक्रिया")

if __name__ == "__main__":
    app()
