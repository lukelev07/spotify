# Author: Luke Levis
import spotipy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 

# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

# main takes in song name 
# searched for all songs with 'remix' in title 
# adds all songs (including original search) into playlist titles 'keyword'



if __name__ == '__main__':
    app.run()
