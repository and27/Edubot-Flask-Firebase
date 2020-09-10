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
game_ref = db.collection('game')

edubot = Blueprint('edubot', __name__, url_prefix='/api')


@edubot.route('/game', methods=['POST'])
def add_game():
 #{category, level, name, rating}
 try:
  id = request.json['id']
  game_ref.document(id).set(request.json)
  game = game_ref.document(id).get()
  return response(game.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/game', methods=['GET'])
def get_game():
 try:
  game_id = request.args.get('id')
  if game_id:
   game = game_ref.document(game_id).get()
   return response(game.to_dict())
  else:
   all_games = [doc.to_dict() for doc in game_ref.stream()]
   return response(all_games)

 except Exception as e:
  return bad_request()

@edubot.route('/game/<id>', methods=['PUT'])
def update_game(id):
 try:
  game_ref.document(id).update(request.json)
  game = game_ref.document(id).get()
  return response(game.to_dict())

 except Exception as e:
  return bad_request()

@edubot.route('/game/<id>', methods=['DELETE'])
def delete_game(id):
 #try:
 game_id =  id
 game_ref.document(game_id).delete()
 return response("")

# except Exception as e:
 # return bad_request()


app.register_blueprint(edubot)

port = int(os.environ.get('PORT', 5050))
if __name__ == '__main__':
 	
 app.run(threaded=True, host='0.0.0.0', port=port, debug=True)
