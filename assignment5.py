# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title

st.title('Titanic App by Xinyue Zhou :')

# read csv and show the dataframe
df_train = pd.read_csv('train.csv')
df_train

# create a figure with three subplots, size should be (15, 5)
fig,ax = plt.subplots(1,3,figsize = (15,5))

# show the box plot for ticket price with different classes
df_train[df_train['Pclass']==1]['Fare'].plot.box(ax=ax[0]).set_xlabel("Pclass = 1")
ax[0].set_ylabel('Fare')

df_train[df_train['Pclass']==2]['Fare'].plot.box(ax=ax[1]).set_xlabel("Pclass = 2")
ax[1].set_ylabel('Fare')

df_train[df_train['Pclass']==3]['Fare'].plot.box(ax=ax[2]).set_xlabel("Pclass = 3")
ax[2].set_ylabel('Fare')

# you need to set the x labels and y labels
st.pyplot(fig)

# a sample diagram is shown below

