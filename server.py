from flask import Flask, render_template, request, jsonify
import sqlBackend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sqlBackend.py', methods=['GET', 'POST'])
def handle_request():
  if request.method == 'POST':
    debaterInfo=request.get_json()
    debaterName=jsonify(debaterInfo['debaterName'])
    debaterSchool=jsonify(debaterInfo['debaterSchool'])
#return jsonify(debaterInfo['debaterName'])
    debaterArray=sqlBackend.findDebater("name", "school")
    print("result: "+str(debaterArray))
    return jsonify(debaterArray)
  else:
      return jsonify({'error': 'Unsupported method'}), 405 


if __name__ == '__main__':
    app.run(debug=True)
    
    