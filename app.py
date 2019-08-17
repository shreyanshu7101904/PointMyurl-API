from flask import Flask
import sys
# from apis.test.test import sms_twilio
# from apis.charts.bar.BarChart import bar_chart


app = Flask(__name__)
# app.register_blueprint(sms_twilio)
# app.register_blueprint(bar_chart)

@app.route('/')
def hello_world():
    return 'test-api'

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    # app.run(debug = True, port= 4000)