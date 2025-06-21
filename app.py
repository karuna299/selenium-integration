from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask API!"})

@app.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
        return "Server shutting down...", 200
    return "No shutdown hook", 500

if __name__ == '__main__':
    app.run(port=5000)
