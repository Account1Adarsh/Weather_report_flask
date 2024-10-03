from flask import Flask, request, render_template

# import json to load jason data to python dictionary
import json

# import urllib.request to make request to api
import urllib.request


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def weather():
    city = "patna"
    if request.method == "POST":
        city = request.form.get("city")

        
    api = "6d0b3c7043917d21c801b66eaefdc9c7"
    
    try:
        source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api).read()
        
        list_data = json.loads(source)

        data = {
            "country_code": str(list_data['sys']['country']),
            "city": city,
            "temperature": str(list_data['main']['temp'])+"K",
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
        }
    except Exception as e:
        data = {"error": str(e)}
    print(data)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
