# weather-app
A web application that fetches and displays current weather information for a specified location using the OpenWeatherMap API

## Technologies Used
- Python
- Flask
- OpenWeather API
- HTML/CSS
## Virtual Environment Setup (LINUX)

* Install 'virtualenv' if it's not already installed
```
pip install virtualenv
```
## Installation
* Navigate to desired directory of installation
```
python3 -m venv <environment name>
example: python -m venv .venv
```
* Activate the virtual environment
```
  source <venv name>/bin/activate
```
* Clone the repository by entering this in the terminal
```
git clone https://github.com/linalvinv/weather-app.git
```
* Use pip or pip3 to install all the dependencies
```
pip install -r requirements.txt
```
## OpenWeatherMap API Setup

* Create an OpenWeatherMap account at https://openweathermap.org.
* Create an API key at https://home.openweathermap.org/api_keys.
* Place API key into .env file

## Run

After virtual enviroment is set up, you may run the following line to start the program
```
flask run
```
To start the program in debug mode:
```
python app.py
```
