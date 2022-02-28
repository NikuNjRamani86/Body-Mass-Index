# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""

from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)
model = pickle.load(open('height-weight-preiction.pkl','rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit():
    if request.method == 'POST':
        Male = request.form['Male']
        if (Male=='Male'):
            Male=1
        else:
            Male=0
          
        
        Height = int(request.form['height'])
        Weight = int(request.form['weight'])
        
        data = np.array([[Male,Height,Weight]])
        
        my_pred = model.predict(data)
        
        return render_template('result.html',prediction=my_pred)
        
        
if __name__=="__main__":
    app.run(debug=True)
            

