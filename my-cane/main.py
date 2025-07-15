# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# @app.route('/upload', methods=['POST'])
# def upload():
#     data = request.get_json()
#     print("📍 收到位置:", data)
#     return jsonify({"status": "received"}), 200
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
# 以上是最基础的功能 现在开始进行拓展
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)
gps_data = {"lat": 0.0, "lng": 0.0}

@app.route('/')
def index():
    return render_template('map.html')  # 显示地图页面

@app.route('/upload', methods=['POST'])
def upload():
    global gps_data
    try:
        data = request.get_json(force=True)
        # 容错提取：若缺少字段则使用默认值
        gps_data['lat'] = float(data.get('lat', 0.0))
        gps_data['lng'] = float(data.get('lng', 0.0))
        print("🛰️ 收到坐标：", gps_data)
        return jsonify({"status": "received"}), 200
    except Exception as e:
        print("❌ 错误：", e)
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/latest')
def latest():
    return jsonify(gps_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


