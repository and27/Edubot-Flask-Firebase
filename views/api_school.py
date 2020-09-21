# Required Imports
import os
from flask import Flask, request, jsonify, Blueprint
from firebase_admin import credentials, firestore, initialize_app
from responses.responses import bad_request, response

# Initialize Flask App
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('edubot-f2362-firebase-adminsdk-k4fzh-6c456bc9e2.json')
default_app = initialize_app(cred)
db = firestore.client()

#Here is the reference to your database collection (School, player, subject, etc)
school_ref = db.collection('school')

edubot = Blueprint('edubot', __name__, url_prefix='/api')

@edubot.route('/school', methods=['POST'])
def add_school():
 #{name, bday, avatar, grade, school}
 try:
  id = request.json['id']
  school_ref.document(id).set(request.json)
  school = school_ref.document(id).get()
  return response(school.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/school', methods=['GET'])
def get_school():
 try:
  school_id = request.args.get('id')
  if school_id:
   school = school_ref.document(school_id).get()
   return response(school.to_dict())
  else:
   all_schools = [doc.to_dict() for doc in school_ref.stream()]
   return response(all_schools)

 except Exception as e:
  return bad_request()

@edubot.route('/school/<id>', methods=['PUT'])
def update_school(id):
 try:
  school_ref.document(id).update(request.json)
  school = school_ref.doument(id).get()
  return response(school.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/school/<id>', methods=['DELETE'])
def delete_school(id):
 # try:
  school_id = id
  school_ref.document(school_id).delete()
  # school = school_ref.document(id).get()
  return response("")

 # except Exception as e:
 #  return bad_request()

@edubot.route('/school/signin',  methods=['GET', 'POST'])
def signin_school():
    unsuccessful = 'Error en registro'
    successful = 'Se Registro Correctamente'
    if request.method=='POST':
        name = request.form['name_school']
        location = request.form['location_school']
        students_num = request.form['students_school']
        type_s = request.form['type_school']

        post = {
            "location": location,
            "name": name,
            "students_num": int(students_num),
            "type_s": type_s
        }

        try:
          db.collection("school").add(post)
          return render_template('forms/signin_school.html', s=successful)
        except:
          return render_template('forms/signin_school.html', us=unsuccessful)

    return render_template('forms/signin_school.html', the_title='Registrate')

 

app.register_blueprint(edubot)

port = int(os.environ.get('PORT', 5050))
if __name__ == '__main__':
  app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
