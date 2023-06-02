from twilio.rest import Client
import streamlit as st

@st.cache_data(allow_output_mutation=True)
def get_ice_servers(username: str, password: str):
    from twilio.base.exceptions import TwilioRestException
    try:
        client = Client(username, password)
        token = client.tokens.create()
        ice_servers = token.ice_servers
        return ice_servers
    except TwilioRestException as e:
        st.error(f"Twilio API call failed with error: {e}")
        return []

def get_twilio_client():
    username = st.secrets["TWILIO"]["TWILIO_ACCOUNT_SID"]
    password = st.secrets["TWILIO"]["TWILIO_AUTH_TOKEN"]
    return Client(username, password)

def get_twilio_token():
    client = get_twilio_client()
    token = client.tokens.create()
    return token

username = st.secrets["TWILIO"]["TWILIO_ACCOUNT_SID"]
password = st.secrets["TWILIO"]["TWILIO_AUTH_TOKEN"]

rtc_configuration = {"iceServers": get_ice_servers(username, password)}
