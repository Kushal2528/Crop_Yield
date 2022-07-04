def get_district_name(s):
    dn = ['district_names_AHMEDNAGAR_sqrt', 'district_names_AKOLA_sqrt', 'district_names_AMRAVATI_sqrt', 'district_names_AURANGABAD_sqrt', 'district_names_BEED_sqrt', 'district_names_BHANDARA_sqrt', 'district_names_BULDHANA_sqrt', 'district_names_CHANDRAPUR_sqrt', 'district_names_DHULE_sqrt', 'district_names_GADCHIROLI_sqrt', 'district_names_GONDIA_sqrt', 'district_names_HINGOLI_sqrt', 'district_names_JALGAON_sqrt', 'district_names_JALNA_sqrt', 'district_names_KOLHAPUR_sqrt', 'district_names_LATUR_sqrt', 'district_names_MUMBAI_sqrt',
          'district_names_NAGPUR_sqrt', 'district_names_NANDED_sqrt', 'district_names_NANDURBAR_sqrt', 'district_names_NASHIK_sqrt', 'district_names_OSMANABAD_sqrt', 'district_names_PALGHAR_sqrt', 'district_names_PARBHANI_sqrt', 'district_names_PUNE_sqrt', 'district_names_RAIGAD_sqrt', 'district_names_RATNAGIRI_sqrt', 'district_names_SANGLI_sqrt', 'district_names_SATARA_sqrt', 'district_names_SINDHUDURG_sqrt', 'district_names_SOLAPUR_sqrt', 'district_names_THANE_sqrt', 'district_names_WARDHA_sqrt', 'district_names_WASHIM_sqrt', 'district_names_YAVATMAL_sqrt']
    res = [idx for idx, value in enumerate(dn) if s in value]
    if len(res) == 0:
        return "Invalid district name"
    else:
        at_idx = res[0]
    ret = [0]*len(dn)
    ret[at_idx] = 1
    return ret


def get_crop_name(s):
    cn = ['crop_names_Arhar/Tur_sqrt', 'crop_names_Bajra_sqrt', 'crop_names_Banana_sqrt', 'crop_names_Castor seed_sqrt', 'crop_names_Cotton(lint)_sqrt', 'crop_names_Gram_sqrt', 'crop_names_Grapes_sqrt', 'crop_names_Groundnut_sqrt', 'crop_names_Jowar_sqrt', 'crop_names_Linseed_sqrt', 'crop_names_Maize_sqrt', 'crop_names_Mango_sqrt', 'crop_names_Moong(Green Gram)_sqrt', 'crop_names_Niger seed_sqrt', 'crop_names_Onion_sqrt', 'crop_names_Other  Rabi pulses_sqrt', 'crop_names_Other Cereals & Millets_sqrt', 'crop_names_Other Kharif pulses_sqrt', 'crop_names_Pulses total_sqrt', 'crop_names_Ragi_sqrt', 'crop_names_Rapeseed &Mustard_sqrt', 'crop_names_Rice_sqrt', 'crop_names_Safflower_sqrt', 'crop_names_Sesamum_sqrt', 'crop_names_Small millets_sqrt', 'crop_names_Soyabean_sqrt', 'crop_names_Sugarcane_sqrt', 'crop_names_Sunflower_sqrt', 'crop_names_Tobacco_sqrt', 'crop_names_Tomato_sqrt', 'crop_names_Total foodgrain_sqrt', 'crop_names_Urad_sqrt', 'crop_names_Wheat_sqrt', 'crop_names_other oilseeds_sqrt']
    res = [idx for idx, value in enumerate(cn) if s in value]
    if len(res) == 0:
        return "Invalid crop name"
    else:
        at_idx = res[0]
    ret = [0]*len(cn)
    ret[at_idx] = 1
    return ret


def get_soil_type(s):
    st = ['soil_type_chalky_sqrt', 'soil_type_clay_sqrt', 'soil_type_loamy_sqrt',
          'soil_type_peaty_sqrt', 'soil_type_sandy_sqrt', 'soil_type_silt_sqrt', 'soil_type_silty_sqrt']
    res = [idx for idx, value in enumerate(st) if s in value]
    if len(res) == 0:
        return "Invalid soil type"
    else:
        at_idx = res[0]
    ret = [0]*len(st)
    ret[at_idx] = 1
    return ret