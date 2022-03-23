from flask import Flask, redirect, url_for, render_template, request, abort


from app import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    return redirect('dashboard.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html',404)