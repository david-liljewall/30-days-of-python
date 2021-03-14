import pandas as pd


dictionary = {
    "region": [ "USA", "India" ],
    "price:": [ 1000, 2000 ]
}

df = pd.DataFrame( dictionary )
print( df )

print() 

df_grouped = df.groupby( "region" )

for data in df_grouped:
    print( data )

df_grouped.price.min()