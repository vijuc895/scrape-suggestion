from flask import Flask ,render_template,request,jsonify
from flask_restful import Resource, Api
from json import dumps
import requests, json

app = Flask(__name__)
api = Api(app)

class Suggestion(Resource):
    def get(self, text):
        URL="https://in.pinterest.com/resource/AdvancedTypeaheadResource/get/?source_url=%2F&data=%7B%22options%22%3A%7B%22count%22%3A5%2C%22pin_scope%22%3A%22pins%22%2C%22term%22%3A%22" +text+ "%22%7D%2C%22context%22%3A%7B%7D%7D"
        headers = {'User-agent':'Mozilla/5.0'}

        response = requests.get(URL, headers=headers)
        result = json.loads(response.content.decode('utf-8'))
        li =[]
        for i in result["resource_response"]["data"]["items"]:
            try:
                li.append(i["query"])
            except:
                break
        result = {'data': li}
        return jsonify(result)


api.add_resource(Suggestion, '/<text>') # Route_3
if __name__ == '__main__':
     app.run(port='5002')