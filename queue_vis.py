from flask import Flask, render_template, url_for

app = Flask(__name__)

data_active_procs = {
    'bacillus': 1242,
    'bulls1k': 70,
    'cowfert': 1,
    'cows10k': 51,
    'das': 94,
    'pulsemarker': 24,
}


@app.route('/')
def graph():
    return render_template('graph1.html', data=data_active_procs)


if __name__ == '__main__':
    app.run()
