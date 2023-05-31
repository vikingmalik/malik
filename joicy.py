import json
import requests
import streamlit as st

from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Joicy",
    page_icon="😎"
    )



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


def home():
    
    st.subheader("This is Martina Joicy")
    st.write("I am very much excited to see the adventure of my life 🤠")
    st.image("j5.JPG")

def edu():
    st.title("EDUCATION")
    st.text("I am currently pursuing my Bachelors Degree. At AKNU in RJY")
    st.write("That's what in this section! okay! No worries ,I'll be add more in this 👍")
    lottie_coding = load_lottiefile("C:/Users/malik/Desktop/cool.json")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=None,
        width=None,
        key=None,
        )

def passi():
    st.title("PASSION")
    st.text("1.Getting  Degree Certificate\n2.High paying job\n3.Nice family\n4.L_drop husband\n5.Enjoy")

def intre():
    st.title("INTEREST")
    st.text("1.dancing\n2.singing\n3.shorts\n4.walking around")
    st.write("to show my editing skills!! down below")
    st.video('C:/Users/malik/Desktop/j3.mp4')


def con():
    st.title("CONTACT")
    st.text("NAME : JOICY\nNUM:xxxxxxxxxx\nMail:xxxxxxx@gmail.com")
    st.write("THAT'S ALL ABOUT ME IN SHORT. THANK YOU!!!")
    st.image("j2.JPG")
    st.write("BYE !!😚")
    

st.title("MARTINA JOICY")


st.sidebar.title('wanna know me!!')

options = st.sidebar.radio('pages',options = ["home/story 😅",  
                                               "EDUCATION",
                                                "PASSION",
                                                "INTEREST",
                                                "CONTACT"]
                                                )

if options == "home/story 😅":
    home()
   
elif options == "EDUCATION":
    edu()
elif options == "PASSION":
    passi()
elif options == "INTEREST":
    intre()
elif options == "CONTACT":
    con()
    
    




    
