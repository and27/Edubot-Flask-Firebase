# app.py
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
subject_ref = db.collection('subject')

edubot = Blueprint('edubot', __name__, url_prefix='/api')


@edubot.route('/game', methods=['POST'])
def add_subject():
 #{contents, id, level, name}
 try:
  id = request.json['id']
  subject_ref.document(id).set(request.json)
  subject = subject_ref.document(id).get()
  return response(subject.to_dict())

  except Exception as e:
  return bad_request()


@edubot.route('/subject', methods=['GET'])
def get_subject():
 try:
  subject_id = request.args.get('id')
  if subject_id:
   subject = subject_ref.document(subject_id).get()
   return response(subject.to_dict())
  else:
   all_subjects = [doc.to_dict() for doc in subject_ref.stream()]
   return response(all_subjects)

 except Exception as e:
  return bad_request()

@edubot.route('/subject/<id>', methods=['PUT'])
def update_subject(id):
 try:
  subject_ref.document(id).update(request.json)
  subject = subject_ref.document(id).get()
  return response(subject.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/subject/<id>', methods=['DELETE'])
def delete_subject(id):
 #try:
 subject_id =  id
 subject_ref.document(subject_id).delete()
 return response("")

# except Exception as e:
 # return bad_request()

app.register_blueprint(edubot)

port = int(os.environ.get('PORT', 5050))
if __name__ == '__main__':
 	
 app.run(threaded=True, host='0.0.0.0', port=port, debug=True)