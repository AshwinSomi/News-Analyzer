from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as ps

df=ps.read_csv('data.csv')# encoding='cp1252')

analyzer = SentimentIntensityAnalyzer()

negative=[];neutral=[];positive=[]

for i in range(df.shape[0]):
    title=df.iloc[i,0]
    description=df.iloc[i,3]
    publisher=df.iloc[i,1]
    title_ana =analyzer.polarity_scores(title)
    description_ana = analyzer.polarity_scores(description)
    negative.append(((title_ana['neg'])+(description_ana['neg']))/2)
    neutral.append(((title_ana['neu']) + (description_ana['neu'])) / 2)
    positive.append(((title_ana['pos']) + (description_ana['pos'])) / 2)
df['Negative']=negative
df['Neutral']=neutral
df['Positive']=positive
ps.set_option('display.max_columns',None)
#print(df.head())

print(df.nlargest(20,['Negative']))
print(df.nlargest(20,['Positive']))

"""print(df['Negative'].mean())
print(df['Positive'].mean())
print(df['Neutral'].mean())"""