#!/usr/bin/env python3
# from tryOn import TryOn as tryOn

from flask import Flask, render_template, Response,redirect,request
from camera import VideoCamera
import os
app = Flask(__name__)

CART=[]

@app.route('/tryall',methods = ['POST', 'GET'])
def tryall():
        CART = request.form['mydata'].replace(',', '/')
        os.system('python test.py ' + CART)
        render_template('index.html', message='')


@app.route('/')
def indexx():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/clothes')
def clothes():
    return render_template('clothes.html')

@app.route('/necklace')
def necklace():
    return render_template('necklace.html')

@app.route('/earrings')
def earrings():
    return render_template('earrings.html')

@app.route('/goggles')
def goggels():
    return render_template('goggles.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/webcontact')
def webcontact():
    return render_template('web-contact.html')
    

if __name__ == '__main__':
    app.run()
    