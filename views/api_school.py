# Required Imports
import os
from flask import Flask, request, jsonify, Blueprint
from firebase_admin import credentials, firestore, initialize_app
from responses.responses import bad_request, response

# Initialize Flask App
# app = Flask(__name__)
# Initialize Firestore DB
cert_file = "here_the_json_withyourfirestore_credentials"
cred = credentials.Certificate(cert_file)
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

@edubot.route('/school', methods=['PUT'])
def update_school():
 try:
  id = request.json['id']
  school_ref.document(id).update(request.json)
  school = school_ref.doument(id).get()
  return response(school.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/school', methods=['DELETE'])
def delete_school():
 try:
  school_id = request.args.get('id')
  school_ref.document(school_id).delete()
  school = school_ref.document(id).get()
  return response(school)

 except Exception as e:
  return bad_request()

port = int(os.environ.get('PORT', 5050))
if __name__ == '__main__':
    edubot.run(threaded=True, host='0.0.0.0', port=port, debug=True)
