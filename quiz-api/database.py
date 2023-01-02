import sqlite3
from Participation import Participation
from Question import Question
import json

from sqlite3 import Error

def createConnection():
    conn = None
    try:
        conn = sqlite3.connect('bdd.db')
    except Error as e:
        print(e)
    return conn

def getNumberOfQuestion():
    conn = createConnection()
    cur = conn.cursor()
    try:
        result = cur.execute('SELECT COUNT(*) FROM question').fetchall()[0]
        conn.commit()

    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return result

def insertRequest(question):
    conn = createConnection()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO question (title, position, text, image, possibleAnswers) VALUES (?, ?, ?, ?, ?)',
                        (question.title, question.position, question.text, question.image, json.dumps(question.possibleAnswers, ensure_ascii=False)))
        id = cur.lastrowid
        conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return id

def getQuestion(key, val):
    conn = createConnection()
    try:
        if (key == "id"):
            result = conn.execute('SELECT * FROM question WHERE id = ?', (val,)).fetchone()
            conn.commit()
            if (result == None):
                return None
        elif (key == "position"):
            result = conn.execute('SELECT * FROM question WHERE position = ?', (val,)).fetchone()
            conn.commit()
            if (result == None):
                return None
        else:
            conn.close()

        question = None
        question = Question(result[0], result[1], result[2], result[3], result[4], result[5])
        question.possibleAnswers = json.loads(question.possibleAnswers)

    except sqlite3.Error as error:
        print('Error occured - ', error)
    finally:
        if conn:
            conn.close()
            print('SQLite Connection closed')
    return question

def updateQuestion(question_id, payload, question):
    conn = createConnection()
    cur = conn.cursor()
    try:
        if (question.position > payload["position"]):
            result = cur.execute('SELECT * FROM question WHERE position >= ? AND position <= ?', (payload["position"], question.position)).fetchall()
            #conn.commit()
            for row in result:
                if (row[2] == question.position):
                    cur.execute('UPDATE question SET position = ? WHERE id = ?',
                            (payload["position"], row[0]))
                    conn.commit()
                elif (row[2]<question.position):
                    cur.execute('UPDATE question SET position = ? WHERE id = ?',
                            (row[2]+1, row[0]))
                    conn.commit()
                else:
                    return 0
                   #if (payload["position"] == question.position):
            cur.execute('UPDATE question SET title = ?, position = ?, text = ?, image = ?, possibleAnswers = ? WHERE id = ?',
                (payload["title"], payload["position"], payload["text"], payload["image"], json.dumps(payload["possibleAnswers"], ensure_ascii=False), question_id))
            conn.commit()
        elif (question.position < payload["position"]):
            result = cur.execute('SELECT * FROM question WHERE position <= ? AND position >= ?', (payload["position"], question.position)).fetchall()
            #conn.commit()
            for row in result:
                if (row[2] == question.position):
                    cur.execute('UPDATE question SET position = ? WHERE id = ?',
                            (payload["position"], row[0]))
                    conn.commit()
                elif (row[2]>question.position):
                    cur.execute('UPDATE question SET position = ? WHERE id = ?',
                            (row[2]-1, row[0]))
                    conn.commit()
                else:
                    return 0
                   #if (payload["position"] == question.position):
            cur.execute('UPDATE question SET title = ?, position = ?, text = ?, image = ?, possibleAnswers = ? WHERE id = ?',
                    (payload["title"], payload["position"], payload["text"], payload["image"], json.dumps(payload["possibleAnswers"], ensure_ascii=False), question_id))
            conn.commit()
        elif (question.position == payload["position"]):
            cur.execute('UPDATE question SET title = ?, position = ?, text = ?, image = ?, possibleAnswers = ? WHERE id = ?',
                    (payload["title"], payload["position"], payload["text"], payload["image"], json.dumps(payload["possibleAnswers"], ensure_ascii=False), question_id))
            conn.commit()
        else:
            return 0
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return 1

def deleteQuestion(question_id, question):
    conn = createConnection()
    cur = conn.cursor()
    try:
        result = cur.execute('SELECT * FROM question WHERE position > ?', (question.position,)).fetchall()
        #conn.commit()
        for row in result:
            cur.execute('UPDATE question SET position = ? WHERE id = ?',
                    (row[2]-1, row[0]))
            conn.commit()
        conn.execute('DELETE FROM question WHERE id = ?',
                (question_id,))
        conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return 1

def deleteAllQuestions():
    conn = createConnection()
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM question')
        conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return 1

### Au moment de l'ajout, si la position de la question est la même que celle d'une question deja enregistrée, on décale de 1 la position de toutes les questions
def updatePositions(questionByPosition):
    conn = createConnection()
    cur = conn.cursor()
    try:
        result = cur.execute('SELECT * FROM question WHERE position >= ?', (questionByPosition.position,)).fetchall()
        #conn.commit()
        for row in result:
            cur.execute('UPDATE question SET position = ? WHERE id = ?',
                    (row[2]+1, row[0]))
            conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return 1

def deleteAllParticipations():
    conn = createConnection()
    cur = conn.cursor()
    try:
        cur.execute('DELETE FROM participation')
        conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return 1

def getCorrectAnswerPosition(question):
    answers = question.possibleAnswers
    index = 0
    while (index < 4):
        if (answers[index]["isCorrect"] == False):
            index+=1
        else:
            break
    return index+1

def getAnswersSummaries(answers):
    score = 0
    answersSummaries = []
    for i in range(1, len(answers)+1):
        list = []
        question = getQuestion("position", i)
        answer = answers[i-1]
        correctAnswerPosition = getCorrectAnswerPosition(question)
        if (answer == correctAnswerPosition):
            boolean = 1
            score+=1
        else:
            boolean = 0
        list.append(correctAnswerPosition)
        list.append(boolean)
        answersSummaries.append(list)
    return answersSummaries, score

def insertParticipation(participation):
    conn = createConnection()
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO participation (playerName, score, date) VALUES (?, ?, ?)',
                    (participation.playerName, participation.score, participation.date))
        id = cur.lastrowid
        conn.commit()
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return id

def getScores():
    scores = []
    conn = createConnection()
    cur = conn.cursor()
    try:
        result = cur.execute('SELECT * FROM participation ORDER BY score DESC')
        for row in result:
            participation = Participation(row[0], row[1], row[2], row[3])
            score = {'playerName': participation.playerName, 'score': participation.score, 'date': participation.date}
            scores.append(score)
    except sqlite3.Error as error:
        print('Error occured - ', error)
        return 0
    finally:
        if conn:
            cur.close()
            conn.close()
            print('SQLite Connection closed')
    return scores