import os
import sys
from wtforms import StringField,PasswordField,SubmitField
from flask import Flask
from wtforms.validators import DataRequired,EqualTo
from flask_wtf import DataRequired_EqualTo

app=Flask(__name__)

