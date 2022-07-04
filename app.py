from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler
from get_dummy import *

app = Flask(__name__)
model = pickle.load(open("gboost.pkl", "rb"))
crop_years = [2014, 2015, 2016, 2017, 2018, 2019, 2022, 2021, 2022, 2023, 2024, 2025, 2026]
district_names = ['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR',
                  'MUMBAI', 'NAGPUR', 'NANDED', 'NANDURBAR', 'NASHIK', 'OSMANABAD', 'PALGHAR', 'PARBHANI', 'PUNE', 'RAIGAD', 'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL']
crop_names = ['Maize', 'Arhar/Tur', 'Bajra', 'Gram', 'Jowar', 'Moong(Green Gram)', 'Pulses total', 'Ragi', 'Rice', 'Sugarcane', 'Total foodgrain', 'Urad', 'Other  Rabi pulses', 'Wheat', 'Cotton(lint)', 'Castor seed', 'Groundnut', 'Niger seed',
              'Other Cereals & Millets', 'Other Kharif pulses', 'Sesamum', 'Soyabean', 'Sunflower', 'Linseed', 'Safflower', 'Small millets', 'Rapeseed &Mustard', 'other oilseeds', 'Banana', 'Grapes', 'Mango', 'Onion', 'Tomato', 'Tobacco']

soil_types = ['loamy', 'sandy', 'clay', 'chalky', 'peaty', 'silty', 'silt']

@app.route('/', methods=['GET'])
def Home():
    return render_template('index2.html',
                           crop_years=crop_years,
                           district_names=district_names,
                           soil_types=soil_types,
                           crop_names=crop_names)


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        crop_year = int(request.form['cyear'])
        district_name = request.form["dname"]
        crop_name = request.form["cname"]
        soil_type = request.form['stype']  
        pressure = float(request.form.get("pressure"))
        wind_speed = float(request.form.get("wind"))
        temperature = float(request.form.get("temp"))

        input_=[crop_year, pressure, wind_speed, temperature] + get_district_name(district_name) + get_crop_name(crop_name) + get_soil_type(soil_type)  
        output=list(model.predict([input_]))
        return render_template('index2.html', prediction_text="Crop Yield will be {} per hectare 👨‍🌾".format(output[0]),                           crop_years=crop_years,
                               district_names=district_names,
                               soil_types=soil_types,
                               crop_names=crop_names)
   

if __name__ == "__main__":
    app.run(debug=True)
