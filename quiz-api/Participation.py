from flask import Flask, request
from flask_cors import CORS

class Participation():

    def __init__(self, id, playerName, score, date):
        self.id = id
        self.playerName = playerName
        self.score = score
        self.date = date
