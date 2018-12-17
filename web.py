from flask import Flask, url_for, render_template, request
import json

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
		return getKeys(query = q[0].strip(), minus_words=minus_words)
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Ошибка 404. Страница не найдена"
