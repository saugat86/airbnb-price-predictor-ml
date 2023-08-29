from unittest import result
from flask import jsonify, request, abort, Flask
import pandas as pd
import re
import numpy as np
import haversine as hs
import pickle
import xgboost as xgb


def main(features):
    ### import controller
    dataset = pd.DataFrame([features], columns=features.keys())
    df = property_prep(dataset)
    df = bathrooms_prep(df)
    df = reviews_per_month_prep(df)
    df = beds_prep(df)
    df = spatial_data_prep(df)
    df = license_prep(df)

    df['host_is_superhost'] = df['host_is_superhost'].str.replace('t', '1')
    df['host_is_superhost'] = df['host_is_superhost'].str.replace('f', '0')

    df['host_has_profile_pic'] = df['host_has_profile_pic'].str.replace(
        't', '1')
    df['host_has_profile_pic'] = df['host_has_profile_pic'].str.replace(
        'f', '0')

    df['host_identity_verified'] = df['host_identity_verified'].str.replace(
        't', '1')
    df['host_identity_verified'] = df['host_identity_verified'].str.replace(
        'f', '0')

    df['has_availability'] = df['has_availability'].str.replace('t', '1')
    df['has_availability'] = df['has_availability'].str.replace('f', '0')

    df['instant_bookable'] = df['instant_bookable'].str.replace('t', '1')
    df['instant_bookable'] = df['instant_bookable'].str.replace('f', '0')

    df = df.drop('latitude', axis=1)
    df = df.drop('longitude', axis=1)
    df = dummies(df)

    # call this function only if scaling is needed in all features.
    # df=featureScalingAll(df)

    # To be implemented. Call this function if only numeric features are scaled.
    # df = featuresPartialScaling(df)

    # xgboost model
    # m = xgb.Booster()
    # m.load_model('repo/model')

    m = pickle.load(open('repo/rf_model', 'rb'))
    prediction = m.predict(df)

    value_to_return = np.power(prediction, 2.7183)

    return str(round(value_to_return[0], 2))


def property_prep(data):
    property_mapping = {"Entire rental unit": "house", "Entire condominium (condo)": "house", "Private room in rental unit": "room", "Entire residential home": "house", "loft": "house", "Room in hotel": "room", "Entire serviced apartment": "house", "Room in aparthotel": "room", "Room in boutique hotel": "room", "Private room in condominium (condo)": "room",
                        "Private room in bed and breakfast":  "room", "Room in serviced apartment": "room", "Private room in residential home": "room", "Shared room in hostel": "room", "Private room in serviced apartment": "room", "Shared room in rental unit": "room",
                        "Entire townhouse": "house", "Entire guest suite": "house", "Entire villa": "house", "Shared room in residential home": "room", "Private room in townhouse": "room", "Private room in hostel": "room", "Room in bed and breakfast": "room", "Private room in guest suite": "room", "Entire guesthouse house": "room", "Tiny house": "room",
                        "Shared room in condominium (condo)": "room", "Entire place": "house", "Earth house":  "house", "Private room": "house", "Private room in guesthouse": "house", "Camper/RV": "house", "Shared room in serviced apartment": "house", "Cycladic house": "house",
                        "Private room in loft": "room", "Floor": "house", "Private room in boat": "room", "Shared room in guesthouse": "room", "Private room in floor": "room", "Entire cottage": "house",
                        "Farm stay": "house", "Private room in tiny house": "room", "Shared room in nature lodge": "room", "Private room in earth house": "room", "Shared room in bed and breakfast": "room",
                        "Boat": "house", "Entire home/apt": "house", "Entire bed and breakfast": "room", "Private room in resort": "room", "Entire loft": "house", "Entire guesthouse": "house"}

    for var in data:
        if var == "property_type":
            data["property_type"].replace(property_mapping, inplace=True)

    return (data)


