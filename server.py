
from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('front_HTML.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return render_template('result.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
