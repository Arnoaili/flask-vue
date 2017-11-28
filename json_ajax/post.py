#! -*- coding:utf-8 -*-

from flask import Flask, jsonify, render_template, request, make_response
import json
import MySQLdb

app = Flask(__name__)
db = MySQLdb.connect(host="localhost",user="root",passwd="admin1",db="myaoo",charset="utf8")
cursor = db.cursor()

@app.route('/', methods=['POST', 'GET'])
def function():
	return render_template('http-get.html')

@app.route('/post', methods=['POST', 'GET'])
def function2():
	return render_template('http-post.html')

@app.route('/pp', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		#n = [request.form.get(x, 0, type=float) for x in {'n1','n2','n3','n4'}]
		n=[]
		for x in {'n1','n2','n3','n4'}:
			n.append(float(request.form[x]))
		return jsonify(max=max(n), min=min(n), sum=max(n)+min(n), name=request.form["name"])#前端一般接受字符串，所以用jsonify將字典換成字符串
	else:
		return render_template('index_post.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
	if request.method == 'POST':
		# 接受前端发来的数据
		data = json.loads(request.form.get('data'))

		# lesson: "Operation System"
		# score: 100
		lesson = data["lesson"]
		score = data["score"]

		# 自己在本地组装成Json格式,用到了flask的jsonify方法
		info = dict()
		info['name'] = "pengshuang"
		info['lesson'] = lesson
		info['score'] = score
		return jsonify(info)

	return render_template('ajax.html')

@app.route('/tt', methods=['POST', 'GET'])
def func():
	info = dict()
	info['id'] = 1
	info['author'] = "lesson"
	info['name'] = "score"
	info['price'] = 32
	print "IOHOSVHOH"
	print list(info)
	aa= []
	aa.append(info)
	# response = make_response(jsonify(info))
	response = make_response(jsonify(aa))
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'POST'
	response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
	return response

@app.route('/tes', methods=['GET', 'POST'])
def tes():
	if request.method == 'POST' and request.json:
		id = int(request.json["customerId"])
		name = request.json["companyName"]
		password = request.json["contactName"]
		message_id = int(request.json["phone"])
		sql = "insert into blog_user(id,name,password,message_id) values('%d','%s','%s','%d')" % (id,name,password,message_id)
		cursor.execute(sql)
		db.commit()
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
	# info = dict()
	# info['customerId'] = 112223
	# info['companyName'] = "11223"
	# info['contactName'] = "1122"
	# info['phone'] = 1122233434
	# aa= []
	# aa.append(info)
	print "**********", aa

	# 	print "DDDDDDDDDDDDD"
	# 	print aa
	# 	info['customerId'] = ""
	# 	info['companyName'] = request.json['companyName']
	# 	info['contactName'] = request.json['contactName']
	# 	info['phone'] = request.json['phone']
	# 	aa.append(info)
	# 	print aa
	# 	response = make_response(jsonify(aa))
	# 	return response

	response = make_response(jsonify(aa))
	# response.headers['Access-Control-Allow-Origin'] = '*'
	# response.headers['Access-Control-Allow-Methods'] = 'POST'
	# response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
	return jsonify(aa)
# @app.route('/tes', methods=['POST'])
# def oo():
# 	if request.json:
# 		info = {}
# 		aa = []
# 		info['customerId'] = ""
# 		info['companyName'] = request.json['companyName']
# 		info['contactName'] = request.json['contactName']
# 		info['phone'] = request.json['phone']
# 		aa.append(info)
# 		response = make_response(jsonify(aa))
# 		cursor.execute("insert into blog_user('id','name','password','update_time','create_time','message_id') values(2,'王林','123qwe','2017-07-03','2017-07-04','3')")
# 		db.commit()
# 		return response

if __name__ == '__main__':
	app.run(debug=True)
