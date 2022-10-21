# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# show the title
st.title('Titanic App by Junjie Lai')
df = pd.read_csv('train.csv')

# read csv and show the dataframe
st.write(df)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(1, 3, figsize=(15,5))
df[df.Pclass == 1].Fare.plot.box(ax=ax[0])  
df[df.Pclass == 2].Fare.plot.box(ax=ax[1])  
df[df.Pclass == 3].Fare.plot.box(ax=ax[2]) 

st.pyplot(fig)