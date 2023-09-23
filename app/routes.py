from flask_restx import Resource, Namespace
from .models import Player, Team, League, Tournament
from flask import request

from .extensions import mongo

ns = Namespace('api')

@ns.route("/leagues")
class League(Resource):
    @ns.marshal_with(League)
    def get(self):
        leagues = list(mongo.db.leagues.find({}).sort("priority"))
        return leagues, 200 

@ns.route("/teams")
class Team(Resource):
    @ns.marshal_with(Team)
    def get(self):
        teams = list(mongo.db.teams.find({}))
        return  teams,200


@ns.route("/tournaments/per_page<int:per_page>/page<int:page>")
class Tournament(Resource):
    @ns.marshal_with(Tournament)
    def get(self, per_page, page):
      
        # Calculate the skip value for MongoDB
        skip = (page - 1) * per_page

        tournaments = list(mongo.db.tournaments.find({}).skip(skip).limit(per_page))
        return  tournaments,200

@ns.route("/players")
class Player(Resource):
    @ns.marshal_with(Player)
    def get(self):
        players = list(mongo.db.players.find({}))
        return  players,200
    
