# -*- coding: utf-8 -*-

import datetime
import streamlit as st  #Web App
import requests
import os
# import basic
import basic_test
import aspose.words as aw
from PIL import Image, ImageOps
# from PIL import Image
from pdf2image import convert_from_path
import json
import pandas as pd

#Make streamlit to wide screen
st.set_page_config(layout="wide")

# Hide made with streamlit and Hamburger menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Uploading file in the form of pdf, doc and docx format 
# image = Image.open(r'BPAI_logo.png')
# st.image(image)
st.header("RESUME PARSER")
input_file=st.file_uploader(label='UPLOAD PDF FILE HERE:',type=['pdf','doc','docx'])

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
def display(input_file):
    # Checking uploaded file is pdf or doc or docx
    if input_file is not None:
        if input_file.type == "application/pdf":
            with open(os.path.join("uploaded_files", input_file.name),"wb") as f:
                    f.write((input_file).getbuffer())
            pdf_file = os.path.join("./uploaded_files/", input_file.name)
            data = basic_test.extraction(pdf_file)
            
        else:
            with open(os.path.join("uploaded_files", input_file.name),"wb") as f:
                    f.write((input_file).getbuffer())
            pdf_file = os.path.join("./uploaded_files/", input_file.name)
            doc = aw.Document(input_file)
            # doc.save("./uploaded_files/temp.pdf")
            saveOptions = aw.saving.PdfSaveOptions()
            saveOptions.compliance = aw.saving.PdfCompliance.PDF17
            doc.save("./uploaded_files/temp.pdf", saveOptions)
            data =basic_test.extraction('./uploaded_files/temp.pdf')
        edit(input_file)

    else:
        st.write("Upload a pdf")

# st.subheader('Invoice Details')
def edit(input_file):
    # Create two columns, one for the PDF and the other for the extracted data
    col1, col2 = st.columns(2)

    # Convert the first page of the PDF file to an image and display it in the first column
    with col1:
        st.subheader("Uploaded Resume")
        st.write(" ")
        pdf_file = os.path.join("./uploaded_files/", input_file.name)
        pages = convert_from_path(pdf_file, 500, first_page=1)
        for page in pages:
            image = ImageOps.autocontrast(page.convert('RGB'))
            st.image(image, use_column_width=True)

        # Display the extracted data in the second column
    with col2:
        #     st.subheader("Resume Details")
        #     st.write(" ")
        #     # st.write(data)
        #     for k,v in data.items():
        #         st.write(k,":", v)

        st.subheader('Extracted Details')
        json_file_path = './output_files/resume_output.json'
        json_data = read_json_file(json_file_path)
        #st.write("JSON data:")
        # st.write(json_data)

        # Create the Streamlit form to edit the JSON data
        with st.form("details_form"):
            form_data = {}
            for key in json_data:
                form_data[key] = st.text_input(key, value=json_data[key])
            if st.form_submit_button("Sumbit"):
                json_data = update_json_data(form_data, json_data)
                write_json_file(json_file_path, json_data)
                st.success("Saved Changes.")

        # form_data = {}
        # for key in json_data:
        #     form_data[key] = st.text_input(key, value=json_data[key])
        # # save_format = st.radio('Select the format:',['text','excel','database'])
        
        # if st.button("Sumbit"):
        #     json_data = update_json_data(form_data, json_data)
        #     write_json_file(json_file_path, json_data)
        #     json_file_path = './output_files/resume_output.json'
        #     json_data = read_json_file(json_file_path)
        #     # if save_format == 'text':
        #     #     with open('./output_files/resume_out.txt', 'w') as convert_file:
        #     #         convert_file.write(json.dumps(json_data))
        #     # if save_format=='excel':
        #     #     df1 = pd.DataFrame(data=json_data, index=[0])
        #     #     df1.to_excel('./output_files/resume_output.xlsx')
        #     # if save_format=='database':
        #     #     basic_test.db_data(json_data)
        #     st.success("Saved Changes.")

    st.success("Resume Data Extracted Successfully")

if __name__ == '__main__':
    display(input_file)

