import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# Select wide mode 
st.set_page_config(layout="wide")

if 'count' not in st.session_state:
    st.session_state.count = 0

# Define your fields or your quotes that you want to display
if 'fields' not in st.session_state:
    st.session_state.fields = ["chemical1", "chemical2", "chemical3"]

# Read the data 
if 'data' not in st.session_state:
    st.session_state.df = pd.read_csv("data.csv")

def get_fig(field):
    df = st.session_state.df
    field = st.session_state.fields[st.session_state.count]

    fig, ax = plt.subplots(1, 2, figsize = (10, 2))
    
    ax[0].scatter(df["days"], df[field], color='black')
    ax[1].scatter(df["dose"], df[field], color='black')

    ax[0].set_xlabel("Days"); ax[0].set_ylabel(field)
    ax[1].set_xlabel("Dose"); ax[1].set_ylabel(field)
    
    fig.suptitle(f"{field} statistics")
    return fig
    
def next_field():
    if st.session_state.count + 1 >= len(st.session_state.fields):
        st.session_state.count = 0
    else:
        st.session_state.count += 1

def previous_field():
    if st.session_state.count > 0:
        st.session_state.count -= 1

st.title("Chemical Analysis")

field = st.session_state.fields[st.session_state.count]
fig = get_fig(field)

# Render some things like sliders etc. which you want
s1 = st.slider("slide1", min_value=1, max_value=100)

# First render the figure
st.pyplot(fig)

# Then render the next and previous buttons
col1, _, col2 = st.columns([3, 20, 3])
with col1:
    if st.button("⏮️ Previous", on_click=previous_field):
        pass

with col2:
    if st.button("Next ⏭️", on_click=next_field):
        pass