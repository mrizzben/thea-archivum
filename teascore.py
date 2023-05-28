import streamlit as st

flavor_attributes = {
    'Sweetness': ['Honey', 'Sugar', 'Caramel', 'Maple Syrup'],
    'Bitterness': ['Dark Chocolate', 'Coffee', 'Grapefruit Peel', 'Black Walnut'],
    'Astringency': ['Green Apple', 'Black Tea', 'Cranberry', 'Unripe Persimmon'],
    'Floral': ['Rose', 'Jasmine', 'Lavender', 'Honeysuckle'],
    'Fruity': ['Berry', 'Citrus', 'Tropical', 'Stone Fruit'],
    'Earthy': ['Mushroom', 'Forest Floor', 'Damp Earth', 'Wet Leaves'],
    'Herbal': ['Mint', 'Basil', 'Thyme', 'Eucalyptus'],
    'Spicy': ['Cinnamon', 'Ginger', 'Cloves', 'Peppercorn'],
    'Vegetal': ['Grass', 'Seaweed', 'Artichoke', 'Fresh Herbs'],
    'Nutty': ['Almond', 'Peanut', 'Hazelnut', 'Cashew'],
    'Woody': ['Cedar', 'Oak', 'Pine', 'Sandalwood'],
    'Other': ['Biscuit', 'Molasses', 'Tobacco', 'Leather']
}

def main():
    st.title('Tea Tasting Score Sheet')

    taster_name = st.text_input('Taster\'s Name')
    date = st.date_input('Date')
    tea_name = st.text_input('Tea Name')

    st.header('Dry Leaf Evaluation')
    dry_leaf_appearance = st.text_input('Dry Appearance')
    dry_leaf_aroma = st.text_input('Dry Aroma')

    st.header('Wet Leaf Evaluation')
    wet_leaf_appearance = st.text_input('Wet Appearance')
    wet_leaf_aroma = st.text_input('Wet Aroma')

    st.header('Liquor Evaluation')
    liquor_appearance = st.text_input('Appearance (Color, Clarity)')
    liquor_aroma = st.text_input('Aroma (Intensity, Quality)')
    body = st.text_input('Body (Viscosity, Weight)')
    overall_flavor = st.text_input('Flavor (Overall)')

    st.header('Flavor Intensity')
    sweetness = st.number_input('Sweetness', min_value=1, max_value=10)
    bitterness = st.number_input('Bitterness', min_value=1, max_value=10)
    astringency = st.number_input('Astringency', min_value=1, max_value=10)
    floral = st.number_input('Floral', min_value=1, max_value=10)
    fruity = st.number_input('Fruity', min_value=1, max_value=10)
    earthy = st.number_input('Earthy', min_value=1, max_value=10)
    herbal = st.number_input('Herbal', min_value=1, max_value=10)
    spicy = st.number_input('Spicy', min_value=1, max_value=10)
    vegetal = st.number_input('Vegetal', min_value=1, max_value=10)
    nutty = st.number_input('Nutty', min_value=1, max_value=10)
    woody = st.number_input('Woody', min_value=1, max_value=10)

    selected_flavors = {}

    st.title('Flavour Attributes')

    for attribute, options in flavor_attributes.items():
        selected = st.multiselect(attribute, options)
        selected_flavors[attribute] = selected

    st.title('Selected Flavors')
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
