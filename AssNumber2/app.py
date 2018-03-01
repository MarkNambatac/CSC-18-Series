from flask import Flask, jsonify, request

app = Flask(__name__)
DEBUG = True
HOST = "localhost"
PORT = 8080
courseList = [{'courseName': 'BSEE',
              'courseName': 'BSCS',
               'courseName': 'BSIT'
              }]

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'message': 'Now working..'})

@app.route('/course', methods = ['GET'])
def allCourses():
    return jsonify({'courses': courseList})

@app.route('/course/<string:courseName>', methods = ['GET'])
def course(courseName):
    course = [course for course in courseList if course['courseName'] == courseName]
    return jsonify({'courses': course[0]})

@app.route('/language', methods = ['POST'])
def addCourse():
    course = {'courseName': request.json['courseName']}
    courseList.append(course)
    return jsonify({'courses': courseList})

@app.route('/language/<string:courseName>', methods = ['PUT'])
def updateCourse(courseName):
    course = [course for course in courseList if course['courseName'] == courseName]
    course[0]['courseName'] = request.json['courseName']
    return jsonify({'courses' : course[0]})

@app.route('/language/<string:courseName>', methods = ['DELETE'])
def removeCourse(courseName):
    course = [course for course in courseList if course['courseName'] == courseName]
    courseList.remove(course[0])
    return jsonify({'language': courseList})

if __name__ == '__main__':
    app.run(debug = DEBUG, host = HOST, port = PORT)