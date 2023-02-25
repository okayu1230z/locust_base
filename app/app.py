from flask import Flask, request
import random, string, json, ast, os

port = int(os.environ['PORT'])
app = Flask(__name__)

def get_name(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def create_user(name):
    return random.randint(0, 300)

@app.route('/<int:id>', methods=["GET"])
def get(id):
    id = id
    name = get_name(10)

    return {
        "id": id,
        "name": name,
    }

@app.route('/', methods=["POST"])
def post():
    name = ast.literal_eval(request.data.decode('utf-8'))["name"]
    id = create_user(name)

    return {
        "id": id,
        "name": name
    }, 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
