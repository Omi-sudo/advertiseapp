import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("Water_Bill app")

total_bill = st.slider('Enter total water bill', 100, 1000)
st.subheader("Total Bill is")
st.write(total_bill)

each_bill = total_bill/13
shitole = each_bill * 4
st.write('Bill for Shitole is Rs:', shitole)

limbe = each_bill * 2
st.write('Bill for Limbe is Rs:', limbe)

bansode = each_bill * 3
st.write('Bill for Bansode is Rs:', bansode)

infinity = each_bill * 4
st.write('Bill for Infinity Academy is Rs:', infinity)