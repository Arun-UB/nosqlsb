from flask import Flask
from flask import Response, request, render_template, redirect, url_for, flash, jsonify
import sh
app = Flask(__name__)


# def ycsb():
# 	# sh.fab("-H","ubuntu@ec2-174-129-80-204.compute-1.amazonaws.com","-i","/home/arun/nosqlsb.pem","host_type");
# 	# sh.fab("")
# 	#return "hello_world"+print(sh.fab("-H","1PI09IS020@119.82.126.182","host_type"));
# 	error = None
#     if request.method == 'POST':
#         return (request.form['recordcount'])
#     else:
#         error = 'Invalid username/password'

# 	return render_template('index.html')

@app.route('/',methods=['POST', 'GET'])

def ycsb():
    error = None
    if request.method == 'POST':
    	#msg=sh.fab("-H","ubuntu@ec2-174-129-80-204.compute-1.amazonaws.com`","-i","/home/arun/nosqlsb.pem","host_type");

        sh.fab("ycsb:workload="+request.form['workload']+',recordcount='+request.form['recordcount']+',voldemort='+request.form['voldemort'])
	flash('Done'+request.form['voldemort'])
	return render_template('index.html')

    else:
        error = 'Invalid username/password'
    
    return render_template('index.html')

if __name__ == '__main__':
	app.debug=True
	app.secret_key="i want this sem to get over"	
	app.run(port=8000,host='0.0.0.0')
