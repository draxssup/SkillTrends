import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("clean_jobs.csv")

print(data.info())
print((data.isnull().sum()/data['id'].count())*100)
#irrelevent features
data.drop(['location', 'link', 'source', 'id','work_type','employment_type'],axis=1,inplace=True)

#saving new csv file:
data.to_csv('newdata.csv', index=False)

data['description'] =  data['description'].fillna(data['title'])

print((data.isnull().sum()/data['title'].count())*100)
