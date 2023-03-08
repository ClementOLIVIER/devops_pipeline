import streamlit as st
import time
from runner import function_runner

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
