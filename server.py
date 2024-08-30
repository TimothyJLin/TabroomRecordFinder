from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/print.py', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        # Handle GET requests
        data = {'message': 'Hello from the GET endpoint'}
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    
    