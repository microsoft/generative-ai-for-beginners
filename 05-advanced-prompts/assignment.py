from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    """
    Say hello to the user.
    If a 'name' parameter is provided in the request, greet them with their name.
    Otherwise, greet them with 'World'.
    """
    name = request.args.get('name', 'World')
    if not name:
        return jsonify(message="Error: 'name' parameter is required."), 400
    return jsonify(message=f'Hello, {name}!')

if __name__ == '__main__':
    # Load configurations from a config file (config.py)
    app.config.from_object('config')
    app.run()
    
    