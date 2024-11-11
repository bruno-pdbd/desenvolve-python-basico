import pandas as pd
dataFrame=pd.read_csv('spotify-2023.csv',encoding='latin-1')
filteredDataFrame=dataFrame[(dataFrame['released_year']>=2012) & (dataFrame['released_year']<=2022)].copy()
filteredDataFrame.loc[:,'released_year']=pd.to_numeric(filteredDataFrame['released_year'])
filteredDataFrame.loc[:,'streams']=pd.to_numeric(filteredDataFrame['streams'])
filteredDataFrame=filteredDataFrame.dropna(subset=['released_year','streams'])
result=filteredDataFrame.loc[filteredDataFrame.groupby('released_year')['streams'].idxmax()]
result=result[['track_name','artist(s)_name','released_year','streams']]
result=result[result['released_year'].between(2012, 2022)]
result=result.drop_duplicates(subset=['released_year'])
result=result.sort_values(by='released_year').head(10)
resultList=result.values.tolist()
for index,item in enumerate(resultList):
    print("Posição {}: {}".format(index+1,item))