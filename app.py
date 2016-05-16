import os

import leancloud
from flask import Flask

from config import APPID, MASTERKEY
from views import test_views

APP_ID = os.environ.get('LC_APP_ID', APPID)
MASTER_KEY = os.environ.get('LC_APP_MASTER_KEY', MASTERKEY)

leancloud.init(APP_ID, master_key=MASTER_KEY)

app = Flask(__name__)
engine = leancloud.Engine(app)


app.register_blueprint(test_views, url_prefix='/test')
