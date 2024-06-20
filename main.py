# main.py
import streamlit as st
import helper as helper
import logging
import threading
from flask_app import app 

logging.basicConfig(level=logging.DEBUG)

def run_flask_app():
    app.run(debug=True) 

def main():
    st.title("Daffodil Smart Bot")
    text_input = st.text_input("What do you want to know?")

    if st.button("Get Information"):
        if text_input.strip():
            data = helper.get_information(text_input)
            if "answer" in data:
                answer = data["answer"]
                st.success(answer)
            else:
                st.error("No answer found for the query.")
        else:
            st.warning("Please enter a question to get an answer.")

if __name__ == "__main__":
   
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    main()