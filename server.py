from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def printTest():
  print("hello world from server.py")
  

if __name__ == '__main__':
    app.run(debug=True)