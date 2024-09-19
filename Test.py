import streamlit as st

def main():
    rick_roll_url = "https://www.myinstants.com/media/sounds/rick-rolled.mp3"
    st.audio(rick_roll_url, format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
