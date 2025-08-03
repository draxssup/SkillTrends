import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("data/clean_jobs.csv")

print(data.info())
print((data.isnull().sum()/data['id'].count())*100)
#irrelevent features
data.drop(['location', 'link', 'source', 'id','work_type','employment_type'],axis=1,inplace=True)
#replace na description with title
data['description'] =  data['description'].fillna(data['title'])
#replace company with unk
data['company'] =  data['company'].fillna('Unknown')
#removing all rows with no date data:
data = data.dropna(subset='date_posted')
#checking null values
print((data.isnull().sum()/data['title'].count())*100)
#saving cleaned data:
data.to_csv('data/newdata.csv', index=False)
#handling datetime
data['date_posted'] = pd.to_datetime(data['date_posted'], errors='coerce')
data['month'] = data['date_posted'].dt.to_period('M')
print(data['month'].value_counts().sort_index())
