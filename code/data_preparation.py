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


def remove_NaN(run_df):
#This function removes NaN values from run_df.worldwide_gross column
    for idx in range(len(run_df.worldwide_gross)):
        if type(run_df.worldwide_gross[idx]) != int:
            if len(run_df.worldwide_gross[idx]) > 1:
                run_df.worldwide_gross[idx]=run_df.worldwide_gross[idx].dropna()
    

def construct_run(budget_and_profit ,movie_profits_df,\
                  additional_movie_info_df, run_df,known_titles):
#This function adds runtime,doemstic gross, and worldwide gross to the 
#three lists below. Then the lists are placed as the columns for run_df
    ordered_domestic=[]
    ordered_runtime=[]
    ordered_worldwide=[]

    titles_one=list(budget_and_profit.movie)


    titles_two=list(movie_profits_df.title)


    for title in known_titles:
        ordered_runtime.append(
        additional_movie_info_df.loc[additional_movie_info_df.primary_title==title]\
            .runtime_minutes)
        if title in titles_one:
            ordered_domestic.append(
            budget_and_profit.loc[budget_and_profit.movie==title].domestic_gross)
            ordered_worldwide.append(
            budget_and_profit.loc[budget_and_profit.movie==title].worldwide_gross)
        elif title in titles_two:
            ordered_domestic.append(
            movie_profits_df.loc[movie_profits_df.title==title].domestic_gross)
            ordered_worldwide.append(
            movie_profits_df.loc[movie_profits_df.title==title].foreign_gross)
            
    run_df.domestic_gross=ordered_domestic
    run_df.runtime=ordered_runtime
    run_df.worldwide_gross=ordered_worldwide
    

def better_runtime_titles(additional_movie_info_df):
#This function makes a list of titles that habe an associated runtime 
#i.e not NaN
    better_titles = additional_movie_info_df.loc[additional_movie_info_df["runtime_minutes"].\
                                        isna() == False].primary_title
    return better_titles


def unique_names(movie_profits_df,budget_and_profit):
#This function goes through two dataframes with profit information and makes
#a list of unique movie titles that have an associated $ amount.
    unique_names=[]
    for movie in movie_profits_df.title:
        if movie in list(movie_profits_df.loc[movie_profits_df.domestic_gross.isna()==False].title)\
        and\
        movie in list(movie_profits_df.loc[movie_profits_df.foreign_gross.isna()==False].title):
            unique_names.append(str(movie))
        
    for movie in budget_and_profit.movie:
        if movie in  list(budget_and_profit.loc[ budget_and_profit.domestic_gross.isna()==False].movie) \
        and\
        movie in list(budget_and_profit.loc[ budget_and_profit.worldwide_gross.isna()==False].movie):
            unique_names.append(str(movie))
    

    unique_names=list(set(unique_names))
    unique_names.sort()
    return unique_names

def format_num(data_value,indx):
#This function formats graph data to show B for billion, M for million,
# and k for thousand
    if data_value >= 1_000_000_000:
        formatter = '{:1.2f}B'.format(data_value*.000000001)
    elif data_value >= 1_000_000:
        formatter = '{:1.1f}M'.format(data_value*0.000001)
    else:
        formatter = '{:1.0f}K'.format(data_value*.001)
    return formatter


def clean_it(em):
#This function cleans the neccessary columns of budget_and_profit
    #cleans budget
    budget = em['production_budget'].str.\
replace(',','')
    budget=budget.apply(lambda x: x.strip('$'))
    em['production_budget']=budget.astype('int64')
    #cleans domestic gross
    budget = em['domestic_gross'].str.\
replace(',','')
    budget=budget.apply(lambda x: x.strip('$'))
    em['domestic_gross']=budget.astype('int64')
    #cleans worldwide gross
    budget = em['worldwide_gross'].str.\
replace(',','')
    budget=budget.apply(lambda x: x.strip('$'))
    em['worldwide_gross']=budget.astype('int64')

    
def clean_run(rune):
#This function fixes the datatypes of the run_df by casting to int
    index=0
    for i in rune:
        if type(i) != int:
            if len(i) > 1:
                rune[index]=int(rune[index][rune[index].idxmin()])
            else:
                rune[index]=int(rune[index])
            index+=1
        else:
            rune[index]=int(rune[index])
            index+=1
          
    
#These methods will return the average gross provided a runtime range of count - count+60 {

def populate_average_world(data,count):
    count = count
    average = data.loc[(data.runtime>count) & (data.runtime<=count+60)].\
    worldwide_gross.mean()
    return average

def populate_average_dom(data,count):
    count = count
    average = data.loc[(data.runtime>count) & (data.runtime<=count+60)].\
    domestic_gross.mean()
    return average    
#}


    
    
    
    
    
    
    