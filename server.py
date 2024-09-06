from flask import Flask, render_template, request, jsonify
import sqlBackend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sqlBackend.py', methods=['GET', 'POST'])
def handle_request():
  if request.method == 'POST':
    
    if request.is_json:
      return jsonify('fuck')
      #data = request.get_json() 
#      return jsonify({'screw you'})
#      return jsonify(data['school'])

      if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400      
      #return jsonify("POST REQUEST RECIEVED STONKS")


      #data=request.get['inputData']
      #name=data['name']
      #school=data['school']
      #return jsonify("school: "+school)
      result=sqlBackend.findDebater("name", "school")
      return result
    else:
        return jsonify({'error': 'Unsupported method'}), 405 


if __name__ == '__main__':
    app.run(debug=True)
    
    