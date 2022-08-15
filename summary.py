import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(page_title = "Data Summary")
st.image("image.jpeg")

filename = st.file_uploader("Upload a file")

try: 
    df = pd.read_csv(filename)
    num_rows = len(df)
    num_col = len(df.columns)
    num_na = df.isna().sum()
    df_dtypes = df.dtypes
    cormatrix = df.corr().round(3)
    st.title("DATA SUMMARY DASHBOARD")
    st.write("File:", filename)
    st.dataframe(df.head())
    col1, col2 = st.columns(2)
    col1.write("Number of Rows")
    col1.write(num_rows)

    col2.write("Number of Columns")
    col2.write(num_col)

    col3, col4, col5 = st.columns(3)

    col3.write("Number of NAs")
    col3.write(num_na)

    col4.write("Column Names")
    col4.write(df.columns)

    col5.write("Data Types")
    col5.write(df_dtypes.astype(str))

    st.write("Correlation Matrix", cormatrix)
except ValueError as e:
    st.subheader("WAITING FOR FILE UPLOAD")

