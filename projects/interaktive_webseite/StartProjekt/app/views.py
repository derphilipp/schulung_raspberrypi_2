from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'login': 'Philipp'}
    sensors = [
            {
                'name': 'Temperature Living Room',
                'data': {'set':21, 'measured':19}
                },
            {
                'name': 'Temperature Kitchen',
                'data': {'set':19, 'measured':20}
                }
            ]
    return render_template('index.html', title='Home', user=user, sensors=sensors)
