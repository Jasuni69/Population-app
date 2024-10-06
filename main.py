import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

file_path = "cleaned_folkmängd_data.csv" #File location
df = pd.read_csv(file_path) #Loading file and creating a dataframe named df
df["civilstatus_gender"] = df["civilstånd"] + " " + df["kön"] #Making new column calle civilstatus_gender that is a concatenation of column civilstånd and column kön


min_year = int(df["år"].min()) #Variable of the lowest value of år column using .min
max_year = int(df["år"].max()) #Variable of the highest value of år column using .max
year_options = list(range(min_year, max_year + 1)) #Create list of years from min year to max year


st.header("Select gender and relationship status") #Header for multiselect list
civilstatus_gender_options = df["civilstatus_gender"].unique() #Listing all unique values of civilstatus_gender and assigning them to civilstatus_gender_options
civilstatus_gender_selected = st.multiselect("Välj kön och civilstatus", #Multiselect function where chosen option is assigned to civilstatus_gender_selected, 
                                 options= civilstatus_gender_options #listed options are civilstatus_gender_options 
                                 )

selected_year = st.select_slider("Årtal", #Slider function using the min_year, max_year year_options list
                 options=year_options,
                 value=min_year #Default value when starting is smallest value i.e 1968 df["år"].min()
)



slide_df = df[df["år"] == selected_year]
civilstatus_gender_df = slide_df[slide_df["civilstatus_gender"].isin(civilstatus_gender_selected)]
color_map = {
    "gifta män": "blue",
    "gifta kvinnor": "green",
    "ogifta män": "red",
    "ogifta kvinnor": "orange",
    "skilda män": "purple",
    "skilda kvinnor": "pink",
    "änkor/änklingar män": "gray",
    "änkor/änklingar kvinnor": "brown"
}


fig = px.scatter(civilstatus_gender_df,
                  x="ålder",
                  y="Folkmängd", 
                  color="civilstatus_gender", 
                  color_discrete_map=color_map, 
                  title=f"Population by age and gender in {selected_year}"
)



st.plotly_chart(fig)

