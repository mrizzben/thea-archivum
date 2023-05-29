import streamlit as st
import plotly.express as px
import pytz
from src.dataloader.load import json_load

FLAVOR_WHEEL = json_load('conf/flavour_wheel.json')
DRY_LEAF_ATTRS = json_load('conf/dry_appearance.json')
WET_LEAF_ATTRS = json_load('conf/wet_appearance.json')
TEXTURE = json_load('conf/texture.json')
TYPES = json_load('conf/tea_types.json')
COUNTRY = list(pytz.country_names.values())
COUNTRY.insert(0, 'N/A')
COLOR = ['Pale Yellow / Green', 'Green', 'Yellow', 'Orange', 'Red', 'Brown']
CLARITY = ['Clear', 'Dark', 'Murky']
PEKOE_GRADES = json_load('conf/pekoe_grades.json')


def main():
    st.title('Tea Tasting Score Sheet')

    with st.container():
        col1, col2 = st.columns(2)
        taster_name = col1.text_input('Taster\'s Name')
        date = col2.date_input('Date')
        tea_name = col1.text_input('Tea Name')
        tea_type = col2.selectbox('Tea Type', TYPES)
        if tea_type == 'Black Tea':
            grade = st.selectbox('Pekoe Grades', PEKOE_GRADES, index=0)
        else:
            grade = 'N/A'


    with st.expander('Add Further Details'):
        region = st.selectbox('Country of Origin', COUNTRY)
        area = st.text_input('Region / Area')
        processor = st.text_input('Processor')
        plantation = st.text_input('Plantation')
        distributor = st.text_input('Distributor')
        

    with st.container():

        col1, col2 = st.columns(2)

        col1.header('Dry Leaf Evaluation')
        dry_leaf_appearance = col1.multiselect(
            'Dry Appearance',
            DRY_LEAF_ATTRS
        )

        col2.header('Wet Leaf Evaluation')
        wet_leaf_appearance = col2.multiselect(
            'Wet Appearance',
            WET_LEAF_ATTRS
        )

    st.header('Liquor Evaluation')
    liquor_color = st.radio('Liqour Color', COLOR, horizontal=True)
    liqour_clarity = st.radio('Liqour Clarity', CLARITY, horizontal=True)
    liquor_intensity = st.number_input('Aroma Intensity', 1, 5)
    st.caption('0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense')
    liqour_body = st.multiselect('Body (Viscosity, Weight)', TEXTURE)
    st.caption('You may choose more than one attributes')

    st.subheader('Flavor Intensity')
    st.caption('0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense')
    flavour_intensity_dict = dict()
    with st.container():
        col1, col2, col3 = st.columns(3)
        flavour_intensity_dict['sweetness'] = col1.number_input('Sweetness', min_value=0, max_value=5)
        flavour_intensity_dict['bitterness'] = col2.number_input('Bitterness', min_value=0, max_value=5)
        flavour_intensity_dict['astringency'] = col3.number_input('Astringency', min_value=0, max_value=5)
        flavour_intensity_dict['floral'] = col1.number_input('Floral', min_value=0, max_value=5)
        flavour_intensity_dict['fruity'] = col2.number_input('Fruity', min_value=0, max_value=5)
        flavour_intensity_dict['earthy'] = col3.number_input('Earthy', min_value=0, max_value=5)
        flavour_intensity_dict['herbal'] = col1.number_input('Herbal', min_value=0, max_value=5)
        flavour_intensity_dict['spicy'] = col2.number_input('Spicy', min_value=0, max_value=5)
        flavour_intensity_dict['vegetal'] = col3.number_input('Vegetal', min_value=0, max_value=5)
        flavour_intensity_dict['nutty'] = col1.number_input('Nutty', min_value=0, max_value=5)
        flavour_intensity_dict['woody'] = col2.number_input('Woody', min_value=0, max_value=5)
        flavour_intensity_dict['umami'] = col3.number_input('Umami', min_value=0, max_value=5)
    st.write("---")

    with st.expander('Flavour Chart'):
        fig = px.line_polar(
            r=flavour_intensity_dict.values(), 
            theta=flavour_intensity_dict.keys(), 
            line_close=True
        )
        fig.update_traces(fill='toself')
        st.plotly_chart(fig)

    selected_flavors = {}

    st.subheader('Flavour Attributes')
    st.caption('You may choose more than one attribute per flavour profile')

    num_columns = 2

    columns = st.columns(num_columns)
    for i, (attribute, options) in enumerate(FLAVOR_WHEEL.items()):
        selected = columns[i % num_columns].multiselect(attribute, options, key=i)
        selected_flavors[attribute] = selected
    
    if any(selected_flavors.values()):
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
    st.caption('0 : None - 1 : Muted - 2 : Slight - 3 : Mild - 4 : Intense - 5 : Very Intense')
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
