import streamlit as st

flavor_wheel = {
    'Sweetness': ['Honey', 'Caramel', 'Sugar', 'Maple Syrup', 'Marshmallow', 'Agave'],
    'Bitterness': ['Dark Chocolate', 'Coffee', 'Gentian', 'Quinine', 'Grapefruit Peel', 'Black Walnut'],
    'Astringency': ['Pomegranate', 'Cranberry', 'Green Banana', 'Grape Skin', 'Black Tea', 'Walnut Skin'],
    'Floral': ['Jasmine', 'Rose', 'Lavender', 'Chamomile', 'Osmanthus', 'Honeysuckle'],
    'Fruity': ['Citrus', 'Berry', 'Stone Fruit', 'Tropical Fruit', 'Apple', 'Mango'],
    'Earthy': ['Mushroom', 'Forest Floor', 'Damp Earth', 'Wet Leaves', 'Roasted Beet', 'Oak Moss'],
    'Herbal': ['Mint', 'Basil', 'Thyme', 'Eucalyptus', 'Sage', 'Lemongrass'],
    'Spicy': ['Cinnamon', 'Ginger', 'Cloves', 'Peppercorn', 'Cardamom', 'Nutmeg'],
    'Vegetal': ['Grass', 'Seaweed', 'Artichoke', 'Fresh Herbs', 'Green Bell Pepper', 'Snow Pea'],
    'Nutty': ['Almond', 'Peanut', 'Hazelnut', 'Cashew', 'Pistachio', 'Walnut'],
    'Woody': ['Cedar', 'Oak', 'Pine', 'Sandalwood', 'Cypress', 'Mahogany'],
    'Other': ['Biscuit', 'Molasses', 'Tobacco', 'Leather', 'Burnt Sugar', 'Toasted Sesame']
}

color = ['Pale/White', 'Light Green', 'Yellow', 'Orange', 'Brown', 'Dark Red']
clarity = ['Clear', 'Dark', 'Murky']
texture = ['Heavy', 'Metallic', 'Thick', 'Creamy', 'Full', 'Empty', 'Bright', 'Soft', 'Light']


def main():
    st.title('Tea Tasting Score Sheet')

    taster_name = st.text_input('Taster\'s Name')
    date = st.date_input('Date')
    tea_name = st.text_input('Tea Name')

    with st.container():

        col1, col2 = st.columns(2)

        col1.header('Dry Leaf Evaluation')
        dry_leaf_appearance = col1.text_input('Dry Appearance')
        dry_leaf_aroma = col1.text_input('Dry Aroma')

        col2.header('Wet Leaf Evaluation')
        wet_leaf_appearance = col2.text_input('Wet Appearance')
        wet_leaf_aroma = col2.text_input('Wet Aroma')

    st.header('Liquor Evaluation')
    liquor_color = st.select_slider('Liqour Color', color)
    liqour_clarity = st.radio('Liqour Clarity', clarity)
    liquor_intensity = st.slider('Aroma Intensity', 1, 5)
    liqour_body = st.multiselect('Body (Viscosity, Weight)', texture)

    st.header('Flavor Intensity')
    with st.container():
        col1, col2, col3 = st.columns(3)
        sweetness = col1.number_input('Sweetness', min_value=1, max_value=10)
        bitterness = col2.number_input('Bitterness', min_value=1, max_value=10)
        astringency = col3.number_input('Astringency', min_value=1, max_value=10)
        floral = col1.number_input('Floral', min_value=1, max_value=10)
        fruity = col2.number_input('Fruity', min_value=1, max_value=10)
        earthy = col3.number_input('Earthy', min_value=1, max_value=10)
        herbal = col1.number_input('Herbal', min_value=1, max_value=10)
        spicy = col2.number_input('Spicy', min_value=1, max_value=10)
        vegetal = col3.number_input('Vegetal', min_value=1, max_value=10)
        nutty = col1.number_input('Nutty', min_value=1, max_value=10)
        woody = col2.number_input('Woody', min_value=1, max_value=10)

    selected_flavors = {}

    st.header('Flavour Attributes')

    for attribute, options in flavor_wheel.items():
        selected = st.multiselect(attribute, options)
        selected_flavors[attribute] = selected

    st.header('Selected Flavors')
    st.write(selected_flavors)

    st.header('Aftertaste')
    aftertaste_duration = st.text_input('Duration')
    aftertaste_quality = st.text_input('Quality')

    st.header('Mouthfeel')
    smoothness = st.text_input('Smoothness')
    thickness = st.text_input('Thickness')
    creaminess = st.text_input('Creaminess')
    dryness = st.text_input('Dryness')

    st.header('Overall Evaluation')
    balance = st.text_input('Balance (Flavors, Aromas, and Body)')
    complexity = st.text_input('Complexity')
    cleanliness = st.text_input('Cleanliness (Lack of Off-flavors)')
    preference = st.text_input('Personal Preference')

    st.header('Additional Notes')
    additional_notes = st.text_area('Additional Notes', height=200)

    if st.button('Submit'):
        # Perform the necessary operations with the submitted data
        # You can save the data to a file or a database, send it via email, etc.
        # Add your desired logic here

        st.success('Submission Received')

if __name__ == '__main__':
    main()
