from flask import Flask, render_template,request,redirect,json
from time import sleep
from datetime import datetime
import os
from shlex import quote
import pika

app = Flask(__name__)
template_dir = os.path.abspath('/home/comp/clock2/assets/templates/')
@app.route('/')
def main():
	return render_template('index.html', template_folder=template_dir)

@app.route('/text',methods=['POST'])
def text():
	data = request.form
	try:
		data["mgs"].encode('ascii')
	except Exception:
		return redirect('/')
	text_to_display = '{}'.format(quote(data))
	os.system ("sudo -E ./display_msg \"" + text_to_display + '"')
	return redirect('/')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="9001")