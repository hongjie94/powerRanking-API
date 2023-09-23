from .extensions import api
from flask_restx import fields

League = api.model('leagues', {
  'id': fields.String,
  'name': fields.String,
  'slug': fields.String,
  'sport': fields.String,
  'image': fields.String,
  'lightImage': fields.String,
  'darkImage': fields.String,
  'region': fields.String,
  'priority': fields.Integer,
  'displayPriority': fields.Raw,  # Use 'Raw' for an object field
  'tournaments': fields.List(fields.Raw),
})

Tournament = api.model('tournaments', {
  'id': fields.String,
  'leagueId': fields.String,
  "name":fields.String,
  "slug":fields.String,
  "sport":fields.String,
  "startDate":fields.String,
  "endDate":fields.String,
  "stages": fields.List(fields.Raw)
})

Player = api.model('players', {
  'player_id': fields.String,
  'handle': fields.String,
  "first_name":fields.String,
  "last_name":fields.String,
  "home_team_id":fields.String
})
  
Team = api.model('teams', {
  'team_id': fields.String,
  'name': fields.String,
  "acronym":fields.String,
  "slug":fields.String
})
  


  

