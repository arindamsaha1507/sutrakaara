"""Kridanta page of the app."""

# pylint: disable=invalid-name, non-ascii-file-name

import streamlit as st
import pandas as pd
import yaml

from utils import Prakriya, Krdartha
from prakriya_maker import CreatePrakriya


def app():
    """Main app function."""

    if "pp" not in st.session_state:
        st.session_state["pp"] = Prakriya()
        st.session_state["dhaatu"] = ""
        st.session_state["upasarga"] = ""
        st.session_state["pratyaya"] = ""

    st.title("प्रक्रिया विश्लेषक")

    st.write("अयं तन्त्रांशः व्याकरणप्रक्रियानिर्देशकः")

    # Load dhaatus, upasargas, and pratyayas
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

    with open("गणपाठ.yml", "r", encoding="utf-8") as ff:
        upasargas = yaml.safe_load(ff)["प्रादि"].split(" ")

    with open("प्रत्यय.yml", "r", encoding="utf-8") as ff:
        pratyayas = yaml.safe_load(ff)["कृत्"]

    arthas = [Krdartha[i].value for i in Krdartha.__members__]

    # Display inputs
    dhaatu = st.selectbox("धातु", dhaatus["नाम"], key="dhaatu_select")
    # upasarga = st.selectbox("उपसर्ग", [""] + upasargas, key="upasarga_select")
    upasarga = st.multiselect("उपसर्ग", upasargas, key="upasarga_select")

    pratyaya = st.selectbox("प्रत्यय", pratyayas, key="pratyaya_select")
    artha = st.selectbox("अर्थः", arthas, key="artha_select")

    button = st.button("प्रक्रिया योजय", key="process_button")

    pp = st.session_state["pp"]

    if button:

        # Add dhaatu
        dhaatu_num = dhaatus.index[dhaatus["नाम"] == dhaatu][0]
        CreatePrakriya.add_dhaatu(pp, dhaatu_num)
        st.session_state["dhaatu"] = dhaatu

        # Add upasarga if selected
        if upasarga:
            for upasarga in upasarga:
                CreatePrakriya.add_upasarga(pp, upasarga)

                if len(st.session_state["upasarga"]) > 0:
                    st.session_state["upasarga"] += " + "
                st.session_state["upasarga"] += upasarga
        else:
            st.session_state["upasarga"] = ""

        # Add pratyaya
        artha_enum = Krdartha(artha)
        CreatePrakriya.add_krt(pp, pratyaya, artha_enum)
        st.session_state["pratyaya"] = pratyaya

        # Combine the prakriya steps and display the result
        pp.combine()
        st.session_state["pp"] = pp

        st.write("## परिणाम")

        string = f"{dhaatu} + {pratyaya} = {pp.final}"
        if st.session_state["upasarga"] == "":
            st.write(f"### {string}")
        else:
            st.write(f"### {st.session_state['upasarga']} + {string}")

        # Option to restart or save
        if st.button("नवं प्रक्रियां प्रारम्भ", key="restart"):
            st.session_state["pp"] = Prakriya()
            st.session_state["dhaatu"] = ""
            st.session_state["upasarga"] = ""
            st.session_state["pratyaya"] = ""

        if st.button("प्रक्रियां संरक्ष", key="save"):
            with open(
                f"prakriya/{st.session_state['pp'].final}.md", "a", encoding="utf-8"
            ) as ff:
                ff.write(
                    f"# {st.session_state['upasarga']} + {st.session_state['dhaatu']} + {st.session_state['pratyaya']}"
                )
                ff.write("\n")
                ff.write(str(st.session_state["pp"]))

        st.write("## प्रक्रिया")
        st.write(str(st.session_state["pp"]))
        st.session_state["pp"] = Prakriya()


app()
