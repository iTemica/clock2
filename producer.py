from flask import Flask, render_template,request,redirect,json
from datetime import datetime
import os
import pika

app = Flask(__name__,
            template_folder='/home/comp/clock2/assets/templates/',
            static_folder='/home/comp/clock2/assets/static/')

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/text',methods=['POST'])
def text():
	data = request.form
	try:
		data["mgs"].encode('ascii')
	except Exception:
		return redirect('/')
	os.system ("sudo -E /home/comp/clock2/scripts/display_msg \"" + data["mgs"] + '"')
	return redirect('/')

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=9001)
