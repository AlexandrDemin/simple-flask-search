from flask import Flask, url_for, render_template, request
import json
import datetime

app = Flask(__name__)

def getKeys(query = "", minus_words = []):
	if query == "":
		return json.dumps([])
	else:
		return json.dumps([query] + minus_words + list(range(0, 170)))

@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		try:
			q = request.get_json()['q']
			q = q.split(" -")
		except:
			q = ""
		minus_words = []
		if len(q)>1:
			ms = q[1:]
			for m in ms:
				minus_words.append(m.strip())
		query = q[0].strip()
		keys = getKeys(query = query, minus_words=minus_words)
		with open("log.txt", "a") as logFile:
			logEntry = {
				"timestamp": datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
				"requestQuery": query,
				"requestQuery": minus_words,
				"keysCount": len(keys),
				"keys": keys
			}
			logFile.write(json.dumps(logEntry)+'\n')
		return keys
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Ошибка 404. Страница не найдена"
