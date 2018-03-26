import bottle

# uwsgi will call application
app = application = bottle.Bottle()


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
