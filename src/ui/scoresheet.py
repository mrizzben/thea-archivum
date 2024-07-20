import streamlit as st
from src.config import *
from typing import Dict


def basic_details() -> Dict:
    with st.container():
        session = st.text_input("Tasting Session Code (optional)")
        col1, col2 = st.columns(2)
        taster_name = col1.text_input("Taster's Name")
        date = col2.date_input("Date")
        date = date.strftime("%m/%d/%Y")
        tea_name = col1.text_input("Tea Name")
        tea_type = col2.selectbox("Tea Type", TYPES)
        brew_temp = col1.number_input("Brewing Temp", 50, 100)
        if tea_type == "Black Tea":
            grade = st.selectbox("Pekoe Grades", PEKOE_GRADES, index=0)
        else:
            grade = "N/A"

    with st.expander("Add Further Details"):
        region = st.selectbox("Country of Origin", COUNTRY)
        area = st.text_input("Region / Area")
        processor = st.text_input("Processor")
        plantation = st.text_input("Plantation")
        distributor = st.text_input("Distributor")

    basic_details_dict = {
        "Session ID": session,
        "Taster Name": taster_name,
        "Date": date,
        "Tea Name": tea_name,
        "Tea Type": tea_type,
        "Pekoe Grade": grade,
        "Brew Temp": brew_temp,
        "Region": region,
        "Area": area,
        "Processor": processor,
        "Plantation": plantation,
        "Distributor": distributor,
    }
    return basic_details_dict, tea_name, taster_name


def flavour_intensity_sliders() -> Dict:
    flavour_intensity_dict = {}
    st.subheader("Flavor Intensity")
    st.caption(
        "0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense"
    )
    with st.container():
        col1, col2, col3 = st.columns(3)
        flavour_intensity_dict["sweetness"] = col1.number_input(
            "Sweetness", min_value=0, max_value=5
        )
        flavour_intensity_dict["bitterness"] = col2.number_input(
            "Bitterness", min_value=0, max_value=5
        )
        flavour_intensity_dict["astringency"] = col3.number_input(
            "Astringency", min_value=0, max_value=5
        )
        flavour_intensity_dict["floral"] = col1.number_input(
            "Floral", min_value=0, max_value=5
        )
        flavour_intensity_dict["fruity"] = col2.number_input(
            "Fruity", min_value=0, max_value=5
        )
        flavour_intensity_dict["earthy"] = col3.number_input(
            "Earthy", min_value=0, max_value=5
        )
        flavour_intensity_dict["herbal"] = col1.number_input(
            "Herbal", min_value=0, max_value=5
        )
        flavour_intensity_dict["spicy"] = col2.number_input(
            "Spicy", min_value=0, max_value=5
        )
        flavour_intensity_dict["vegetal"] = col3.number_input(
            "Vegetal", min_value=0, max_value=5
        )
        flavour_intensity_dict["nutty"] = col1.number_input(
            "Nutty", min_value=0, max_value=5
        )
        flavour_intensity_dict["woody"] = col2.number_input(
            "Woody", min_value=0, max_value=5
        )
        flavour_intensity_dict["umami"] = col3.number_input(
            "Umami", min_value=0, max_value=5
        )
    flavour_intensity_dict = {k.title(): v for k, v in flavour_intensity_dict.items()}
    return flavour_intensity_dict


def physical_details():
    with st.container():
        col1, col2 = st.columns(2)

        col1.header("Dry Leaf Evaluation")
        dry_leaf_appearance = col1.multiselect("Dry Appearance", DRY_LEAF_ATTRS)

        col2.header("Wet Leaf Evaluation")
        wet_leaf_appearance = col2.multiselect("Wet Appearance", WET_LEAF_ATTRS)

    st.header("Liquor Evaluation")
    liquor_color = st.radio("Liqour Color", COLOR, horizontal=True)
    liqour_clarity = st.radio("Liqour Clarity", CLARITY, horizontal=True)
    liquor_intensity = st.number_input("Aroma Intensity", 1, 5)
    st.caption(
        "0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense"
    )
    liqour_body = st.multiselect("Body (Viscosity, Weight)", TEXTURE)
    st.caption("You may choose more than one attributes")
    physical_details_dict = {
        "Dry Leaf Appearance": dry_leaf_appearance,
        "Wet Leaf Appearance": wet_leaf_appearance,
        "Liquor Color": liquor_color,
        "Liquor Clarity": liqour_clarity,
        "Aroma Intensity": liquor_intensity,
        "Liquor Body": liqour_body,
    }
    return physical_details_dict


def flavour_attributes() -> Dict:
    selected_flavours = {}

    st.subheader("Flavour Attributes")
    st.caption("You may choose more than one attribute per flavour profile")

    num_columns = 2

    columns = st.columns(num_columns)
    for i, (attribute, options) in enumerate(FLAVOR_WHEEL.items()):
        selected = columns[i % num_columns].multiselect(attribute, options, key=i)
        key = str(attribute).title() + " Attributes"
        selected_flavours[key] = selected

    if any(selected_flavours.values()):
        st.subheader("Selected Flavours")
        st.write(selected_flavours)
    return selected_flavours


def texture_attributes():
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
    texture_attributes_dict = {
        "Aftertaste Duration": aftertaste_duration,
        "Aftertaste Quality": aftertaste_quality,
        "Smoothness": smoothness,
        "Thickness": thickness,
        "Creaminess": creaminess,
        "Dryness": dryness,
    }
    return texture_attributes_dict


def final_details():
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
    final_details_dict = {
        "Appearance": appearance,
        "Quality": quality,
        "Balance": balance,
        "Complexity": complexity,
        "Cleanliness": cleanliness,
        "Overall": overall,
        "Additional Notes": additional_notes,
    }
    return final_details_dict
