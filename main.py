import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import av

from sample_utils.turn import get_ice_servers

username = st.secrets["TWILIO"]["TWILIO_ACCOUNT_SID"]
password = st.secrets["TWILIO"]["TWILIO_AUTH_TOKEN"]

st.title('Example')


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    ##flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(format="bgr24")


webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={"iceServers": get_ice_servers(username, password)},
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,

)
