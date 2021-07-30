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




                
def construct_gross_col(budget_and_profit, movie_profits_df, known_titles):
    """
    This function return a list of dataframe rows that from movie_profits_df
    and budget_and_profit IF the row's movie title is in known_titles
    
    """
    domestic = []
    titles_one=list(budget_and_profit.movie)
    titles_two=list(movie_profits_df.title)
    for title in known_titles:
        if title in titles_one:
            domestic.append(budget_and_profit.loc[budget_and_profit.movie == \
                                                 title])
        elif title in titles_two:
            domestic.append(movie_profits_df.loc[movie_profits_df.title == \
                                                title])
  
    return domestic
def construct_runtime_col(additional_movie_info_df, known_titles):
    """
    This function compares known_titles to titles in the dataframe
    additional_movie_info_df. If a title is in both the list and the df
    then it is added to a list called runtimes. This function returns that
    list. The list needs further cleaning because some elements of the list
    have multiple rows due to duplicate movie titles. 
    """
    
    titles= list(additional_movie_info_df.primary_title)

    rel_titles=[]
    for el in known_titles:
        if el in titles:
            rel_titles.append(el)
    rel_titles = list(set(rel_titles))       
    runtimes = []
    df = additional_movie_info_df.copy()
    for title in rel_titles:
        
            
        runtime = df.loc[df.primary_title == title]
        runtimes.append(runtime)
    runtimes = runtimes
    
    return runtimes   



    
#old name was better_runtime_titles
def list_of_titles_with_runtime(additional_movie_info_df):
    """
    This function takes the data frame additional_movie_info_df and returns a list 
    of movie titles that have an associated runtime i.e. not NaN. 
    """
    better_titles = additional_movie_info_df.loc[additional_movie_info_df["runtime_minutes"].\
                                        isna() == False].primary_title
    return better_titles

#old name was unique_names
def list_common_titles(movie_profits_df,budget_and_profit):   
    """ 
    This function returns a list of common movie titles within movie_profits_df and budget_and_profit. It does this by looping through each of the associated columns and checking if the movie title is in the alternative dataframe. Before returning, duplicates are removed from the list and the list is sorted. 
    """
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
    """
    This function formats graphs by adding B to billions, M to milliions, 
    and K to thousands
    """

    if data_value >= 1_000_000_000:
        formatter = '{:1.2f}B'.format(data_value*.000000001)
        return formatter
    elif data_value >= 1_000_000:
        formatter = '{:1.1f}M'.format(data_value*0.000001)
        return formatter
    elif data_value >= 1_000:
        formatter = '{:1.0f}K'.format(data_value*.001)
        return formatter
    else:
        formatter=None
    


def change_cols_to_int(col_to_change):
    """ This function returns a column of values after stripping them
    of , and $. Then each element is casted as an integer. """
    clean_col = col_to_change.str.replace(',','')
    clean_col = clean_col.apply(lambda x: x.strip('$'))
    clean_col = clean_col.astype('int64')
    return clean_col


def populate_average_world(df,start_val):
    """
    This function takes in a dataframe and the starting range for the desired average value for the worldwide gross. It does this by first assigning a sample size of 58. Then for i in range(60, 181, 60) it has three conditional statements; i==60,i==180, or else statemente. Conditionals 60 and 180 run a .loc on the df parameter [df.runtime < 60].sort_values(by='worldwide_gross').\
tail(sample).worldwide_gross.mean(). Which collects the top 58 values from the dataframe returned by the .loc.

    """
    sample = 58
   
    average = []
    for i in range(60, 180, 60):
        
        if i == 60:
            
            average.append(
                df.loc[df.runtime < 60].sort_values(by='worldwide_gross').\
                tail(sample).worldwide_gross.mean()
            )
           
            
        average.append(
        df.loc[(df.runtime>=i)  & (df.runtime < (i+60))].
            sort_values(by='worldwide_gross').
            tail(sample).worldwide_gross.mean())
      
    
    return average 


def populate_average_dom(df,start_val):
    """
  This function takes in a dataframe and the starting range for the desired average value for the domestic gross. It does this by first assigning a sample size of 58. Then for i in range(60, 181, 60) it has three conditional statements; i==60,i==180, or else statemente. Conditionals 60 and 180 run a .loc on the df parameter [df.runtime < 60].sort_values(by='domestic_gross').\
tail(sample).domestic_gross.mean(). Which collects the top 58 values from the dataframe returned by the .loc.
    """
    sample = 58
   
    average = []
    for i in range(60, 180, 60):
        
        if i == 60:
            
            average.append(
                df.loc[df.runtime < 60].sort_values(by='worldwide_gross').\
                tail(sample).domestic_gross.mean()
            )
       
          
            
        average.append(df.loc[(df.runtime>=i) & (df.runtime < (i+60))].
            sort_values(by='worldwide_gross').tail(sample).domestic_gross.mean())
      
    
    return average

    
    
    
    
    
    
    