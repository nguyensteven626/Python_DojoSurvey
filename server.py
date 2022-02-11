from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'uber super secret key'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    session['your_name'] = request.form['your_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    
    return redirect('/info')

@app.route('/info')
def show_info():
    return render_template('info.html')

if __name__ =="__main__":
    app.run(debug=True)