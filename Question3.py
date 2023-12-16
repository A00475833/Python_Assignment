import streamlit as app
import pandas as data
from matplotlib import pyplot as graph

app.title('Age Distribution Analysis')
data_file = app.file_uploader("Please upload a CSV file:", type="csv")

# Check if a file has been uploaded
if data_file is not None:
    data_frame = data.read_csv(data_file)

    if 'Age' in data_frame.columns and 'Name' in data_frame.columns:
        app.write("Displaying a histogram for the age distribution")
        fig, axis = graph.subplots()
        axis.hist(data_frame['Age'], bins=100, color='blue', edgecolor='white')
        axis.set_xlabel('Age Group')
        axis.set_ylabel('Frequency')
        axis.set_title('Age Distribution Histogram')
        app.pyplot(fig)
    else:
        app.error("The CSV file must contain 'Age' and 'Name' columns.")
else:
    app.write("Please upload a CSV file to proceed.")
