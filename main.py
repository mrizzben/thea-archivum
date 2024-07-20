import streamlit as st
import plotly.express as px
from itertools import chain
import pandas as pd

from src.config import *
from src.ui.scoresheet import *
from src.visualise.mainsheet import *

if "submission" not in st.session_state:
    st.session_state.submission = {}


def main():
    st.title("Tea Tasting Score Sheet")
    form_results = []
    basic_dict = basic_details()
    form_results.append(basic_dict)
    physical_dict = physical_details()
    form_results.append(physical_dict)
    flavour_intensity_dict = flavour_intensity_sliders()
    form_results.append(flavour_intensity_dict)
    st.write("---")
    flavour_intensity_chart(flavour_intensity_dict)
    selected_flavours = {}

    st.subheader("Flavour Attributes")
    st.caption("You may choose more than one attribute per flavour profile")

    num_columns = 2

    columns = st.columns(num_columns)
    for i, (attribute, options) in enumerate(FLAVOR_WHEEL.items()):
        selected = columns[i % num_columns].multiselect(attribute, options, key=i)
        key = str(attribute).lower()
        selected_flavours[key] = selected

    if any(selected_flavours.values()):
        st.subheader("Selected Flavours")
        st.write(selected_flavours)

    st.subheader("Aftertaste")
    with st.container():
        col1, col2 = st.columns(2)
        aftertaste_duration = col1.number_input("Aftertaste Duration", 1, 5)
        col1.caption("1 : None / Very Short - 5: Lingering / Very Long")
        aftertaste_quality = col2.number_input("Aftertaste Quality", 1, 5)
        col2.caption("1 : Acceptable - 5 : Outstanding")

    st.subheader("Mouthfeel")
    st.caption(
        "0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense"
    )
    with st.container():
        col1, col2 = st.columns(2)
        smoothness = col1.number_input("Smoothness", 0, 5)
        thickness = col2.number_input("Thickness", 0, 5)
        creaminess = col1.number_input("Creaminess", 0, 5)
        dryness = col2.number_input("Dryness", 0, 5)

    st.header("Overall Evaluation")
    st.caption(
        "1 : Acceptable - 2 : Good - 3 : Very Good - 4 : Excellent - 5 : Outstanding"
    )
    with st.container():
        col1, col2, col3 = st.columns(3)
        appearance = col1.number_input("Appearance", 1, 5)
        col1.caption("Overall Appearance of the Tea")
        quality = col2.number_input("Quality", 1, 5)
        col2.caption("Quality of Flavours, Aromas, and Body")
        balance = col1.number_input("Balance", 1, 5)
        col1.caption("Balance of Flavours, Aromas, and Body")
        complexity = col2.number_input("Complexity", 1, 5)
        col2.caption("Nuance of Flavours, Aromas, and Body")
        cleanliness = col3.number_input("Cleanliness", 1, 5)
        col3.caption("Lack of Unpleasant Off-flavours")
        overall = col3.number_input("Overall", 1, 5)
        col3.caption("Overall Experience of the Tea")

    st.header("Additional Notes")
    additional_notes = st.text_area("Additional Notes", height=200)

    if tea_name and taster_name:
        if st.button("Submit"):
            submission_name = tea_name + "_" + taster_name
            st.session_state.submission[submission_name] = {}
            # Append the submitted data to the DataFrame
            new_row = {
                "Sweetness": flavour_intensity_dict["sweetness"],
                "Sweetness Attr": selected_flavours["sweetness"],
                "Bitterness": flavour_intensity_dict["bitterness"],
                "Bitterness Attr": selected_flavours["bitterness"],
                "Astringency": flavour_intensity_dict["astringency"],
                "Astringency Attr": selected_flavours["astringency"],
                "Floral": flavour_intensity_dict["floral"],
                "Floral Attr": selected_flavours["floral"],
                "Fruity": flavour_intensity_dict["fruity"],
                "Fruity Attr": selected_flavours["fruity"],
                "Earthy": flavour_intensity_dict["earthy"],
                "Earthy Attr": selected_flavours["earthy"],
                "Herbal": flavour_intensity_dict["herbal"],
                "Herbal Attr": selected_flavours["herbal"],
                "Spicy": flavour_intensity_dict["spicy"],
                "Spicy Attr": selected_flavours["spicy"],
                "Vegetal": flavour_intensity_dict["vegetal"],
                "Vegetal Attr": selected_flavours["vegetal"],
                "Nutty": flavour_intensity_dict["nutty"],
                "Nutty Attr": selected_flavours["nutty"],
                "Woody": flavour_intensity_dict["woody"],
                "Woody Attr": selected_flavours["woody"],
                "Umami": flavour_intensity_dict["umami"],
                "Umami Attr": selected_flavours["umami"],
                "Other Attr": selected_flavours["browning"],
                "Aftertaste Duration": aftertaste_duration,
                "Aftertaste Quality": aftertaste_quality,
                "Smoothness": smoothness,
                "Thickness": thickness,
                "Creaminess": creaminess,
                "Dryness": dryness,
                "Appearance": appearance,
                "Quality": quality,
                "Balance": balance,
                "Complexity": complexity,
                "Cleanliness": cleanliness,
                "Overall": overall,
                "Additional Notes": additional_notes,
            }
            # results_df = results_df.append(new_row, ignore_index=True)
            # with open('results.json', 'w') as output:
            #     json.dump(new_row, output)
            dataframe = pd.DataFrame([new_row])
            submission_dict = st.session_state.submission[submission_name]
            submission_dict["scoresheet"] = dataframe
            submission_dict["flavourwhl"] = flavour_intensity_dict
            dataframe.to_csv("results.csv", index=False, mode="a", header=False)

            st.success("Submission Received")
            st.download_button(
                "Download Results",
                data=dataframe.to_csv(index=False),
                file_name=f"{taster_name}_results_{tea_name}_{date}.csv",
            )

    else:
        st.error(
            "Tea Name and Taster Name have not been entered, you will not be able to save your score."
        )


if __name__ == "__main__":
    main()
