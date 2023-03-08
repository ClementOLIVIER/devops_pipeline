import os
import streamlit as st
from runner_page import runner_page
from auth import get_authenticator

st.set_page_config(
    page_title="Runner Page",
    page_icon="🚀"
)

file_directory = os.path.dirname(os.path.realpath(__file__))
config_directory = os.path.join(file_directory, '../config')


def main(auth_path):
    st.title('Runner Page')

    # Login Page
    authenticator = get_authenticator(auth_path)
    name, authentication_status, username = authenticator.login('Login', 'main')

    # Runner Page
    if authentication_status is None:
        st.warning("Enter your username and password")
        st.info("Username: clementolivier | Password: SuchAS€cureP@ssw°rd")
    elif authentication_status:
        st.write(f'Hello, your are logged in as *{name}*')
        authenticator.logout('Logout', 'main')
        st.markdown("""---""")
        runner_page()
    else:
        st.error("Username and/or password incorrect")
        st.info("Username: clementolivier | Password: SuchAS€cureP@ssw°rd")


if __name__ == "__main__":
    auth_filename = 'auth.yaml'
    auth_path = os.path.join(config_directory, auth_filename)
    main(auth_path)
