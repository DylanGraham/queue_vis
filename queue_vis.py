from flask import Flask, render_template, url_for

app = Flask(__name__)

data = {
    'bacillus': (207, 1242),
    'bulls1k': (59, 70),
    'cowfert': (1, 1),
    'cows10k': (5, 51),
    'das': (17, 94),
    'pulsemarker': (2, 24)
}


@app.route('/')
def graph():
    return render_template('graph1.html', data=data)


if __name__ == '__main__':
    app.run()