def bathrooms_prep(data):

    for var in data:
        if var == "bathrooms_text":
            data['bathrooms_text'] = data['bathrooms_text'].fillna('1 bath')
            data['bathrooms_text'] = data['bathrooms_text'].replace(
                {'Half-bath': '0.5', 'Shared half-bath': '0.5'}, regex=True)
            for i, val in enumerate(data["bathrooms_text"]):
                data["bathrooms_text"][i] = re.findall(
                    "[-+]?(?:\d*\.\d+|\d+)", val)[0]
                data["bathrooms_text"] = data["bathrooms_text"].astype(str)

    return (data)


def reviews_per_month_prep(data):
    for var in data:
        if var == "reviews_per_month":
            data['reviews_per_month'] = data['reviews_per_month'].fillna(
                data['reviews_per_month'].median())

    return (data)


def beds_prep(data):
    for var in data:
        if var == "beds":
            data['beds'] = data['beds'].fillna(data['beds'].median())

    return (data)


def spatial_data_prep(data):
    # Lat, Long of monuments
    Acropolis = (37.97255619074434, 23.725852581085093)
    Syntagma_square = (37.975753697142274, 23.734870097114324)
    for lat, lon in zip(data.latitude, data.longitude):
        data['Dist_Acropolis'] = hs.haversine(
            Acropolis, (float(lat), float(lon)))
        data['Dist_Syntagma'] = hs.haversine(
            Syntagma_square, (float(lat), float(lon)))

    return (data)

# Create has license column and drop license column


def license_prep(data):
    for var in data:
        if var == "license":
            data['license'] = ["1" if type(
                x) is str else "0" for x in data.license]
    return (data)


