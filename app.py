from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    #false if user has not inputted any information
    input = False
    data = None
    if request.method == 'POST':
        #toggles to true
        input = True
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city,state,country)
    return render_template('index.html',data=data,input = input)

if __name__ == '__main__':
    app.run(debug=True)