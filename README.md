# Drop Columns from Dataset using Streamlit

This is a simple web application built with Streamlit that lets users upload a CSV file, drop selected columns, and then download the modified dataset.

## Features
- **CSV File Uploader**: Upload your dataset in CSV format.
- **Data Preview**: View the contents of your uploaded dataset.
- **Column Selector**: Choose which columns you wish to drop.
- **Download Link**: After modification, download your new dataset with the undesired columns removed.

## Installation and Setup

1. First, make sure you have Python installed. If not, download and install [Python](https://www.python.org/downloads/).

2. Clone the repository: 📥 Installation

To get started with this project, you can clone the repository:

`git clone https://github.com/teevoCompany/DataDrop.git`

3. Navigate to the directory file: `cd C:\Users\User\Desktop\Ddrop>`
4. Install the necessary libraries to your virtual env: `pip install -r requirments.txt`
5. Run the Streamlit app: `streamlit run app.py`



## 🛠 How to Use
### 1. Upload CSV File:
      * Click on the "Choose a CSV file" button.
      * Select your CSV file.
### 2. Preview Data:
      * After uploading, preview the data directly in the application.
### 3. Drop Columns:
      * Use the multiselect widget to select the columns you want to remove.
### 4. Download Modified Data:
      * Click the "Drop Columns" button after selecting columns.
      * A download link appears. Click on "Download Modified CSV File" to get the updated dataset.
## 📌 Utility Function
`The code includes a utility function, get_table_download_link(df).
It generates a download`

   

