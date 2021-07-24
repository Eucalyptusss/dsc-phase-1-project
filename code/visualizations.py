{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}




import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import data_preparation as dp


def budget_corr(budget_and_profit):
#This method populates a heatmap showing correlation between production budget
#and domestic/worldwide gross. It also returns a table of associated correlations.
    plt.figure(figsize=(12,10))
    cor = budget_and_profit[['production_budget','domestic_gross','worldwide_gross']].corr()
    sns.heatmap(cor, annot=True,cmap=plt.cm.Reds)
    plt.show()
    cor_target = abs(cor["production_budget"])
    relevant_features = cor_target[cor_target>.5]
    return(relevant_features)
    
def budget_line(budget_and_profit):
#This function populates a line graph comparing budget to domestic/worldwide
#gross
    w_gross=budget_and_profit['worldwide_gross']
    d_gross=budget_and_profit['domestic_gross']
    b=budget_and_profit['production_budget']
    df = pd.DataFrame({
    'worldwide gross': list(w_gross),
    'domestic gross': list(d_gross)},
    index=list(b))

    ax=df.plot.line(figsize=(10,5))
    plt.xlabel("Budget(USD)")
    plt.xticks(np.linspace(0,425000000,num=10))
    plt.yticks(np.linspace(0,2776345279,num=10))
    plt.title("Budget vs worldwide and domestic gross")
    ax.yaxis.set_major_formatter(dp.format_num)
    ax.xaxis.set_major_formatter(dp.format_num)
    plt.ylabel("Gross $ Amount(USD)")

    
def run_all(run_df):
#This function populates all of the movies in run_df into a line chart
#that compares runtime(min) vs domestic/worldwide gross
    df = pd.DataFrame({
    'worldwide gross': list(run_df.worldwide_gross),
    'domestic gross': list(run_df.domestic_gross)},
    index=list(run_df.runtime))
    ax=df.plot.line(figsize=(10,5))
    ax.yaxis.set_major_formatter(dp.format_num)
    plt.xlabel("Runtime (minutes)")
    plt.title("Runtime vs worldwide and domestic gross")
    plt.ylabel("Gross $ Amount ()")
    
def run_avg(avg_world,avg_domestic,index):
#This function makes a bar chart with x axis as time ranges (min) and
# y axis is average gross
    df = pd.DataFrame({
    'Average Worldwide Gross':avg_world,
    'Average Domestic Gross':avg_domestic},
     index=index)


    ax=df.plot.bar(rot=0)
    ax.yaxis.set_major_formatter(dp.format_num)
    
    plt.xlabel("Runtime (minutes)")
    plt.title("Runtime range vs Average domestic/worldwide gross ")
    plt.ylabel("Gross $ Amount (USD)")
    
def rating_bar(r,pg_13,pg,g):
    df = pd.DataFrame({
    'Ratings':['R','PG-13','PG','G'],
    'Average Box Office Earnings':[r,pg_13,pg,g]})
    ax=df.plot.barh(x='Ratings',y='Average Box Office Earnings')
    ax.xaxis.set_major_formatter(dp.format_num)    