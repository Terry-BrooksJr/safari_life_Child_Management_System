from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "<h1>Hello Earth!!<H1>"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)