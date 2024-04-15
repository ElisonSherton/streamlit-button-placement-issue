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

def get_fig(field, x_col):
    df = st.session_state.df
    field = st.session_state.fields[st.session_state.count]
    fig, ax = plt.subplots(1, 1, figsize = (10, 2))    
    ax.scatter(df[x_col], df[field], color='black')
    ax.set_title(f"Studying {field} wrt {x_col}")
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


# Render some things like sliders etc. which you want
s1 = st.slider("slide1", min_value=1, max_value=100)

# Now render the figures
field = st.session_state.fields[st.session_state.count]
fig_col1, _, fig_col2 = st.columns([5,1,5])
fig_col1.pyplot(get_fig(field, "dose"))
fig_col2.pyplot(get_fig(field, "days"))

# Then render the next and previous buttons
col1, _, col2 = st.columns([3, 20, 3])
with col1:
    if st.button("⏮️ Previous", on_click=previous_field):
        pass

with col2:
    if st.button("Next ⏭️", on_click=next_field):
        pass