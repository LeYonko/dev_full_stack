from flask import Flask, request
from flask_cors import CORS
from json import JSONEncoder
import json

class Question():

    def __init__(self, id, title, position, text, image, possibleAnswers):
        self.id = id
        self.title = title
        self.position = position
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers
    
    def jsonToQuestion(json_dct):
        return Question(json_dct['title'],json_dct['position'], json_dct['text'],json_dct['image'], json_dct['possibleAnswers'])

    def questionToJson(self):
        json_data = json.dumps(self.__dict__)
        return json_data