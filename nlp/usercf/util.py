import pandas as pd

def generate_train_data(nrows=10):
    df=pd.read_csv("ml-100k/u.data",sep='\t',nrows=nrows,
                   names=['user_id','item_id','rating','timestamp'])
    d=dict()
    for _,row in df.iterrows():
        user_id=str(row['user_id'])
        item_id=str(row['item_id'])
        rating=row['rating']
        if user_id not in d.keys():
            d[user_id]={item_id:rating}
        else:
            d[user_id][item_id]=rating
    return d