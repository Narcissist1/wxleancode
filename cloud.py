# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError

from app import app


engine = Engine(app)


@engine.before_save('StudyButler')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')