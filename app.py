# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:11:18 2019

@author: Amir
"""

from flask import Flask , render_template ,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def upload_file():
    target_image_path = request.form.get('target')
    style_reference_image_path = request.form.get('style')            
    return render_template('success.html')
    
if __name__ =="__main__":
	app.run(debug=True)

















