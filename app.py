from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
led_state = "off"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/led', methods=['GET'])
def get_led():
    return jsonify({'state': led_state})

@app.route('/api/led', methods=['POST'])
def set_led():
    global led_state
    data = request.get_json()
    led_state = data.get('state', 'off')
    return jsonify({'success': True, 'state': led_state})

if __name__ == '__main__':
    app.run(debug=True)
