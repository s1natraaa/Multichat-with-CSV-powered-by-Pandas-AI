import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import Gemini API module
from gemini_api import GeminiAPI


# Initialize Gemini API with your API key
gemini_api_key = "YOUR_GEMINI_API_KEY"
gemini = GeminiAPI(api_key=gemini_api_key)

def chat_with_csv(df, prompt):
    # Call Gemini API functions for data analysis
    # Replace this with actual Gemini API calls for analysis
    result = gemini.perform_analysis(df, prompt)
    return result

st.set_page_config(layout='wide')
st.title("Multiple-CSV ChatApp powered by Gemini API")
st.markdown('<style>h1{color: orange; text-align: center;}</style>', unsafe_allow_html=True)
st.subheader('Built for All Data Analysis and Visualizations')
st.markdown('<style>h3{color: pink;  text-align: center;}</style>', unsafe_allow_html=True)

# Upload multiple CSV files
input_csvs = st.sidebar.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)

if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)

    # Load and display the selected csv file
    st.info("CSV uploaded successfully")
    data = pd.read_csv(input_csvs[selected_index], error_bad_lines=False)
    st.dataframe(data, use_container_width=True)

    # Enter the query for analysis
    st.info("Chat Below")
    input_text = st.text_area("Enter the query")

    # Perform analysis
    if input_text:
        if st.button("Chat with csv"):
            st.info("Your Query: "+ input_text)
            result = chat_with_csv(data, input_text)
            fig_number = plt.get_fignums()
            if fig_number:
                st.pyplot(plt.gcf())
            else:
                st.success(result)