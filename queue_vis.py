from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def graph():
    return render_template('graph1.html')


if __name__ == '__main__':
    app.run()
