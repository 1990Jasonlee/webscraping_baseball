import numpy as np
import pandas as pd
import streamlit as st

st.title('Baseball Stats')
# using https://www.baseball-reference.com/leagues/majors/2021-standard-batting.shtml

st.sidebar.header('User Input Feature')
select_year = st.sidebar.selectbox('Year', list(reversed(range(1950, 2022))))


@st.cache
def load_data(year):
    url = f'https://www.baseball-reference.com/leagues/majors/{year}-standard-batting.shtml'
    html = pd.read_html(url, header=0)
    df = html[0]
    stat_df = df.iloc[:-3]
    return stat_df
stat_df = load_data(select_year)


sorted_unique_team = sorted(stat_df.Tm.unique())
select_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

df_selected_team = stat_df[(stat_df.Tm.isin(select_team))]

st.dataframe(stat_df)
