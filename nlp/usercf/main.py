import pandas as pd


df=pd.read_csv("ml-100k/u.data",sep='\t',nrows=10,
               names=['user_id','item_id','rating','timestamp'])
print(max(df["rating"]))
print(df.dtypes)

d=dict()
for _,row in df.iterrows():
    user_id=str(row['user_id'])
    item_id=str(row['item_id'])
    rating=row['rating']
    if user_id not in d.keys():
        d[user_id]={item_id:rating}
    else:
        d[user_id][item_id]=rating

print(d)