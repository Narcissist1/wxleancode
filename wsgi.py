# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from app import app, engine
import leancloud
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from config import *

leancloud.init(APPID, master_key=MASTERKEY)

application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    server = WSGIServer(('localhost', 3000), application, handler_class=WebSocketHandler)
    server.serve_forever()