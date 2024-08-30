from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def printTest():
  print("hello world from server.py")

  
  app.get("/html", (request, response) => {
  try {
    fetch(request.query.url)
      .then(res => res.text())
      .then(text => {
        response.send(text);
      });
  } catch(e) {
    response.status(400).json(
        { message: "Something went wrong." + e}
      );
  }
});  

if __name__ == '__main__':
    app.run(debug=True)
    
    