import numpy as np
import pandas as pd
import streamlit as st

st.title('Baseball Stats')
#using https://www.baseball-reference.com/leagues/majors/2021-standard-batting.shtml

@st.cache
def load_data(year):
    url = f'https://www.baseball-reference.com/leagues/majors/{year}-standard-batting.shtml'
