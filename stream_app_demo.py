# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:08:52 2023

@author: AMROL
"""
import pandas as pd
import calisolpy
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import os


st.title("CALISOL 	:sun_with_face:")
st.write("Hello guys")


# read the dataframe
total_data=pd.read_pickle("stream_data.pkl")

# select a scan id
scan_id=total_data['Scan ID'].unique()
scan_slider=st.sidebar.select_slider("select a scan",options=scan_id)

# filter the dataframe on the scan id
df=total_data[total_data['Scan ID']==scan_slider]

# choose x and y axis
x_axis_selection=st.sidebar.selectbox("Select the x_axis",df.columns)
y_axis_selection=st.sidebar.selectbox("Select the y_axis",df.columns)


# scan parameters
date_scan=(df['Timestamp'].min()).date()
start_date=df['Timestamp'].min().time()

with st.container():
    col11,col12,col13=st.columns(3)
    col11.metric("date",f"{date_scan.day}/{date_scan.month}/{date_scan.year}")
    col12.metric("start time", f"{start_date.hour}:{start_date.minute}:{start_date.second}")
    col13.metric("scan duration",f"{(df['Timestamp'].max()-df['Timestamp'].min()).total_seconds()/60}")

with st.container():
    col21,col22,col23=st.columns(3)
    col21.metric("azimuth target",f"{df['Azimuth []'].min()}")
    col22.metric("ele min",f"{df['Elevation []'].min()}")
    col23.metric("ele max",f"{df['Elevation []'].max()}")
    

# plot the graph
with st.container():
    fig=plt.figure()
    sns.scatterplot(data=df,x=x_axis_selection,y=y_axis_selection,hue='spectral_density_median',palette=sns.color_palette("viridis", as_cmap=True))
    plt.title(f"Scan id : {scan_slider}")
    plt.xticks(rotation=60)
    plt.legend(loc="upper left",bbox_to_anchor=(1,1))
    st.pyplot(fig)

# plot a plotly graph
with st.container():

    fig_plotly=px.histogram(data_frame=df,x='spectral_density_median')
    st.plotly_chart(fig_plotly, use_container_width=True)











    
