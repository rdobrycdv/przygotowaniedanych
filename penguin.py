import streamlit as st
import seaborn as sns
import altair as alt
import pandas as pd

st.title("Penguins... not again")
penguins = sns.load_dataset("penguins")
st.write(penguins)
x2"""
## Data description
%d number of penguins
""" % penguins.shape[0]

species = penguins["species"].unique()
change_species = st.selectbox("Select species: ", species)

sex = penguins["sex"].dropna().unique()
change_sex = st.selectbox("Select sex: ", sex)

filter = penguins[(penguins['species'] == change_species) & (penguins['sex'] == change_sex)]
filter

frame = pd.DataFrame(filter, columns=['bill_length_mm', 'bill_depth_mm', "flipper_length_mm"])
st.line_chart(frame)

chart = alt.Chart(penguins.dropna()).mark_circle().encode(
    alt.X("bill_depth_mm"),
    alt.Y("flipper_length_mm"),
    color="sex",
    tooltip=['species', 'sex', "bill_depth_mm", 'body_mass_g', 'flipper_length_mm'],
    size='body_mass_g'
).properties(
    width=650,
    height=450
).interactive()

st.altair_chart(chart)
