from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    print(f"Location received: Latitude={lat}, Longitude={lon}")
    return 'Location received successfully!'

if __name__ == '__main__':
    app.run(debug=True)
