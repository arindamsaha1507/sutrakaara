"""A simple Streamlit app demonstrating the use of the SanskritVerbNet API."""

import streamlit as st
import pandas as pd

from utils import Prakriya
from prakriya_maker import CreatePrakriya

st.title("प्रक्रिया विश्लेषक")

st.write("अयं तन्त्रांशः व्याकरणप्रक्रियानिर्देशकः")


dhaatus = pd.read_csv("धातु_1.csv")
dhaatus["नाम"] = (
    dhaatus["धातु"]
    + " "
    + "["
    + dhaatus["उपदेश"]
    + " "
    + dhaatus["अर्थ"]
    + " ("
    + dhaatus["गण"]
    + ")]"
)


dhaatu = st.selectbox("धातु", dhaatus["नाम"])
button = st.button("विश्लेषय")

if button:
    num = dhaatus.index[dhaatus["नाम"] == dhaatu][0]

    pp = Prakriya()
    CreatePrakriya.add_dhaatu(pp, num)
    prakriya = st.markdown(str(pp))
