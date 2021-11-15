import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('HealthScore\healthscr.pkl', 'rb'))
scaler = pickle.load(open('HealthScore\scalar.pkl', 'rb'))
class_names = [0,1,2,3]

def predict(df):
    df = df[['TEMPF', 'PULSE', 'RESPR', 'BPSYS', 'BPDIAS', 'POPCT']]
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output

temp = 99.1
pul = 90
resp = 16
bpsys = 129
bpdi=75
pop = 99


df = pd.DataFrame({ 
    'TEMPF':[temp],
    'PULSE':[pul], 
    'RESPR':[resp], 
    'BPSYS':[bpsys], 
    'BPDIAS':[bpdi],
    'BPDIAS':[bpdi],
    'POPCT':[pop]

})
print(predict(df))