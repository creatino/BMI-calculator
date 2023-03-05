from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight']) * 0.45359237 
    feet = float(request.form['feet'])
    inches = float(request.form['inches'])
    height = (feet * 12 + inches) * 0.0254  # convert feet and inches to meters
    bmi = weight / (height * height)
    emoji = '😊' if 18.5 <= bmi <= 24.9 else '😞'

    return render_template('index.html', bmi=bmi, emoji=emoji)

if __name__ == '__main__':
    app.run(debug=True)
