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
player_ref = db.collection('player')

edubot = Blueprint('edubot', __name__, url_prefix='/api')


@edubot.route('/player', methods=['POST'])
def add_player():
 #{name, bday, avatar, grade, school}
 try:
  id = request.json['id']
  player_ref.document(id).set(request.json)
  player = player_ref.document(id).get()
  return response(player.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/player', methods=['GET'])
def get_player():
 try:
  player_id = request.args.get('id')
  if player_id:
   player = player_ref.document(player_id).get()
   return response(player.to_dict())
  else:
   all_players = [doc.to_dict() for doc in player_ref.stream()]
   return response(all_players)

 except Exception as e:
  return bad_request()

@edubot.route('/player/<id>', methods=['PUT'])
def update_player(id):
 try:
  player_ref.document(id).update(request.json)
  player = player_ref.document(id).get()
  return response(player.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/player/<id>', methods=['DELETE'])
def delete_player(id):
 #try:
 player_id =  id
 player_ref.document(player_id).delete()
 return response("")

# except Exception as e:
 # return bad_request()


app.register_blueprint(edubot)

port = int(os.environ.get('PORT', 5050))
if __name__ == '__main__':
 	
 app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
