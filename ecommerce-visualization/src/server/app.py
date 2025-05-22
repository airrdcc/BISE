from flask import Flask, render_template
from data.hive_query import get_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = get_data()
    return render_template('dashboard.html', data=data)

def run_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run_app()