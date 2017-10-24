# -*- coding:utf-8 -*-
# 参考： https://flask-restplus.readthedocs.io/en/0.4.2/swaggerui.html

from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='A sample API',
)

@api.route('/my-resource/<id>', endpoint='my-resource')
@api.doc(params={'id': 'An ID'})
class MyResource(Resource):
    def get(self, id):
        return {}

    @api.doc(responses={403: 'Not Authorized'})
    def post(self, id):
        api.abort(403)


if __name__ == '__main__':
    app.run(debug=True)
