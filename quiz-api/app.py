import json
from flask import Flask, request
from flask_cors import CORS
from Question import Question
from Participation import Participation
import database
from jwt_utils import JwtError, build_token, decode_token
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/rebuild-db', methods=['POST'])
def generationDB():
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        database.generation()
        return 'Ok', 200
        #return "Ok", 200

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hell, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    nb_question = database.getNumberOfQuestion()
    scores = database.getScores()
    return {"size": nb_question[0], "scores": scores}, 200

@app.route('/login', methods=['POST'])
def PostLogin():
	payload = request.get_json()
	test = "flask2023"
	mdp = payload["password"]
	if(test == mdp):
		return {"token": build_token()}, 200
	else:
		return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def PostQuestions():
    #Récupérer le token envoyé en paramètre
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        payload = request.get_json()
        question_decoded = Question(0, payload["title"], payload["position"], payload["text"], payload["image"], payload["possibleAnswers"])
        questionByPosition = database.getQuestion("position", question_decoded.position)
        if (questionByPosition == None):
            id = database.insertRequest(question_decoded)
            question_decoded.id = id
            return {"id": question_decoded.id}, 200
        else:
            #decaler les positions à partir de question
            database.updatePositions(questionByPosition)
            id = database.insertRequest(question_decoded)
            question_decoded.id = id
            return {"id": question_decoded.id}, 200

@app.route('/questions/<question_id>', methods=['GET'])
def getQuestionById(question_id):
    question = database.getQuestion("id", question_id)
    if (question == None):
        return {}, 404
    else:
        return {"id": question.id, "title": question.title, "position": question.position, "text": question.text, "image": question.image, "possibleAnswers": question.possibleAnswers}, 200
    
@app.route('/questions', methods=['GET'])
def getQuestionByPosition():
    position = request.args.get("position")
    question = database.getQuestion("position", position)
    if (question == None):
        return {}, 404
    else:
        return {"id": question.id, "title": question.title, "position": question.position, "text": question.text, "image": question.image, "possibleAnswers": question.possibleAnswers}, 200

@app.route('/questions/<question_id>', methods=['PUT'])
def updateQuestionById(question_id):
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        payload = request.get_json()
        question = database.getQuestion("id", question_id)
        if (question == None):
            return {}, 404
        else:
            database.updateQuestion(question_id, payload, question)
            return {}, 204;

@app.route('/questions/<question_id>', methods=['DELETE'])
def deleteQuestion(question_id):
	#Récupérer le token envoyé en paramètre
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        question = database.getQuestion("id", question_id)
        if (question == None):
            return {}, 404
        else:
            database.deleteQuestion(question_id, question)
            return {}, 204
    
@app.route('/questions/all', methods=['DELETE'])
def deleteAllQuestions():
	#Récupérer le token envoyé en paramètre
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        database.deleteAllQuestions()
        return {}, 204
    
@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipations():
    #Récupérer le token envoyé en paramètre
    paramToken = request.headers.get('Authorization')
    if (paramToken == None):
        return 'Unauthorized', 401
    else:
        try:
            token = paramToken.replace("Bearer ", "")
            decode_token(token)
        except JwtError as error:
            print('Error occured - ', error)
            return 'Unauthorized', 401
        database.deleteAllParticipations()
        return {}, 204
    
@app.route('/participations', methods=['POST']) #changer id de participation une fois dans la base
def addParticipation():
    payload = request.get_json()
    #participation = Participation(0, payload["playerName"], )
    nb_question = database.getNumberOfQuestion()
    nb_answers = len(payload["answers"])
    if (nb_question[0] != nb_answers):
        return {}, 400
    else:
        now = datetime.now()
        # convert to string
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        answersSummaries, score = database.getAnswersSummaries(payload["answers"])
        participation = Participation(0, payload["playerName"], score, date)
        id = database.insertParticipation(participation)
        participation.id = id
        return {"answersSummaries": answersSummaries, "playerName": participation.playerName, "score": participation.score}, 200

if __name__ == "__main__":
    app.run()