from flask import Flask, request
from flask.blueprints import Blueprint
import requests
from flask_httpauth import HTTPBasicAuth
import re

url = 'https://api.bittrex.com/api/v1.1/public/getmarketsummaries'
url2 = 'https://api.bittrex.com/api/v1.1/public/getmarketsummary'

auth = HTTPBasicAuth()
site = Blueprint('site', __name__)


class Sky():
    def __init__(self):
        pass
    
    @auth.verify_password
    def verify(username, password):
        '''
        For authenticationg the API the function is defined        
        '''  
        USER_DATA = {"admin": "asd#2&(^*(&%^&%*&"}        
        if not(username and password):
            return False        
            return USER_DATA.get(username) == password
    
    @site.route('/', methods=['GET'])
    @auth.login_required
    def index():
        '''
        This function will returns all the data
        '''
        req = requests.get(url).json()
        return req

    @site.route('/getmarketsummary/', methods=['GET'])
    @auth.login_required
    def get_all_data():
        '''
        This function will returns the data which is queried
        '''
        user_querry = str(request.args.get('market'))
        pattern = re.compile('\D{3}.\D{3}')
        if pattern.match(user_querry):
            url1 = url2+"?market=" + user_querry
            req = requests.get(url1).json()
            return (req)
        return "<h1>Wrong choice</h1>"
    