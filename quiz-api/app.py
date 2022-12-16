from flask import Flask, request
from flask_cors import CORS
from jwt_utils import build_token

app = Flask(__name__)
CORS(app)

#payload = request.get_json()

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hell, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def PostLogin():
	payload = request.get_json()
	test = "flask2023"
	mdp = payload["password"]
	if(test == mdp):
		return {"token": build_token()}, 200
	else:
		return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()