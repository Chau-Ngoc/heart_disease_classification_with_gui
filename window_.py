import joblib
import PySimpleGUI as sg

import pandas as pd


def predict_patient(age: int, sex: int, cp: int, trestbps: int,
                    chol: int, fbs: int, restecg: int, thalach: int,
                    exang: int, oldpeak: float, slope: int, ca: int, thal: int):
    a_patient = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    a_patient = pd.DataFrame(a_patient, index=[0])

    a_patient = loaded_ct.transform(a_patient)
    a_patient = loaded_scaler.transform(a_patient)
    prediction = loaded_model.predict(a_patient)

    return prediction


loaded_ct = joblib.load('./column_transformer.joblib')
loaded_scaler = joblib.load('./scaler.joblib')
loaded_model = joblib.load('./final_model.joblib')

# ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
#        'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

# ----------LAYOUT----------
# age:                                                              Input
# sex:                                                              Combo (1 = male, 0 = female)
# cp (chest pain type):                                             Combo (0, 1, 2, 3)
# trestbps (resting blood pressure in mmHg):                        Input
# chol (serum cholesterol in mg/dl):                                Input
# fbs (fasting blood sugar > 120 mg/dl):                            Checkbox (1 = true, 0 = false)
# restecg (resting electrocardiographic results):                   Combo (0, 1, 2)
# thalach (maximum heart rate achieved):                            Input
# exang (exercise-induced angina):                                  Checkbox (1 = yes, 0 = no)
# oldpeak (ST depression induced by exercise relative to rest):     Input
# slope (the slope of the peak exercise ST segment):                Combo (0 = upsloping, 1 = flat, 2 = downsloping)
# ca (number of major vessels):                                     Combo (0, 1, 2, 3)
# thal:                                                             Combo (0 = normal; 1 = fixed defect; 2 = reversable defect)

# ----------CODE FOR GUI WINDOW----------
layout = [
    [sg.Text('How old are you?', pad=((5, 5), (20, 5))), sg.Input(tooltip='Enter your age', do_not_clear=False,
                                                                  key='-AGE-', justification='right', pad=((5, 5), (20, 5)))],

    [sg.Text('Gender:', pad=((5, 5), (20, 5))), sg.Combo(['Male', 'Female'],
                                                         default_value='Male', key='-SEX-', pad=((5, 5), (20, 5)))],

    [sg.Text('Chest pain type:', pad=((5, 5), (20, 5))), sg.Combo(['typical angina',
                                                                   'atypical angina', 'non-anginal pain', 'asymptomatic'],
                                                                  key='-CP-', pad=((5, 5), (20, 5)))],

    [sg.Text('Resting blood pressure in mmHg:', pad=((5, 5), (20, 5)))],
    [sg.Input(justification='right', key='-TRESTBPS-', pad=((5, 5), (0, 0)))],

    [sg.Text('Serum cholesterol in mg/dl:', pad=((5, 5), (20, 5)))],
    [sg.Input(justification='right', key='-CHOL-', pad=((5, 5), (0, 0)))],

    [sg.Text('Fasting blood sugar > 120 mg/dl:', pad=((5, 5), (20, 5))),
     sg.Checkbox('Yes', default=True, key='-FBS-', pad=((5, 5), (20, 5)))],

    [sg.Text('Resting electrocardiographic results:', pad=((5, 5), (20, 5)))],
    [sg.Combo(['normal', 'ST-T wave abnormality',
               'showing probable or definite left ventricular hypertrophy by Estes\' criteria'], default_value='normal',
              key='-RESTECG-', pad=((5, 5), (0, 0)))],

    [sg.Text('Maximum heart rate achieved:', pad=((5, 5), (20, 5))),
     sg.Input(justification='right', key='-THALACH-', pad=((5, 5), (20, 5)))],

    [sg.Text('Exercise-induced angina:', pad=((5, 5), (20, 5))),
     sg.Checkbox('Yes', default=True, key='-EXANG-', pad=((5, 5), (20, 5)))],

    [sg.Text('ST depression induced by exercise relative to rest:',
             pad=((5, 5), (20, 5)))],
    [sg.Input(justification='right', key='-OLDPEAK-', pad=((5, 5), (0, 0)))],

    [sg.Text('the slope of the peak exercise ST segment:', pad=((5, 5), (20, 5))),
     sg.Combo(['upsloping', 'flat', 'downsloping'], key='-SLOPE-', pad=((5, 5), (20, 5)))],

    [sg.Text('Number of major vessels:', pad=((5, 5), (20, 5))),
     sg.Combo([0, 1, 2, 3], key='-CA-', pad=((5, 5), (20, 5)))],

    [sg.Text('Thal', pad=((5, 5), (20, 5))),
     sg.Combo(['normal', 'fixed defect', 'reversable defect'], key='-THAL-', pad=((5, 5), (20, 5)))],

    [sg.Button('Do I Have Heart Disease?'), sg.Button('Cancel')]
]

window = sg.Window('Heart Disease Classification GUI',
                   layout, font=('Arial', 16))

while True:
    event, values = window.read()

    # print(f'Event: {event}\nValues: {values}')
    # print()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    if event == 'Do I Have Heart Disease?':
        genders_dict = {'Female': 0, 'Male': 1}

        cp_types_dict = {
            'typical angina': 0,
            'atypical angina': 1,
            'non-anginal pain': 2,
            'asymptomatic': 3,
        }

        restecg_dict = {
            'normal': 0,
            'ST-T wave abnormality': 1,
            'showing probable or definite left ventricular hypertrophy by Estes\' criteria': 2,
        }

        slope_dict = {
            'upsloping': 0,
            'flat': 1,
            'downsloping': 2,
        }

        thal_dict = {
            'normal': 0,
            'fixed defect': 1,
            'reversable defect': 2,
        }

        age = int(values['-AGE-'])
        sex = genders_dict[values['-SEX-']]
        cp = cp_types_dict[values['-CP-']]
        trestbps = int(values['-TRESTBPS-'])
        chol = int(values['-CHOL-'])
        fbs = int(values['-FBS-'])
        restecg = restecg_dict[values['-RESTECG-']]
        thalach = int(values['-THALACH-'])
        exang = int(values['-EXANG-'])
        oldpeak = float(values['-OLDPEAK-'])
        slope = slope_dict[values['-SLOPE-']]
        ca = values['-CA-']
        thal = thal_dict[values['-THAL-']]

        prediction = predict_patient(age, sex, cp, trestbps,
                                     chol, fbs, restecg, thalach,
                                     exang, oldpeak, slope, ca, thal)

        print(prediction[0])
        print(type(prediction))

        if prediction[0] == 1:
            sg.popup_ok(
                'Congratulation! You Don\'t Have Heart Disease.', background_color='green')
        else:
            sg.popup_ok('You Do Have Heart Disease! Go See A Doctor.',
                        background_color='red')

window.close()
