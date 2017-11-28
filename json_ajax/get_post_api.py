#! -*- coding:utf-8 -*-

from flask import Flask, jsonify, render_template, request, make_response
import json
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",user="root",passwd="admin1",db="myaoo",charset="utf8")
cursor = db.cursor()

@app.route('/', methods=['GET'])
def get():
	return render_template('http-get.html')

@app.route('/post', methods=['GET','POST'])
def post():
	return render_template('http-post.html')

@app.route('/delete', methods=['GET','POST'])
def delete():
	return render_template('http-delete.html')

@app.route('/put', methods=['GET','POST'])
def put():
	return render_template('http-put.html')

# 获取数据
@app.route('/resource', methods=['GET', 'POST'])
def resource():
	cursor.execute("select *from blog_user")
	data = cursor.fetchall()
	aa = []
	for one in data:
		info = dict()
		info['customerId'] = one[0]
		info['companyName'] = one[1]
		info['contactName'] = one[2]
		info['phone'] = one[3]
		aa.append(info)
	return jsonify(aa)

# 插入数据
@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST' and request.json:
		id = int(request.json["customerId"])
		name = request.json["companyName"]
		password = request.json["contactName"]
		message_id = int(request.json["phone"])
		sql = "insert into blog_user(id,name,password,message_id) values('%d','%s','%s','%d')" % (id,name,password,message_id)
		cursor.execute(sql)
		db.commit()
	return jsonify({})

# 删除数据
@app.route('/del', methods=['GET', 'POST'])
def dele():
	if request.method == 'POST' and request.json:
		id = int(request.json["customerId"])
		sql = "delete from blog_user where id=%s" % id
		cursor.execute(sql)
		db.commit()
	return jsonify({})

# 更新数据
@app.route('/update', methods=['GET', 'POST'])
def update():
	if request.method == 'POST' and request.json:
		id = int(request.json["customerId"])
		message_id = int(request.json["phone"])
		sql = "update blog_user set message_id=%d where id=%d" % (message_id, id)
		cursor.execute(sql)
		db.commit()
	return jsonify({})

if __name__ == '__main__':
	app.run(debug=True)
