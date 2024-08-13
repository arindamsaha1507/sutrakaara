import streamlit as st
import pandas as pd
import yaml

from utils import Prakriya, Krdartha
from prakriya_maker import CreatePrakriya


def stage_one(inputs, button, outputs):
    """Stage one of the app."""

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

    dhaatu = inputs.selectbox("धातु", dhaatus["नाम"])
    button = button.button("चिनुत", key="dhaatu_button")

    pp = st.session_state["pp"]

    if button:
        num = dhaatus.index[dhaatus["नाम"] == dhaatu][0]
        CreatePrakriya.add_dhaatu(pp, num)

        st.session_state["stage"] = 2
        st.session_state["dhaatu"] = dhaatu

    outputs.write(str(pp))


def stage_two(inputs, button, alt_button, outputs):
    """Stage two of the app."""

    pp = st.session_state["pp"]

    with open("गणपाठ.yml", "r", encoding="utf-8") as ff:
        upasargas = yaml.safe_load(ff)["प्रादि"]

    upasargas = upasargas.split(" ")

    upasarga = inputs.selectbox("उपसर्ग", upasargas)
    button = button.button("उपसर्गं योजय", key="add_upasarga")
    alt_button = alt_button.button("अग्रे गच्छ", key="upasarga_button")

    if button:
        CreatePrakriya.add_upasarga(pp, upasarga)
        st.session_state["upasarga"] += upasarga + " "

    if alt_button:
        st.session_state["stage"] = 3
        st.session_state["upasarga"] = st.session_state["upasarga"].strip()
        upp = st.session_state["upasarga"].split(" ")
        st.session_state["upasarga"] = " + ".join(upp)

    outputs.write(str(pp))


def stage_three(inputs, alt_inputs, button, outputs):
    """Stage three of the app."""

    pp = st.session_state["pp"]

    with open("प्रत्यय.yml", "r", encoding="utf-8") as ff:
        pratyayas = yaml.safe_load(ff)["कृत्"]

    arthas = list(Krdartha.__members__.keys())
    arthas = [Krdartha[i].value for i in arthas]

    pratyaya = inputs.selectbox("प्रत्यय", pratyayas)
    artha = alt_inputs.selectbox("अर्थः", arthas)
    button = button.button("प्रत्ययं योजय", key="add_pratyaya")

    if button:
        artha = Krdartha(artha)
        print(artha)
        print(pratyaya)
        CreatePrakriya.add_krt(pp, pratyaya, artha)
        st.session_state["stage"] = 4
        st.session_state["pratyaya"] = pratyaya

    outputs.write(str(pp))


def app():
    """Main app function."""

    if "stage" not in st.session_state:
        st.session_state["stage"] = 1
        st.session_state["pp"] = Prakriya()
        st.session_state["dhaatu"] = ""
        st.session_state["upasarga"] = ""
        st.session_state["pratyaya"] = ""

    st.title("प्रक्रिया विश्लेषक")

    st.write("अयं तन्त्रांशः व्याकरणप्रक्रियानिर्देशकः")

    inputs = st.empty()
    alt_inputs = st.empty()
    button = st.empty()
    alt_button = st.empty()
    outputs = st.empty()

    if st.session_state["stage"] == 1:
        stage_one(inputs, button, outputs)

    if st.session_state["stage"] == 2:
        stage_two(inputs, button, alt_button, outputs)

    if st.session_state["stage"] == 3:
        stage_three(inputs, alt_inputs, button, outputs)

    if st.session_state["stage"] == 4:
        st.session_state["pp"].combine()
        inputs.empty()
        alt_inputs.empty()
        button.empty()
        alt_button.empty()
        outputs.empty()

        st.write("## परिणाम")

        if st.session_state["upasarga"] == "":
            st.write(
                f"### {st.session_state['dhaatu']} + {st.session_state['pratyaya']} = {st.session_state['pp'].final}"
            )
        else:
            st.write(
                f"### {st.session_state['upasarga']} + {st.session_state['dhaatu']} + {st.session_state['pratyaya']} = {st.session_state['pp'].final}"
            )

        button = st.button("नवं प्रक्रियां प्रारम्भ", key="restart")
        if button:
            st.session_state["stage"] = 1
            st.session_state["pp"] = Prakriya()
            st.session_state["dhaatu"] = ""
            st.session_state["upasarga"] = ""
            st.session_state["pratyaya"] = ""

        save_button = st.button("प्रक्रियां संरक्ष", key="save")

        if save_button:
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


if __name__ == "__main__":
    app()
