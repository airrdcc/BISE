import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, jsonify
from data.hive_query import get_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = get_data()
    return render_template('dashboard.html', data=data)

@app.route('/api/data')
def api_data():
    data = get_data()
    # 构造前端需要的格式
    return jsonify({
        "categories": ["销售额", "订单数", "用户数"],
        "values": [data["sales"], data["orders"], data["users"]]
    })

def run_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run_app()