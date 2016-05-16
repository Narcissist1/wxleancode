# coding: utf-8

from leancloud import Object
from leancloud import Query
from leancloud import LeanCloudError
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify


test_views = Blueprint('test', __name__)


class StudyButler(Object):
    pass


@test_views.route('')
def show():
    try:
        study = Query(StudyButler).descending('createdAt').find()
    except LeanCloudError, e:
        raise e
    print study
    return 'Hello'


@test_views.route('', methods=['POST'])
def add():
    study = StudyButler(
        referer=request.form['referer'],
        method=request.form['method'],
        name=request.form['name'],
        tel=request.form['tel'],
        grade=request.form['grade']
    )
    try:
        study.save()
    except LeanCloudError as e:
        return e.error, 502
    return redirect(url_for('test.show'))
