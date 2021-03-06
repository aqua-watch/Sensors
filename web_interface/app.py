#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Markup

import json
import sys
sys.path.insert(0, '../')
from formatModels import get_model_json, get_values_from_json
#sys.path.append('arm/web_interface/')

MODEL_DIR = "../Models/"
MODEL_NAME  = "/phase_1/model"
NORM_MODEL_PATH = MODEL_DIR + MODEL_NAME + "_norm.json"
ABS_MODEL_PATH =  MODEL_DIR + MODEL_NAME + "_absolute.json"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_content():
    norm_json = get_model_json(NORM_MODEL_PATH)
    abs_json = get_model_json(ABS_MODEL_PATH)

    #norm_df = get_values_from_json(norm_json)
    absolute_df = get_values_from_json(abs_json)
    
    # contaminated_norm = norm_df[norm_df.Contaminated >= 1]
    contaminated_abs = absolute_df[absolute_df.Contaminated >= 1]
            
    times = []
    
    i = 5
    for _ in range(0, int(len(contaminated_abs) / 50)):
        times.append(i)
        i += 5
        
    ##### For normalized #####
    norm_ph = []
    norm_cond = []
    norm_orp = []
    norm_tds = []
    norm_turp = []
    
    norm_ph_std = []
    norm_cond_std = []
    norm_orp_std = []
    norm_tds_std = []
    norm_turp_std = []
    
    abs_ph = []
    abs_cond = []
    abs_orp = []
    abs_tds = []
    abs_turp = []
    
    exps = abs_json["Exps"]
    for exp in exps:
        if(exp["contaminated"] == 1): 
            abs_ph.append(exp["center_point"]["PH"])
            abs_cond.append(exp["center_point"]["Conductivity"])
            abs_orp.append(exp["center_point"]["ORP"])
            abs_tds.append(exp["center_point"]["TDS"])
            abs_turp.append(exp["center_point"]["Turp"])    
    
    absolute_html = Markup(absolute_df.to_html())
    
    return render_template(
        'content.html', 
        absolute=absolute_html, 
        times=json.dumps(times),
        abs_ph=abs_ph,
        abs_cond=abs_cond,
        abs_orp=abs_orp,
        abs_tds=abs_tds,
        abs_turp=abs_turp,
    ) 
    
if __name__ == '__main__':
    #app.debug = True
    app.run(host= '0.0.0.0')
    
    
    
    
    
    
    
