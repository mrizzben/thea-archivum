import streamlit as st
import pytz
from src.dataloader.load import json_load

flavor_wheel = json_load('conf/flavour_wheel.json')

dry_leaf_appearance_attributes = json_load('conf/dry_appearance.json')

wet_leaf_appearance_attributes = json_load('conf/wet_appearance.json')

color = ['Pale Yellow / Green', 'Green', 'Yellow', 'Orange', 'Red', 'Brown']
clarity = ['Clear', 'Dark', 'Murky']
texture = ['Heavy', 'Metallic', 'Thick', 'Creamy', 'Full', 'Empty', 'Bright', 'Soft', 'Light', 'Mediums']
after_quality = ['Clean', 'Lingering', 'Empty']
country = list(pytz.country_names.values())
country.insert(0, 'N/A')
types = json_load('conf/tea_types.json')


def main():
    st.title('Tea Tasting Score Sheet')

    with st.container():
        col1, col2 = st.columns(2)
        taster_name = col1.text_input('Taster\'s Name')
        date = col2.date_input('Date')
        tea_name = col1.text_input('Tea Name')
        tea_type = col2.selectbox('Tea Type', types)

    with st.expander('Add Further Details'):
        region = st.selectbox('Country of Origin', country)

    with st.container():

        col1, col2 = st.columns(2)

        col1.header('Dry Leaf Evaluation')
        dry_leaf_appearance = col1.multiselect('Dry Appearance', dry_leaf_appearance_attributes)

        col2.header('Wet Leaf Evaluation')
        wet_leaf_appearance = col2.multiselect('Wet Appearance', wet_leaf_appearance_attributes)

    st.header('Liquor Evaluation')
    liquor_color = st.radio('Liqour Color', color, horizontal=True)
    liqour_clarity = st.radio('Liqour Clarity', clarity, horizontal=True)
    liquor_intensity = st.number_input('Aroma Intensity', 1, 5)
    st.caption('1 : Muted / Very Slight - 5 : Very Intense')
    liqour_body = st.multiselect('Body (Viscosity, Weight)', texture)
    st.caption('You may choose more than one attributes')

    st.subheader('Flavor Intensity')
    st.caption('0: None - 1 : Muted / Very Slight - 5 : Very Intense')
    with st.container():
        col1, col2, col3 = st.columns(3)
        sweetness = col1.number_input('Sweetness', min_value=0, max_value=5)
        bitterness = col2.number_input('Bitterness', min_value=0, max_value=5)
        astringency = col3.number_input('Astringency', min_value=0, max_value=5)
        floral = col1.number_input('Floral', min_value=0, max_value=5)
        fruity = col2.number_input('Fruity', min_value=0, max_value=5)
        earthy = col3.number_input('Earthy', min_value=0, max_value=5)
        herbal = col1.number_input('Herbal', min_value=0, max_value=5)
        spicy = col2.number_input('Spicy', min_value=0, max_value=5)
        vegetal = col3.number_input('Vegetal', min_value=0, max_value=5)
        nutty = col1.number_input('Nutty', min_value=0, max_value=5)
        woody = col2.number_input('Woody', min_value=0, max_value=5)
        umami = col3.number_input('Umami', min_value=0, max_value=5)

    selected_flavors = {}

    st.subheader('Flavour Attributes')
    st.caption('You may choose more than one attribute per flavour profile')

    num_columns = 2

    columns = st.columns(num_columns)
    for i, (attribute, options) in enumerate(flavor_wheel.items()):
        selected = columns[i % num_columns].multiselect(attribute, options, key=i)
        selected_flavors[attribute] = selected

    st.subheader('Selected Flavors')
    st.write(selected_flavors)

    st.subheader('Aftertaste')
    with st.container():
        col1, col2 = st.columns(2)
        aftertaste_duration = col1.number_input('Aftertaste Duration', 1, 5)
        col1.caption('1 : None / Very Short - 5: Lingering / Very Long')
        aftertaste_quality = col2.number_input('Aftertaste Quality', 1, 5)
        col2.caption('1 : Acceptable - 5 : Outstanding')

    st.subheader('Mouthfeel')
    st.caption('0: None - 1 : Muted / Very Slight - 5 : Very Intense')
    with st.container():
        col1, col2 = st.columns(2)
        smoothness = col1.number_input('Smoothness', 0, 5)
        thickness = col2.number_input('Thickness', 0, 5)
        creaminess = col1.number_input('Creaminess', 0, 5)
        dryness = col2.number_input('Dryness', 0, 5)

    st.header('Overall Evaluation')
    st.caption('1 : Acceptable - 2 : Good - 3 : Very Good - 4 : Excellent - 5 : Outstanding')
    with st.container():
        col1, col2, col3 = st.columns(3)
        appearance = col1.number_input('Appearance', 1, 5)
        col1.caption('Overall Appearance of the Tea')
        quality = col2.number_input('Quality', 1, 5)
        col2.caption('Quality of Flavors, Aromas, and Body')
        balance = col1.number_input('Balance', 1, 5)
        col1.caption('Balance of Flavors, Aromas, and Body')
        complexity = col2.number_input('Complexity', 1, 5)
        col2.caption('Nuance of Flavors, Aromas, and Body')
        cleanliness = col3.number_input('Cleanliness', 1, 5)
        col3.caption('Lack of Unpleasant Off-flavors')
        overall = col3.number_input('Overall', 1, 5)
        col3.caption('Overall Experience of the Tea')

    st.header('Additional Notes')
    additional_notes = st.text_area('Additional Notes', height=200)

    if st.button('Submit'):
        # Perform the necessary operations with the submitted data
        # You can save the data to a file or a database, send it via email, etc.
        # Add your desired logic here

        st.success('Submission Received')

if __name__ == '__main__':
    main()
