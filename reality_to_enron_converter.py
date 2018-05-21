import pandas as pd

df = pd.read_csv("reality-mining-calls.txt",delimiter=r"\t+")

df['date'] =  pd.to_datetime(df['date'], infer_datetime_format=True)
df = df.sort_values('date')
df['days'] = (df['date'] - df['date'].min()).astype('timedelta64[D]').astype('int')

for i in range(0,df['days'].max()+1):
    df2 = df[df['days']==i]
    df2[['subjectId','otherPartyId']].to_csv("reality_raw/"+str(i)+"_enron_by_day.txt",sep=" ",header=False,index=False)




pass