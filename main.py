import streamlit as st
import plotly.express as px
from itertools import chain
import pandas as pd
from datetime import date

from src.config import *
from src.ui.scoresheet import (
    basic_details,
    flavour_attributes,
    final_details,
    flavour_intensity_sliders,
    physical_details,
)
from src.visualise.mainsheet import flavour_intensity_chart

if "submission" not in st.session_state:
    st.session_state.submission = {}


def main():
    st.title("Tea Tasting Score Sheet")
    form_results = []
    basic_dict, tea_name, taster_name = basic_details()
    form_results.append(basic_dict)
    physical_dict = physical_details()
    form_results.append(physical_dict)
    flavour_intensity_dict = flavour_intensity_sliders()
    form_results.append(flavour_intensity_dict)
    st.write("---")
    flavour_intensity_chart(flavour_intensity_dict)
    flavour_attributes_dict = flavour_attributes()
    form_results.append(flavour_attributes_dict)
    final_details_dict = final_details()
    form_results.append(final_details_dict)

    if tea_name and taster_name:
        if st.button("Submit"):
            submission_name = tea_name + "_" + taster_name
            st.session_state.submission[submission_name] = {}
            new_results = {}
            for res in form_results:
                new_results.update(res)
            dataframe = pd.DataFrame([new_results])
            submission_dict = st.session_state.submission[submission_name]
            submission_dict["scoresheet"] = dataframe
            submission_dict["flavourwhl"] = flavour_intensity_dict
            dataframe.to_csv("results.csv", index=False, mode="a", header=False)

            st.success("Submission Received")
            st.download_button(
                "Download Results",
                data=dataframe.to_csv(index=False),
                file_name=f"{taster_name}_results_{tea_name}_{date.today()}.csv",
            )

    else:
        st.error(
            "Tea Name and Taster Name have not been entered, you will not be able to save your score."
        )


if __name__ == "__main__":
    main()
