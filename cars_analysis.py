import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/CARS.csv")

# Clean data
df["MSRP"] = df["MSRP"].replace('[$ ,]', '', regex=True).astype('int64')
df["Invoice"] = df["Invoice"].replace('[$ ,]', '', regex=True).astype('int64')

# Sidebar for user input
st.title("Car Price Analysis")

# Select Type
types = df["Type"].unique()
selected_type = st.selectbox("Select Car Type", types)

# Filter by selected type
filtered_type_df = df[df["Type"] == selected_type]

# Show available origins
origins = filtered_type_df["Origin"].unique()
selected_origin = st.selectbox("Select Car Origin", origins)

# Final filtered DataFrame
final_df = filtered_type_df[filtered_type_df["Origin"] == selected_origin]

# Plot
st.subheader(f"MSRP Distribution for {selected_type} cars from {selected_origin}")
fig, ax = plt.subplots()
sb.barplot(x=final_df["Type"], y=final_df["MSRP"], ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