def dummies(data):

    headers = ['accommodates', 'bathrooms_text', 'beds', 'minimum_nights', 'maximum_nights',
               'maximum_minimum_nights', 'minimum_maximum_nights', 'minimum_nights_avg_ntm',
               'maximum_nights_avg_ntm', 'availability_30', 'availability_60',
               'availability_90', 'availability_365', 'number_of_reviews', 'reviews_per_month',
               'Dist_Acropolis', 'Dist_Syntagma', 'neighbourhood_cleansed_ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ',
               'neighbourhood_cleansed_ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ',
               'neighbourhood_cleansed_ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ', 'neighbourhood_cleansed_ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ',
               'neighbourhood_cleansed_ΑΚΡΟΠΟΛΗ', 'neighbourhood_cleansed_ΑΜΠΕΛΟΚΗΠΟΙ',
               'neighbourhood_cleansed_ΑΝΩ ΚΥΨΕΛΗ', 'neighbourhood_cleansed_ΑΝΩ ΠΑΤΗΣΙΑ',
               'neighbourhood_cleansed_ΒΟΤΑΝΙΚΟΣ', 'neighbourhood_cleansed_ΓΚΑΖΙ',
               'neighbourhood_cleansed_ΓΚΥΖΗ', 'neighbourhood_cleansed_ΓΟΥΒΑ',
               'neighbourhood_cleansed_ΓΟΥΔΙ', 'neighbourhood_cleansed_ΕΛΛΗΝΟΡΩΣΩΝ',
               'neighbourhood_cleansed_ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ',
               'neighbourhood_cleansed_ΖΑΠΠΕΙΟ', 'neighbourhood_cleansed_ΘΗΣΕΙΟ',
               'neighbourhood_cleansed_ΙΛΙΣΙΑ', 'neighbourhood_cleansed_ΚΕΡΑΜΕΙΚΟΣ',
               'neighbourhood_cleansed_ΚΟΛΟΚΥΝΘΟΥ', 'neighbourhood_cleansed_ΚΟΛΩΝΑΚΙ',
               'neighbourhood_cleansed_ΚΟΛΩΝΟΣ', 'neighbourhood_cleansed_ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ',
               'neighbourhood_cleansed_ΚΥΨΕΛΗ', 'neighbourhood_cleansed_ΛΥΚΑΒΗΤΤΟΣ',
               'neighbourhood_cleansed_ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ',
               'neighbourhood_cleansed_ΝΕΑ ΚΥΨΕΛΗ', 'neighbourhood_cleansed_ΝΕΟΣ ΚΟΣΜΟΣ',
               'neighbourhood_cleansed_ΝΙΡΒΑΝΑ', 'neighbourhood_cleansed_ΠΑΓΚΡΑΤΙ',
               'neighbourhood_cleansed_ΠΑΤΗΣΙΑ', 'neighbourhood_cleansed_ΠΕΔΙΟ ΑΡΕΩΣ',
               'neighbourhood_cleansed_ΠΕΝΤΑΓΩΝΟ', 'neighbourhood_cleansed_ΠΕΤΡΑΛΩΝΑ',
               'neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ', 'neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ',
               'neighbourhood_cleansed_ΠΟΛΥΓΩΝΟ', 'neighbourhood_cleansed_ΠΡΟΜΠΟΝΑ',
               'neighbourhood_cleansed_ΡΗΓΙΛΛΗΣ', 'neighbourhood_cleansed_ΡΙΖΟΥΠΟΛΗ',
               'neighbourhood_cleansed_ΣΕΠΟΛΙΑ', 'neighbourhood_cleansed_ΣΤΑΔΙΟ',
               'neighbourhood_cleansed_ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ', 'room_type_Hotel room',
               'room_type_Private room', 'room_type_Shared room',
               'host_is_superhost_1.0', 'host_has_profile_pic_1.0',
               'host_identity_verified_1.0', 'has_availability_1', 'instant_bookable_1', 'has_license_1']
    dt = pd.DataFrame(0, index=np.arange(len(data)), columns=headers)

    dt['accommodates'] = data['accommodates']
    dt['bathrooms_text'] = data['bathrooms_text']
    dt['beds'] = data['beds']
    dt['minimum_nights'] = data['minimum_nights']
    dt['maximum_nights'] = data['maximum_nights']
    dt['maximum_minimum_nights'] = data['maximum_minimum_nights']
    dt['minimum_maximum_nights'] = data['minimum_maximum_nights']
    dt['minimum_nights_avg_ntm'] = data['minimum_nights_avg_ntm']
    dt['maximum_nights_avg_ntm'] = data['maximum_nights_avg_ntm']

    dt['availability_30'] = data['availability_30']
    dt['availability_60'] = data['availability_60']
    dt['availability_90'] = data['availability_90']
    dt['availability_365'] = data['availability_365']

    dt['number_of_reviews'] = data['number_of_reviews']
    dt['reviews_per_month'] = data['reviews_per_month']
    dt['Dist_Acropolis'] = data['Dist_Acropolis']
    dt['Dist_Syntagma'] = data['Dist_Syntagma']

    if data['room_type'][0] == 'Hotel room':
        dt['room_type_Hotel room'] = 1
    elif (data['room_type'][0] == 'Private room'):
        dt['room_type_Private room'] = 1
    elif data['room_type'][0] == 'Shared room':
        dt['room_type_Shared room'] = 1

    dt['host_is_superhost_1.0'] = data['host_is_superhost']
    dt['host_has_profile_pic_1.0'] = data['host_has_profile_pic']
    dt['host_identity_verified_1.0'] = data['host_identity_verified']
    dt['has_availability_1'] = data['has_availability']
    dt['instant_bookable_1'] = data['instant_bookable']
    dt['has_license_1'] = data['license']

    if data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ':
        dt['neighbourhood_cleansed_ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ':
        dt['neighbourhood_cleansed_ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ':
        dt['neighbourhood_cleansed_ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ':
        dt['neighbourhood_cleansed_ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΚΡΟΠΟΛΗ':
        dt['neighbourhood_cleansed_ΑΚΡΟΠΟΛΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΜΠΕΛΟΚΗΠΟΙ':
        dt['neighbourhood_cleansed_ΑΜΠΕΛΟΚΗΠΟΙ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΝΩ ΚΥΨΕΛΗ':
        dt['neighbourhood_cleansed_ΑΝΩ ΚΥΨΕΛΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΑΝΩ ΠΑΤΗΣΙΑ':
        dt['neighbourhood_cleansed_ΑΝΩ ΠΑΤΗΣΙΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΒΟΤΑΝΙΚΟΣ':
        dt['neighbourhood_cleansed_ΒΟΤΑΝΙΚΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΓΚΑΖΙ':
        dt['neighbourhood_cleansed_ΓΚΑΖΙ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΓΚΥΖΗ':
        dt['neighbourhood_cleansed_ΓΚΥΖΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΓΟΥΒΑ':
        dt['neighbourhood_cleansed_ΓΟΥΒΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΓΟΥΔΙ':
        dt['neighbourhood_cleansed_ΓΟΥΔΙ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΕΛΛΗΝΟΡΩΣΩΝ':
        dt['neighbourhood_cleansed_ΕΛΛΗΝΟΡΩΣΩΝ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ':
        dt['neighbourhood_cleansed_ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΖΑΠΠΕΙΟ':
        dt['neighbourhood_cleansed_ΖΑΠΠΕΙΟ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΘΗΣΕΙΟ':
        dt['neighbourhood_cleansed_ΘΗΣΕΙΟ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΙΛΙΣΙΑ':
        dt['neighbourhood_cleansed_ΙΛΙΣΙΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΕΡΑΜΕΙΚΟΣ':
        dt['neighbourhood_cleansed_ΚΕΡΑΜΕΙΚΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΟΛΟΚΥΝΘΟΥ':
        dt['neighbourhood_cleansed_ΚΟΛΟΚΥΝΘΟΥ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΟΛΩΝΑΚΙ':
        dt['neighbourhood_cleansed_ΚΟΛΩΝΑΚΙ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΟΛΩΝΟΣ':
        dt['neighbourhood_cleansed_ΚΟΛΩΝΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ':
        dt['neighbourhood_cleansed_ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΚΥΨΕΛΗ':
        dt['neighbourhood_cleansed_ΚΥΨΕΛΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΝΕΟΣ ΚΟΣΜΟΣ':
        dt['neighbourhood_cleansed_ΝΕΟΣ ΚΟΣΜΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΝΙΡΒΑΝΑ':
        dt['neighbourhood_cleansed_ΝΙΡΒΑΝΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΑΓΚΡΑΤΙ':
        dt['neighbourhood_cleansed_ΠΑΓΚΡΑΤΙ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΑΤΗΣΙΑ':
        dt['neighbourhood_cleansed_ΠΑΤΗΣΙΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΕΔΙΟ ΑΡΕΩΣ':
        dt['neighbourhood_cleansed_ΠΕΔΙΟ ΑΡΕΩΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΕΝΤΑΓΩΝΟ':
        dt['neighbourhood_cleansed_ΠΕΝΤΑΓΩΝΟ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΕΤΡΑΛΩΝΑ':
        dt['neighbourhood_cleansed_ΠΕΤΡΑΛΩΝΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ':
        dt['neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ':
        dt['neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΟΛΥΓΩΝΟ':
        dt['neighbourhood_cleansed_ΠΟΛΥΓΩΝΟ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΠΡΟΜΠΟΝΑ':
        dt['neighbourhood_cleansed_ΠΡΟΜΠΟΝΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΡΗΓΙΛΛΗΣ':
        dt['neighbourhood_cleansed_ΡΗΓΙΛΛΗΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΡΙΖΟΥΠΟΛΗ':
        dt['neighbourhood_cleansed_ΡΙΖΟΥΠΟΛΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΣΕΠΟΛΙΑ':
        dt['neighbourhood_cleansed_ΣΕΠΟΛΙΑ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΣΤΑΔΙΟ':
        dt['neighbourhood_cleansed_ΣΤΑΔΙΟ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ':
        dt['neighbourhood_cleansed_ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΛΥΚΑΒΗΤΤΟΣ':
        dt['neighbourhood_cleansed_ΛΥΚΑΒΗΤΤΟΣ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ':
        dt['neighbourhood_cleansed_ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ'] = 1
    elif data['neighbourhood_cleansed'][0] == 'neighbourhood_cleansed_ΝΕΑ ΚΥΨΕΛΗ':
        dt['neighbourhood_cleansed_ΝΕΑ ΚΥΨΕΛΗ'] = 1

    return dt


def featureScalingAll(data):

    mean = [3.735838552540014,
            1.1535142658315936,
            2.043284620737648,
            3.28169798190675,
            2139.765483646486,
            3.3056367432150315,
            927.7885873347251,
            3.1984690327070284,
            931.8544885177453,
            13.22491301322199,
            32.61419624217119,
            53.1704940848991,
            228.74961725817676,
            35.07571329157968,
            1.5203020180932496,
            1.7533078290738775,
            1.6685659216326008,
            0.0022268615170494086,
            0.06610995128740431,
            0.007515657620041753,
            0.006263048016701462,
            0.032011134307585246,
            0.03242867084203201,
            0.007654836464857342,
            0.006123869171885873,
            0.005984690327070285,
            0.0065414057063326375,
            0.009324982602644399,
            0.006263048016701462,
            0.018093249826026444,
            0.004453723034098817,
            0.1916492693110647,
            0.014057063326374391,
            0.031315240083507306,
            0.018093249826026444,
            0.025052192066805846,
            0.0019485038274182323,
            0.031871955462769656,
            0.008629088378566458,
            0.08601252609603341,
            0.020876826722338204,
            0.013639526791927627,
            0.07195546276965901,
            0.005984690327070285,
            0.0744606819763396,
            0.011830201809324982,
            0.039526791927627,
            0.012386917188587334,
            0.008768267223382045,
            0.00013917884481558804,
            0.024773834377174668,
            0.012386917188587334,
            0.04077940153096729,
            0.0018093249826026444,
            0.0005567153792623522,
            0.0002783576896311761,
            0.0011134307585247043,
            0.003340292275574113,
            0.0232428670842032,
            0.009464161447459986,
            0.015448851774530271,
            0.0918580375782881,
            0.008350730688935281,
            0.38761308281141266,
            0.996938065414057,
            0.7156576200417537,
            0.9780097425191371,
            0.6839248434237996,
            0.79526791927627]

    std = [1.7358488281909747,
           0.3386058482783085,
           1.2869017672456173,
           21.07460975685579,
           117966.27980859844,
           17.499064649326897,
           402.041518721875,
           17.47798656480772,
           397.6552329815551,
           11.386278890023336,
           23.16549395637106,
           34.047899871023276,
           131.09748459794147,
           50.56143148249674,
           1.3717790704100774,
           1.1140092751666437,
           0.9357427989856865,
           0.04714034248620854,
           0.24849148807600105,
           0.08637251191266379,
           0.07889669569259171,
           0.17604185537139277,
           0.17714801658275683,
           0.0871624765975547,
           0.0780206037515029,
           0.07713431066259818,
           0.08061960253838316,
           0.09612134632351699,
           0.07889669569259171,
           0.1332980011709746,
           0.06659207591341747,
           0.39362595372698117,
           0.11773441089787862,
           0.174180418944581,
           0.1332980011709746,
           0.15629452836691135,
           0.04410190313381633,
           0.1756713665815027,
           0.0924976648418067,
           0.28040205853568256,
           0.14298192255320707,
           0.1159972534272746,
           0.25843213714312685,
           0.0771343106625982,
           0.2625373913189709,
           0.10812897574742392,
           0.19485817721564935,
           0.11061276757216748,
           0.093234084639405,
           0.011797408394032484,
           0.1554459859537,
           0.11061276757216748,
           0.19779253494701596,
           0.042500620287668794,
           0.0235898897389482,
           0.016682893715921698,
           0.03335184920631065,
           0.057702670065688154,
           0.15068442646942687,
           0.0968292105820028,
           0.12333816110189084,
           0.28884554773304333,
           0.09100631124148938,
           0.48723938901928865,
           0.05525381483054475,
           0.4511320390003945,
           0.14666178694250287,
           0.46497499145687843,
           0.4035337899885201]

    data_list = [float(x) for x in data.values[0]]

    scaled = [(x-y/z) for x, y, z in zip(data_list, mean, std)]

    data.iloc[0] = scaled
    return (data)
