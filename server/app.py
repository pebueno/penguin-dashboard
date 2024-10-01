from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    print("Hi")  # Console log
    return {"message": "Hi"}  # Return a simple JSON response

if __name__ == '__main__':
    app.run(debug=True)
