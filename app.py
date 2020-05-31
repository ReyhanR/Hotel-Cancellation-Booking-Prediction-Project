from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

######################
# FUNCTION FOR ROUTE #
######################

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/visual')
def visual():

    return render_template('visualisasi.html')

@app.route('/prediksi', methods = ['POST', 'GET'])
def predict():
    if request.method == "POST":
        input = request.form
    
        feature = [ 
                    int(input['country']), 
                    int(input['deposit_type']), 
                    float(input['lead_time']), 
                    int(input['total_of_special_requests']), 
                    int(input['adr']), 
                    int(input['market_segment']), 
                    int(input['arrival_date_day_of_month']), 
                    int(input['arrival_date_week_number']), 
                    int(input['stays_in_week_nights']),
                    ]

        scaled_feat = scaler.transform([feature])
        
        pred = GBModel.predict(scaled_feat)[0]
        pred_proba = GBModel.predict_proba(scaled_feat)
        endresult = f"{round(np.max(pred_proba)*100,2)}% {'(Cancel)' if pred == 1 else '(Not Cancel)'}"

        return render_template('prediksi.html', data = input, prediction = endresult,
            country = input['country'], deposit_type = input['deposit_type'], lead_time=input['lead_time'],
            total_of_special_requests=input['total_of_special_requests'], adr=input['adr'], market_segment=input['market_segment'], 
            arrival_date_day_of_month=input['arrival_date_day_of_month'], arrival_date_week_number=input['arrival_date_week_number'], stays_in_week_nights=input['stays_in_week_nights'],)

if __name__ == '__main__':
    GBModel = joblib.load('GBModelNormalData')
    scaler = joblib.load('RobScalerHotelnew')

    app.run(debug = True)