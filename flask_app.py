"""
Put your Flask app code here.
"""

from flask import Flask, request, render_template
app = Flask(__name__)
#Make an app.route() decorator here
@app.route("/initial/", methods = ['GET', 'POST'])
def initialFunction():
    if request.method == 'GET':
  		#Display the form
        return render_template('flask_app.html')

    elif request.method == 'POST':
    	#check if the input fields are completed
    	if request.form['firstname'] == '' and request.form['lastname'] == '' and request.form['ninja_softdes'] == '':
    		error = 'Invalid username/password'
    		#if not then direct to page with error message
    		return render_template('error.html', error=error)
    	else:
    		first_name = request.form['firstname']
    		last_name = request.form['lastname']
    		#if yes then direct to profile page with message
    		return render_template('profile.html', firstname=first_name, 
    			lastname = last_name, ninja = 'Patrick Huston')
    		

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
