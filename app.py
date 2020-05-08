from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import (
    User,
    UserLogin,
    UserRegister,
    TokenRefreshResource,
)
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mysupersecretkey'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

# Add claims to all requests
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}

# Access token has expired
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The access token has expired.',
        'error': 'access_token_expired',
    }), 401

# Access token is invalid (not a valid access token)
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Invalid access token.',
        'error': 'invalid_access_token',
    }), 401

# Access token was not sent in the request
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'message': 'Request does not contain an access token.',
        'error': 'access_token_required',
    }), 401

# Access token was sent in the request and is not a fresh one
# but the endpoint requires it to be a fresh one
@jwt.needs_fresh_token_loader
def token_not_fresh_callback(error):
    return jsonify({
        'message': 'The access token is not fresh.',
        'error': 'fresh_access_token_required',
    }), 401

# Revoke a token
@jwt.revoked_token_loader
def revoke_token_callback(error):
    return jsonify({
        'message': 'The access token has been revoked.',
        'error': 'access_token_required',
    }), 401

api.add_resource(User, '/user/<int:name>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(TokenRefreshResource, '/refresh')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

db.init_app(app)

if __name__ == '__main__':
    # db.init_app(app)
    app.run(port=5000, debug=True)
