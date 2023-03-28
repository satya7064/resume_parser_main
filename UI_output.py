import streamlit as st
import json
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import ImageDraw,Image

# Define a function to read a JSON file and return its contents as a dictionary
def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Define a function to write a dictionary to a JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Define a function to update a JSON file with the contents of a Streamlit form
def update_json_data(form_data, json_data):
    for key in form_data:
        json_data[key] = form_data[key]
    return json_data

# Define the Streamlit app
def main():
    st.title("Resume Parsing")

    # Create the two columns
    col1, col2 = st.columns(2)

    # Create the PDF uploader in the first column
    with col1:
        st.subheader('Uploaded Resume')
        uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded PDF', use_column_width=True)


    # Create the JSON file selector and editor in the second column
    with col2:
        st.subheader('Extracted Details')
        json_file_path = 'resume_data.json'
        json_data = read_json_file(json_file_path)
        #st.write("JSON data:")
        st.write(json_data)

        # Create the Streamlit form to edit the JSON data
        with st.form("details_form"):
            form_data = {}
            for key in json_data:
                form_data[key] = st.text_input(key, value=json_data[key])
            if st.form_submit_button("Sumbit"):
                json_data = update_json_data(form_data, json_data)
                write_json_file(json_file_path, json_data)
                st.success("Saved Changes.")

if __name__ == '__main__':
    main()
