import streamlit as st
import pandas as pd
import base64

st.title("Drop Columns from Dataset")

# Upload dataset
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    # Read the uploaded CSV
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(data)
    
    # Select columns to drop
    columns = data.columns.tolist()
    columns_to_drop = st.multiselect("Select columns to drop:", columns)
    
    if st.button("Drop Columns"):
        data.drop(columns=columns_to_drop, inplace=True)
        st.write("Modified Data:")
        st.write(data)

        # Offer the option to download the modified dataset
        csv = data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download Modified CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

# This is a simple utility function to encode data into base64
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download Modified CSV File</a>'
    return href

# Note: Make sure to have the necessary libraries installed using pip:
# pip install streamlit pandas
