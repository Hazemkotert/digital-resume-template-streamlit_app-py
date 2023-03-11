from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config (page_title="My webpage",page_icon=":cyclone:", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True )

local_css("style.css")


lottie_coding= load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_4kx2q32n.json")

img=Image.open("smooking.png" )

st.subheader("Hi My name is Hazem :wave:")
st.title("Student in Mohamed ragab miami")
st.write("Learninig python ")
st.write("13 Years old")
st.write("From Egypt")
st.write("Video editor and graphic designer")
st.write("[learn more>>](https://www.facebook.com/profile.php?id=100041010124627&viewas=&show_switched_toast=false&show_switched_tooltip=false&is_tour_dismissed=false&is_tour_completed=false&show_podcast_settings=false&show_community_review_changes=false&should_open_composer=false&badge_type=NEW_MEMBER&show_community_rollback_toast=false&show_community_rollback=false&show_follower_visibility_disclosure=false&bypass_exit_warning=true)")
 
   

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do")
    st.write("###")
    st.write("Beginner programmer")
    ("Video editor")
    st.write("Canva Graphic Designer")

    st.write("[My instagram >>](https://www.instagram.com/hazem_foden123/)")
with right_column:
    st_lottie(lottie_coding, height=350, key=lottie_coding)
    

st.write("---")
st.header("My projects")
st.write("##")
image_column, text_column=st.columns((1,2)) 

with image_column:
    st.image(img)
    

with text_column:
    st.subheader("No smoking ")
    st.write("This video is talking about smoking with interviews and some fun information")
    st.markdown("[WATCH IT NOW!!!](https://www.facebook.com/100006118839325/videos/952397199104354/)")

st.write("---")
st.header("Talk with me")
st.write("##")
contact_form = """
<form action="https://formsubmit.co/youtubwatcher12345@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="flase">
     <input type="text" name=" your name" placeholder= Name required>
     <input type="email" name=" your email" placeholder=email required>
     <textarea name="message" placeholder= message required></textarea>
     <button type="submit">Send</button>
</form>
   """
left_column, right_column = st.columns(2)        
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()    
