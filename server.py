from flask import Flask, render_template, request, jsonify
import sqlBackend

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
      return jsonify("POST REQUEST RECIEVED STONKS")
      data=request.args.get('inputData')
      name=data[0]
      school=data[1]
      result=sqlBackend.findDebater(name, school)
      return result
      
      
if __name__ == '__main__':
    app.run(debug=True)
    
    