from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ddemmmbbdnuhaf:1a78571195b8789db6c427795f864950da38743e5b824ace30c217c7de230f10@ec2-44-195-162-77.compute-1.amazonaws.com:5432/d35qp57ekdsuvv'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False #日本語を利用

#SQLAlchemyでデータベース定義
db = SQLAlchemy(app)
ma = Marshmallow(app)

import src.db