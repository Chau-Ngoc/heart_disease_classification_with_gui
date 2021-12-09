import joblib
import PySimpleGUI as sg

import pandas as pd

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
        a_patient = {
            'age': '',
            'sex': '',
            'cp': '',
            'trestbps': '',
            'chol': '',
            'fbs': '',
            'restecg': '',
            'thalach': '',
            'exang': '',
            'oldpeak': '',
            'slope': '',
            'ca': '',
            'thal': '',
        }

        a_patient['age'] = int(values['-AGE-'])

        if values['-SEX-'] == 'Female':
            a_patient['sex'] = 0
        elif values['-SEX-'] == 'Male':
            a_patient['sex'] = 1

        if values['-CP-'] == 'typical angina':
            a_patient['cp'] = 0
        elif values['-CP-'] == 'atypical angina':
            a_patient['cp'] = 1
        elif values['-CP-'] == 'non-anginal pain':
            a_patient['cp'] = 2
        elif values['-CP-'] == 'asymptomatic':
            a_patient['cp'] = 3

        a_patient['trestbps'] = int(values['-TRESTBPS-'])
        a_patient['chol'] = int(values['-CHOL-'])

        if values['-FBS-']:
            a_patient['fbs'] = 1
        elif values['-FBS-'] == False:
            a_patient['fbs'] = 0

        if values['-RESTECG-'] == 'normal':
            a_patient['restecg'] = 0
        elif values['-RESTECG-'] == 'ST-T wave abnormality':
            a_patient['restecg'] = 1
        elif values['-RESTECG-'] == 'showing probable or definite left ventricular hypertrophy by Estes\' criteria':
            a_patient['restecg'] = 2

        a_patient['thalach'] = int(values['-THALACH-'])

        if values['-EXANG-']:
            a_patient['exang'] = 1
        elif values['-EXANG-'] == False:
            a_patient['exang'] = 0

        a_patient['oldpeak'] = float(values['-OLDPEAK-'])

        if values['-SLOPE-'] == 'upsloping':
            a_patient['slope'] = 0
        elif values['-SLOPE-'] == 'flat':
            a_patient['slope'] = 1
        elif values['-SLOPE-'] == 'downsloping':
            a_patient['slope'] = 2

        a_patient['ca'] = values['-CA-']

        if values['-THAL-'] == 'normal':
            a_patient['thal'] = 0
        elif values['-THAL-'] == 'fixed defect':
            a_patient['thal'] = 1
        elif values['-THAL-'] == 'reversable defect':
            a_patient['thal'] = 2

        # print(a_patient)

        a_patient = pd.DataFrame(a_patient, index=[0])

        a_patient = loaded_ct.transform(a_patient)
        a_patient = loaded_scaler.transform(a_patient)
        prediction = loaded_model.predict(a_patient)

        print(prediction[0])
        print(type(prediction))

        if prediction[0] == 1:
            sg.popup_ok('Congratulation! You Don\'t Have Heart Disease.', background_color='green')
        else:
            sg.popup_ok('You Do Have Heart Disease! Go See A Doctor.', background_color='red')

window.close()
