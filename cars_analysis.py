import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Page title
st.title("Car Dataset Analysis")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../Dataset/CARS.csv")
    df['MSRP'] = df['MSRP'].replace('[$ ,]', '', regex=True).astype('int64')
    df['Invoice'] = df['Invoice'].replace('[$ ,]', '', regex=True).astype('int64')
    return df

df = load_data()

# Car type selection
types = df['Type'].unique()
selected_type = st.selectbox("Select Car Type", types)

# Filter by selected type
typ = df[df['Type'] == selected_type]

# Origin selection
origins = typ['Origin'].unique()
selected_origin = st.selectbox("Select Car Origin", origins)

# Filter by selected origin
orii = typ[typ['Origin'] == selected_origin]

# Plot
st.subheader(f"MSRP for {selected_type} cars from {selected_origin}")
fig, ax = plt.subplots()
sb.barplot(x=orii['Type'], y=orii['MSRP'], ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)
