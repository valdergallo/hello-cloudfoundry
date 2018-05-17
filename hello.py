import bottle
import os


# uwsgi will call application
app = application = bottle.Bottle()
PORT = os.environ.get("PORT", 8080)


@app.route('/')
def hello():
    return "Hello World! SAP CF"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
