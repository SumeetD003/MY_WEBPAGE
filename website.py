import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/7ba28213-137d-466c-90fb-728e13e8c152/F4ELaxn0RW.json")
img_contact_form = Image.open("1662353833082.jpeg")
img_lottie_animation = Image.open("Gym Logo Silhouette PNG Images, Gym Logo, Muscle Clipart, Fitness, Gym PNG Image For Free Download.jpeg")
img_lottie_my_pic = Image.open("profile-pic copy.png")
lottie_animation1 = ("https://lottie.host/50570123-d8c7-4d2c-a497-26defdcd8cb2/kuKQq7Ofv5.json")
st_lottie(lottie_animation1 , height=250)

# ---- HEADER SECTION ----
with st.container():
    col1, col2 = st.columns([5, 1])
    with col1:
        st.title("Hi, I am Sumeet Deshpande :wave:")
        st.subheader("A student from Vellore Institute of Technology, Bhopal")
        st.write("I am passionate about finding ways to use Python and an Enthusiast of MACHINE LEARNING AND ARTIFICIAL INTELLIGENCE. . As part of my academic journey, I have immersed myself in the world of data science, focusing on constructing powerful machine learning models. Leveraging my skills and knowledge, I've developed predictive models, delved into various algorithms, and utilized datasets to derive valuable insights.")
        st.write("[LinkedIn Profile >](https://www.linkedin.com/in/sumeet-deshpande-b33840227/)")

    with col2:
        st.image(img_lottie_my_pic, width=250)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ?")
        st.write("##")
        st.write(
            """
           **I'm a Full Stack Developer** who is passionate about learning and developing new technologies. My expertise lies in building ML
           models and using various libraries and combining it with other tech like Computer Vision.  My expertise lies in utilizing machine learning techniques to solve real-world problems,
           and I am enthusiastic about contributing my skills to create innovative solutions in this ever-evolving field.
            
            """
        )
        st.write("[GitHub Profile >](https://github.com/SumeetD003)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("GYM_ML:- An app which will help the user to fix posture during the workout sessions")
        st.write(
            """
            This project is developed using Flask and ML model for predicting whether a person has good or bad posture while doing workout. The model
            uses CV and mediapipe to detect the posture of user and also counts your reps in live feed.
            """
        )
        st.markdown("[GitHub Repo](https://github.com/SumeetD003/GYM.git)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Gesture Detection:- Detects Gestures and can form words using gestures in live feed")
        st.write(
            """
             By capturing live feeds, it recognizes and translates gestures into meaningful words or commands. 
             This innovative system enables users to communicate and form words seamlessly through hand or body gestures,
             offering a dynamic and intuitive way to interact with technology.
            """
        )
        st.markdown("[GitHub Repo](https://github.com/SumeetD003/ProjectGD.git)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/el/vihufa" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
