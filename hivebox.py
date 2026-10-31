"""return version and tempreture"""
import datetime as dt
import requests
from flask import Flask
from project import VERSION

app = Flask(__name__)

@app.route("/version")
def print_version():
    """"return version"""
    return {"version":VERSION}

@app.route("/temperature")
def print_temperature():
    """ Get Tempreture from sensor"""
    fresh_sensors = []
    sensebox_ids = ['5eba5fbad46fb8001b799786',
                    '5c21ff8f919bf8001adf2488',
                    '5ade1acf223bd80019a1011c']
    for sensebox_id in sensebox_ids :
        try:
            r = requests.get('https://api.opensensemap.org/boxes/' + sensebox_id, timeout=20)
        except requests.RequestException:
            continue
        data = r.json()
        for sensor in data['sensors']:
            if sensor.get('title') == 'Temperatur':

                now = dt.datetime.now(tz=dt.UTC)
                last_measurement = dt.datetime.fromisoformat(sensor['lastMeasurement']['createdAt'])
                reading = now - last_measurement

                if reading < dt.timedelta(hours=1) :
                    fresh_sensors.append(float(sensor['lastMeasurement']['value']))

    if fresh_sensors :
        sum_fresh_sensors = sum(fresh_sensors)
        len_fresh_sensors = len(fresh_sensors)
        avg_fresh_sensors = sum_fresh_sensors/ len_fresh_sensors
        return {"temperature":avg_fresh_sensors}
    return {"temperature":"No fresh temperature data available"}
