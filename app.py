from flask import Flask, render_template, jsonify
import speedtest
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speedtest')
def speed_check():
    try:
        sp = speedtest.Speedtest()
        sp.get_servers()
        download_speed = round(sp.download() / (10**6), 2)
        upload_speed = round(sp.upload() / (10**6), 2)
        return jsonify({'download': f"{download_speed} Mbps", 'upload': f"{upload_speed} Mbps"})
    except Exception as e:
        print("Error:", e)
        return jsonify({'download': 'Error', 'upload': 'Error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
