import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.write("""
#DND-MONSTERS AND STUFF

         Monsters and creatures from Dungeons & Dragons
         """)

@st.cache
def get_data():
    url = "hirviot.json"
    return pd.read_json(url)

df = get_data()
#print(df.to_string())
#petsName = df.get("name")

#alt.renderers.enable('notebook') not working

pets = df.get("name")
typeofpets = df.get("type")
sizeofpets = df.get("size")
hitpointsofpets = df.get("hit_points")
armor_class_of_pets = df.get("armor_class")
petsChallenge = df.get('challenge_rating')
##This is a one way to show things in radio buttons or selectbox/dropdown menu.
##One idea would be to make this go trought, but this is not working yet, either np not working or something else
#all the monsters and then when you click it would show all the stats etc
st.header("Monsters by selectbox")
pet = st.selectbox("Pick a creature",
    (pets[11], pets[78], pets[145]))
if pet == pets[78]:
    st.write(typeofpets[78])
    st.write(sizeofpets[78])
    st.write(hitpointsofpets[78])
    st.write(armor_class_of_pets[78])
if pet == pets[11]:
    st.write(typeofpets[11])
    st.write(sizeofpets[11])
    st.write(hitpointsofpets[11])
    st.write(armor_class_of_pets[11])
if pet == pets[145]:
    st.write(typeofpets[145])
    st.write(sizeofpets[145])
    st.write(hitpointsofpets[145])
    st.write(armor_class_of_pets[145])