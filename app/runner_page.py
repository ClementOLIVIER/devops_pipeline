import streamlit as st
import time
from runner import function_runner
import random

mapping = {
    'Dog': '🐶',
    'Fish': '🐟',
    'Cat': '🐱',
    'Banana': '🍌',
    'Salad': '🥗',
    'Pizza': '🍕'
}


def feed_animal(animal, food):
    print(f"Feeding {animal} with {food}")
    time.sleep(0.5)
    print(f'The animal is {animal} {mapping[animal]} is eating a {food} {mapping[food]} !')
    time.sleep(2)
    print("Finished eating")


def runner_page():

    import streamlit as st

    tab1, tab2 = st.tabs(["Feed an animal", "Roll a dice"])

    with tab1:
        feed_animal_page()

    with tab2:
        roll_a_dice_page()

dice_mapping = {
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}


def roll_a_dice_page():
    st.header('Roll a dice')

    run_function_button = st.button('Roll the dice')

    if run_function_button:
        dice_value = random.randint(1, 6)
        new_title = f'<p style="font-family:sans-serif; font-size: 100px;">{dice_mapping[dice_value]}</p>'
        st.markdown(new_title, unsafe_allow_html=True)


def feed_animal_page():
    st.header('Feed an animal')

    animal = st.selectbox(
        '**Option Animal**',
        ('Cat', 'Dog', 'Fish'))

    food = st.radio(
        '**Option Food**',
        ('Banana', 'Salad', 'Pizza'))

    st.write('Running the `feed_animal` with option')
    st.markdown(f'**Animal**: {animal} {mapping[animal]}')
    st.markdown(f'**Food**: {food} {mapping[food]}')

    run_function_button = st.button('Run the function')

    if run_function_button:
        function_runner(feed_animal, animal, food)
