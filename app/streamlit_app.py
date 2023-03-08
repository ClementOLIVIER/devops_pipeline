import streamlit as st
from runner_page import runner_page

st.set_page_config(
    page_title="Runner Page",
    page_icon="..."
)


def main():
    st.title('Runner Page')

    # Runner Page
    runner_page()


if __name__ == "__main__":
    main()
