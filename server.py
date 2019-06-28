from flask import *
import uuid
import subprocess

app = Flask (__name__)

def check_json (id):
    try:
        with open (id + ".json") as ouf:
            task = json.load (ouf)
    except:
        return {"status" : "not exists"}
    status = task ['status']
    if status == "running":
        return {"status" : "running"}
    elif status == "failed":
        return {"status" : "failed"}
    else:
        md5 = task ['md5']
        url = task ['url']
        return {"md5" : md5, "status" : "done", "url" : url}

@app.route('/submit', methods=['POST'])
def create_task ():
    url = request.form ['url']
    id = str (uuid.uuid4 ())
    try:
        email = request.form ['email']
        subprocess.Popen (["python3", "application.py", str(id), str(url), str(email)])
    except:
        subprocess.Popen (["python3", "application.py", str(id), str(url)])
    return jsonify ({'id' : id})

@app.route('/check', methods=['GET'])
def get_task ():
    id = request.args.get ('id')
    return jsonify (check_json (id))

if __name__ == '__main__':
    app.run (port="8000", debug=True)
