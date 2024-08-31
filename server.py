from flask import Flask, render_template, request, jsonify
import sqlBackend.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sqlBackend.py', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        # Handle GET requests
        data = {'message': 'Hello from the GET endpoint'}
        return jsonify(data)
    if request.method == 'POST':
      data=request.args.get('inputData')
      name=data[0]
      school=data[1]
      
      
if __name__ == '__main__':
    app.run(debug=True)
    
    