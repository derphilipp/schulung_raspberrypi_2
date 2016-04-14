#!flask/bin/python
import flask
import idha
import cv2

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/herd', methods=['GET'])
def get_herd():
    stove_is_on = idha.stove_is_on()
    return flask.render_template("herd.html", title='Herd Zustand', stove_is_on=stove_is_on)

@app.route('/state', methods=['GET'])
def get_herd_status():
    stove_is_on = idha.stove_is_on()
    return flask.jsonify({'stove': stove_is_on})


@app.route('/img', methods=['GET'])
def get_herd_status_img():
    img = idha.cut_out_frames()
    ret, img = cv2.imencode('.jpg', img)
    return flask.Response(img.tostring(), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8081)
