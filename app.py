from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open("Green_Pro/gboost.pkl", "rb"))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index2.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    district_names_AHMEDNAGAR = 0
    temperature = 0
    district_names_AKOLA = 0
    district_names_AMRAVATI = 0
    district_names_AURANGABAD = 0
    district_names_BEED = 0
    district_names_BHANDARA = 0
    district_names_BULDHANA = 0
    district_names_CHANDRAPUR = 0
    district_names_DHULE = 0
    district_names_GADCHIROLI = 0
    district_names_GONDIA = 0
    district_names_HINGOLI = 0
    district_names_JALGAON = 0
    district_names_JALNA = 0
    district_names_KOLHAPUR = 0
    district_names_LATUR = 0
    district_names_MUMBAI = 0
    district_names_NAGPUR = 0
    district_names_NANDED = 0
    district_names_NANDURBAR = 0
    district_names_NASHIK = 0
    district_names_OSMANABAD = 0
    district_names_PALGHAR = 0
    district_names_PARBHANI = 0
    district_names_PUNE = 0
    district_names_RAIGAD = 0
    district_names_RATNAGIRI = 0
    district_names_SANGLI = 0
    district_names_SATARA = 0
    district_names_SINDHUDURGH = 0
    district_names_SOLAPUR = 0
    district_names_THANE = 0
    district_names_WARDHA = 0
    district_names_WASHIM = 0
    district_names_YAVATMAL = 0
    crop_names_Arhar = 0
    crop_names_Bajra = 0
    crop_names_Banana = 0
    crop_names_CastorSeed = 0
    crop_names_Cotton = 0
    crop_names_Gram = 0
    crop_names_Grapes = 0
    crop_names_Groundnut = 0
    crop_names_Jowar = 0
    crop_names_Linseed = 0
    crop_names_Maize = 0
    crop_names_Mango = 0
    crop_names_Moong = 0
    crop_names_Niger = 0
    crop_names_Onion = 0
    crop_names_OtherRabi = 0
    crop_names_OtherCereals = 0
    crop_names_OtherKharif = 0
    crop_names_PulsesTotal = 0
    crop_names_Ragi = 0
    crop_names_Rapeseed = 0
    crop_names_Rice = 0
    crop_names_Safflolwer = 0
    crop_names_Sesamum = 0
    crop_names_SmallMillets = 0
    crop_names_Soyabean = 0
    crop_names_Sugarcane = 0
    crop_names_Sunflower = 0
    crop_names_Tobacco = 0
    crop_names_Tomato = 0
    crop_names_TotalFoodGrain = 0
    crop_names_Urad = 0
    crop_names_Wheat = 0
    crop_names_OtherOilSeeds = 0
    soil_type_chalky = 0
    soil_type_clay = 0
    soil_type_loamy = 0
    soil_type_peaty = 0
    soil_type_sandy = 0
    soil_type_silt = 0
    soil_type_silty = 0
    crop_year = 0
    pressure = 0
    wind_speed = 0
    humidity = 0

    if request.method == 'POST':
        district_names = request.form['district_names']
        if(district_names == 'AHMEDNAGAR'):
            district_names_AHMEDNAGAR = 1
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        temperature = float(request.form['temperature'])
        if(district_names == 'AKOLA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 1
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'AMRAVATI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 1
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'AURANGABAD'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 1
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'BEED'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 1
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'BHANDARA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 1
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'BULDHANA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 1
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'CHANDRAPUR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 1
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'DHULE'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 1
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'GADCHIROLI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 1
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'GONDIA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 1
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'HINGOLI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 1
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'JALGAON'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 1
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'JALNA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 1
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'KOLHAPUR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 1
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'LATUR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 1
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'MUMBAI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 1
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'NAGPUR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 1
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'NANDED'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 1
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'NANDURBAR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 1
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'NASHIK'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 1
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'OSMANABAD'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 1
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'PALGHAR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 1
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'PARBHANI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 1
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'PUNE'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 1
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'RAIGAD'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 1
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'RATNAGIRI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 1
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'SANGLI'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 1
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'SATARA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 1
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'SINDHUDURGH'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 1
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'SOLAPUR'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 1
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'THANE'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 1
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'WARDHA'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 1
            district_names_WASHIM = 0
            district_names_YAVATMAL = 0
        elif(district_names == 'WASHIM'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 1
            district_names_YAVATMAL = 0
        elif(district_names == 'YAVATMAL'):
            district_names_AHMEDNAGAR = 0
            district_names_AKOLA = 0
            district_names_AMRAVATI = 0
            district_names_AURANGABAD = 0
            district_names_BEED = 0
            district_names_BHANDARA = 0
            district_names_BULDHANA = 0
            district_names_CHANDRAPUR = 0
            district_names_DHULE = 0
            district_names_GADCHIROLI = 0
            district_names_GONDIA = 0
            district_names_HINGOLI = 0
            district_names_JALGAON = 0
            district_names_JALNA = 0
            district_names_KOLHAPUR = 0
            district_names_LATUR = 0
            district_names_MUMBAI = 0
            district_names_NAGPUR = 0
            district_names_NANDED = 0
            district_names_NANDURBAR = 0
            district_names_NASHIK = 0
            district_names_OSMANABAD = 0
            district_names_PALGHAR = 0
            district_names_PARBHANI = 0
            district_names_PUNE = 0
            district_names_RAIGAD = 0
            district_names_RATNAGIRI = 0
            district_names_SANGLI = 0
            district_names_SATARA = 0
            district_names_SINDHUDURGH = 0
            district_names_SOLAPUR = 0
            district_names_THANE = 0
            district_names_WARDHA = 0
            district_names_WASHIM = 0
            district_names_YAVATMAL = 1
        crop_names = request.form['crop_names']
        if(crop_names == 'Arhar/Tur'):
            crop_names_Arhar = 1
            crop_names_Bajra = 0
            crop_names_Banana = 0
            crop_names_CastorSeed = 0
            crop_names_Cotton = 0
            crop_names_Gram = 0
            crop_names_Grapes = 0
            crop_names_Groundnut = 0
            crop_names_Jowar = 0
            crop_names_Linseed = 0
            crop_names_Mango = 0
            crop_names_Moong = 0
            crop_names_Niger = 0
            crop_names_Onion = 0
            crop_names_OtherRabi = 0
            crop_names_OtherCereals = 0
            crop_names_OtherKharif = 0
            crop_names_PulsesTotal = 0
            crop_names_Ragi = 0
            crop_names_Rapeseed = 0
            crop_names_Rice = 0
            crop_names_Safflolwer = 0
            crop_names_Sesamum = 0
            crop_names_SmallMillets = 0
            crop_names_Soyabean = 0
            crop_names_Sugarcane = 0
            crop_names_Sunflower = 0
            crop_names_Tobacco = 0
            crop_names_Tomato = 0
            crop_names_TotalFoodGrain = 0
            crop_names_Urad = 0
            crop_names_Wheat = 0
            crop_names_OtherOilSeeds = 0
        elif(crop_names == 'Bajra'):
            crop_names_Arhar = 0
            crop_names_Bajra = 1
            crop_names_Banana = 0
            crop_names_CastorSeed = 0
            crop_names_Cotton = 0
            crop_names_Gram = 0
            crop_names_Grapes = 0
            crop_names_Groundnut = 0
            crop_names_Jowar = 0
            crop_names_Linseed = 0
            crop_names_Mango = 0
            crop_names_Moong = 0
            crop_names_Niger = 0
            crop_names_Onion = 0
            crop_names_OtherRabi = 0
            crop_names_OtherCereals = 0
            crop_names_OtherKharif = 0
            crop_names_PulsesTotal = 0
            crop_names_Ragi = 0
            crop_names_Rapeseed = 0
            crop_names_Rice = 0
            crop_names_Safflolwer = 0
            crop_names_Sesamum = 0
            crop_names_SmallMillets = 0
            crop_names_Soyabean = 0
            crop_names_Sugarcane = 0
            crop_names_Sunflower = 0
            crop_names_Tobacco = 0
            crop_names_Tomato = 0
            crop_names_TotalFoodGrain = 0
            crop_names_Urad = 0
            crop_names_Wheat = 0
            crop_names_OtherOilSeeds = 0

        elif(crop_names == 'Banana'):
            crop_names_Arhar = 0
            crop_names_Bajra = 0
            crop_names_Banana = 1
            crop_names_CastorSeed = 0
            crop_names_Cotton = 0
            crop_names_Gram = 0
            crop_names_Grapes = 0
            crop_names_Groundnut = 0
            crop_names_Jowar = 0
            crop_names_Linseed = 0
            crop_names_Mango = 0
            crop_names_Moong = 0
            crop_names_Niger = 0
            crop_names_Onion = 0
            crop_names_OtherRabi = 0
            crop_names_OtherCereals = 0
            crop_names_OtherKharif = 0
            crop_names_PulsesTotal = 0
            crop_names_Ragi = 0
            crop_names_Rapeseed = 0
            crop_names_Rice = 0
            crop_names_Safflolwer = 0
            crop_names_Sesamum = 0
            crop_names_SmallMillets = 0
            crop_names_Soyabean = 0
            crop_names_Sugarcane = 0
            crop_names_Sunflower = 0
            crop_names_Tobacco = 0
            crop_names_Tomato = 0
            crop_names_TotalFoodGrain = 0
            crop_names_Urad = 0
            crop_names_Wheat = 0
            crop_names_OtherOilSeeds = 0

        elif(crop_names == 'Castor Seed'):
            crop_names_Arhar = 0
            crop_names_Bajra = 0
            crop_names_Banana = 0
            crop_names_CastorSeed = 1
            crop_names_Cotton = 0
            crop_names_Gram = 0
            crop_names_Grapes = 0
            crop_names_Groundnut = 0
            crop_names_Jowar = 0
            crop_names_Linseed = 0
            crop_names_Mango = 0
            crop_names_Moong = 0
            crop_names_Niger = 0
            crop_names_Onion = 0
            crop_names_OtherRabi = 0
            crop_names_OtherCereals = 0
            crop_names_OtherKharif = 0
            crop_names_PulsesTotal = 0
            crop_names_Ragi = 0
            crop_names_Rapeseed = 0
            crop_names_Rice = 0
            crop_names_Safflolwer = 0
            crop_names_Sesamum = 0
            crop_names_SmallMillets = 0
            crop_names_Soyabean = 0
            crop_names_Sugarcane = 0
            crop_names_Sunflower = 0
            crop_names_Tobacco = 0
            crop_names_Tomato = 0
            crop_names_TotalFoodGrain = 0
            crop_names_Urad = 0
            crop_names_Wheat = 0
            crop_names_OtherOilSeeds = 0
        soil_type = request.form['soil_type']
        if(soil_type == 'chalky'):
            soil_type_chalky = 1
            soil_type_loamy = 0
            soil_type_peaty = 0
            soil_type_sandy = 0
            soil_type_silt = 0
            soil_type_silty = 0

        elif(soil_type == 'loamy'):
            soil_type_chalky = 0
            soil_type_loamy = 1
            soil_type_peaty = 0
            soil_type_sandy = 0
            soil_type_silt = 0
            soil_type_silty = 0

        elif(soil_type == 'peaty'):
            soil_type_chalky = 0
            soil_type_loamy = 0
            soil_type_peaty = 1
            soil_type_sandy = 0
            soil_type_silt = 0
            soil_type_silty = 0

        elif(soil_type == 'sandy'):
            soil_type_chalky = 0
            soil_type_loamy = 0
            soil_type_peaty = 0
            soil_type_sandy = 1
            soil_type_silt = 0
            soil_type_silty = 0

        elif(soil_type == 'silt'):
            soil_type_chalky = 0
            soil_type_loamy = 0
            soil_type_peaty = 0
            soil_type_sandy = 0
            soil_type_silt = 1
            soil_type_silty = 0

        elif(soil_type == "silty"):
            soil_type_chalky = 0
            soil_type_loamy = 0
            soil_type_peaty = 0
            soil_type_sandy = 0
            soil_type_silt = 0
            soil_type_silty = 1

        # Temperature=float(request.form['temperature'])
        wind_speed = float(request.form['wind_speed'])
        # NitrogenContent=float(request.form['N'])
        crop_year = int(request.form['crop_year'])
        # humidity=float(request.form['humidity'])
        pressure = float(request.form['pressure'])

        prediction = model.predict(([[
            crop_year,
            pressure,
            wind_speed,
            temperature,
            district_names_AHMEDNAGAR,
            district_names_AKOLA,
            district_names_AMRAVATI,
            district_names_AURANGABAD,
            district_names_BEED,
            district_names_BHANDARA,
            district_names_BULDHANA,
            district_names_CHANDRAPUR,
            district_names_DHULE,
            district_names_GADCHIROLI,
            district_names_GONDIA,
            district_names_HINGOLI,
            district_names_JALGAON,
            district_names_JALNA,
            district_names_KOLHAPUR,
            district_names_LATUR,
            district_names_MUMBAI,
            district_names_NAGPUR,
            district_names_NANDED,
            district_names_NANDURBAR,
            district_names_NASHIK,
            district_names_OSMANABAD,
            district_names_PALGHAR,
            district_names_PARBHANI,
            district_names_PUNE,
            district_names_RAIGAD,
            district_names_RATNAGIRI,
            district_names_SANGLI,
            district_names_SATARA,
            district_names_SINDHUDURGH,
            district_names_SOLAPUR,
            district_names_THANE,
            district_names_WARDHA,
            district_names_WASHIM,
            district_names_YAVATMAL,
            crop_names_Arhar,
            crop_names_Bajra,
            crop_names_Banana,
            crop_names_CastorSeed,
            crop_names_Cotton,
            crop_names_Gram,
            crop_names_Grapes,
            crop_names_Groundnut,
            crop_names_Jowar,
            crop_names_Linseed,
            crop_names_Maize,
            crop_names_Mango,
            crop_names_Moong,
            crop_names_Niger,
            crop_names_Onion,
            crop_names_OtherRabi,
            crop_names_OtherCereals,
            crop_names_OtherKharif,
            crop_names_PulsesTotal,
            crop_names_Ragi,
            crop_names_Rapeseed,
            crop_names_Rice,
            crop_names_Safflolwer,
            crop_names_Sesamum,
            crop_names_SmallMillets,
            crop_names_Soyabean,
            crop_names_Sugarcane,
            crop_names_Sunflower,
            crop_names_Tobacco,
            crop_names_Tomato,
            crop_names_TotalFoodGrain,
            crop_names_Urad,
            crop_names_Wheat,
            crop_names_OtherOilSeeds,
            soil_type_chalky,
            soil_type_clay,
            soil_type_loamy,
            soil_type_peaty,
            soil_type_sandy,
            soil_type_silt,
            soil_type_silty

        ]]))

        # inp = [2010.0,
        #         31.83012454242965,
        #         1.4484933784637755,
        #         4.592304008894227,
        #         1.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         1.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         0.0,
        #         1.0,
        #         0.0,
        #         0.0,
        #         0.0]

        # prediction=model.predict([inp]);

        output = round(prediction[0], 2)
        if output < 0:
            return render_template('index2.html', prediction_texts="Oh ho! 😞 No prediction for the given input, try again!")
        else:
            return render_template('index2.html', prediction_text="Crop Yield will be {} per hectare 👨‍🌾".format(output))
    else:
        return render_template('index2.html')


if __name__ == "__main__":
    app.run(debug=True)
