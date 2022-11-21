from src import app
from src import db
from src import ma
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, desc

# DBの作成
class test(db.Model):
    __tablename__ = 'test'
    id = db.Column(Integer, primary_key=True) #連番（主キー）
    date = db.Column(String(8)) #日付
    time = db.Column(String(8)) #時刻

@app.before_first_request
def init():
    db.create_all()

class testSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = test
test_schema = testSchema(many=True)

#GET(全件参照)
@app.route('/yumesuzu', methods=["GET"])
def getAll():
    data = test.query.all()
    return jsonify(test_schema.dump(data))


#GET(1件参照)
@app.route('/yumesuzu/<int:id>', methods=["GET"])
def get(id):
    
    data = test.query.filter_by(id=id).all() 
    return jsonify(test_schema.dump(data))

#POST(登録)
@app.route('/yumesuzu', methods=["POST"])
def post():
    entry = test()
    # jsonリクエストから値取得
    json = request.get_json()
    if type(json) == list:
        data = json[0]
    else:
        data = json
    entry.date = data["date"]
    entry.time = data["time"]
    db.session.add(entry)
    db.session.commit()
    db.session.close()

    latestdata= test.query.test_by(desc(test.id)).first()   
    return redirect('/yumesuzu/' + str(latestdata.id))

