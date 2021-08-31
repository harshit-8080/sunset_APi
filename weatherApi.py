from flask import Flask, jsonify
import requests
app= Flask(__name__)

@app.route('/')
def homePage():

    data={
        "Description": "This is simple home page"
    }
    return jsonify(data)


@app.route('/sunset')
def sunset():
    response= requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")

    return response.json()

if __name__=="__main__":
    app.run(debug=True)