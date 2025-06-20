from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] Location received: Latitude = {lat}, Longitude = {lon}")
    
    # Optional: save to file
    with open("location_log.txt", "a") as f:
        f.write(f"[{timestamp}] Lat: {lat}, Lon: {lon}\n")
    
    return {'status': 'success'}
    
if __name__ == '__main__':
    app.run()
