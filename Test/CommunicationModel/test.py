import pandas as pd
def csv_input():
    name="SendDB\overallPrediction.csv"
    df=pd.read_csv(name,sep=',')
    df.sort_values("Crop Rank",inplace=True)
    a=df[0:]
    x=a['Crop Name'].values
    print(x[0:3])
    print(x[0])
    print(a)

csv_input()

