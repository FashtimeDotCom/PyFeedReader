__author__ = 'sis13'

from flask import *
import bcrypt
import random
import time
from pyfeedreader import app
from pyfeedreader.database import db_session
from pyfeedreader.models.user import User
from flask.ext.login import *


mod = Blueprint('index', __name__)

@mod.route("/", methods=["GET"])
@login_required
def index():
    return render_template("index.html")