import pickle
import pandas as pd

model = pickle.load(open('healthscr.pkl', 'rb'))
scaler = pickle.load(open('scalar.pkl', 'rb'))
class_names = [0,1,2,3]

def predict(df):
    df = df[['TEMPF', 'PULSE', 'RESPR', 'BPSYS', 'BPDIAS', 'POPCT']]
    df = scaler.transform(df)
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output
