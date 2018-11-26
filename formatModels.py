# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:16:24 2018

@author: Armin
"""
import json
import pandas as pd
import os, sys

def formatModel():
    #take our json object and convert to tabular format
    model = {}  
    with open('./Models/distilled_water_model_absolute.json') as f:
        model = f.read().replace('\n', '')
        model = json.loads(model)
    model_df = pd.DataFrame([], columns = ['Cond','PH', 'ORP', 'TDS', 'Turb', 'Desc', 'Timestamp', 'Contaminated'])  
    experiments =  model["Exps"]
    ix = 0 #index of df
    for exp in experiments:
        insert = []
        desc = exp["desc"]
        ts = exp["timeStamp"]
        contaminated = exp["contaminated"]
        
        for result in exp["results"]:
            insert = []
            insert.append(result["Conductivity"])
            insert.append(result["PH"])
            insert.append(result["ORP"])
            insert.append(result["Turp"])
            insert.append(result["TDS"])
            insert.append(desc)
            insert.append(ts)
            insert.append(contaminated)
            
            model_df.loc[ix] = (insert)
            ix += 1
            
    
    return model_df

def get_normalized_values():
    cwd = os.getcwd()
    print(cwd)
    #take our json object and convert to tabular format
    model = {}  
    with open('../../Models/distilled_water_model_norm.json') as f:
        model = f.read().replace('\n', '')
        model = json.loads(model)
        
    model_df = pd.DataFrame([], columns = ['Cond','PH', 'ORP', 'TDS', 'Turb', 'Desc', 'Timestamp', 'Contaminated'])  
    experiments =  model["Exps"]
    ix = 0 #index of df
    for exp in experiments:
        insert = []
        desc = exp["desc"]
        ts = exp["timeStamp"]
        contaminated = exp["contaminated"]
        
        for result in exp["results"]:
            insert = []
            insert.append(result["Conductivity"])
            insert.append(result["PH"])
            insert.append(result["ORP"])
            insert.append(result["Turp"])
            insert.append(result["TDS"])
            insert.append(desc)
            insert.append(ts)
            insert.append(contaminated)
            
            model_df.loc[ix] = (insert)
            ix += 1
            
    
    return model_df

def get_absolute_values():
    #take our json object and convert to tabular format
    model = {}  
    with open('../../Models/distilled_water_model_absolute.json') as f:
        model = f.read().replace('\n', '')
        model = json.loads(model)
    model_df = pd.DataFrame([], columns = ['Cond','PH', 'ORP', 'TDS', 'Turb', 'Desc', 'Timestamp', 'Contaminated'])  
    experiments =  model["Exps"]
    ix = 0 #index of df
    for exp in experiments:
        insert = []
        desc = exp["desc"]
        ts = exp["timeStamp"]
        contaminated = exp["contaminated"]
        
        for result in exp["results"]:
            insert = []
            insert.append(result["Conductivity"])
            insert.append(result["PH"])
            insert.append(result["ORP"])
            insert.append(result["Turp"])
            insert.append(result["TDS"])
            insert.append(desc)
            insert.append(ts)
            insert.append(contaminated)
            
            model_df.loc[ix] = (insert)
            ix += 1
            
    
    return model_df

