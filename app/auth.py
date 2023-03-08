import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader


def get_authenticator(auth_path):
    with open(auth_path) as auth_file:
        config = yaml.load(auth_file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    return authenticator
