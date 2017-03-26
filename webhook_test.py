import urllib
import json
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import make_response

app = Flask(__name__)
app.config['DEBUG'] = True

# Import db for flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///progLang_ques.db'

db = SQLAlchemy(app)

class progLang(db.Model):
    __tablename__ = 'ProgrammingLanguageQuestions'

    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(20))
    language_question = db.Column(db.String(256))

try:
    progLang.query.all()
except Exception as e:
    print "Error:\n",e
    sys.exit(1)

# Make webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    resp = makeWebHookeResult(req)
    resp = json.dumps(resp, indent=4)
    flresp = make_response(resp)
    flresp.headers['Content-Type'] = 'application/json'
    print "Response:"
    print flresp.data
    return flresp


def makeWebHookeResult(req):
    '''
    Refer https://docs.api.ai/docs/query for more info
    on response fields

    Action name == progLang.ques
    '''
    if req.get("result").get("action") != "progLang.ques":
        return {}

    result = req.get("result")
    parameters= result.get("parameters")
    language = parameters.get("progLang") # Get entity value for progLang   
    if language=="python":
        selectLang = progLang.query.filter_by(language_name="python")
        selectLang = [i.language_question for i in selectLang]
    else:
        selectLang = progLang.query.filter_by(language_name="C++")
        selectLang = [i.language_question for i in selectLang]

    speech = selectLang[0]
    #print("Response:")
    #print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-progLang-ques"
    }




if __name__ == '__main__':
   port  = int(os.getenv('PORT', 5000))
   print "Starting app on port {}".format(port)

   app.run(debug=True, port=port, host='0.0.0.0')
