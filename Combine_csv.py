import glob
import pandas as pd
#import csv
#csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)
path = r'/home/uvionics/Downloads/check' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
#    df['bar'].iloc[0] = 0
    df = pd.read_csv(filename, index_col=None, header=0,error_bad_lines=False)
#    df['sales'].iloc[0] = 0
#   df['Stock_Quantity1']=df['Stock_Quantity']
#    df['Stock_Quantity1'].iloc[0] = 0

#i=0
#j=1
#while j < len(df['Stock_Quantity']):
#   
# #   df['Stock_Quantity1']=df['Stock_Quantity1'][i+1] - df['Stock_Quantity1'][i] #the difference btwn two values in a column.
#    i+=1 #move to the next value in the column.
#    j+=1 
#    df['Stock_Quantity1'].iloc[0] = 0
#    df['sales']=df['Stock_Quantity']
#    df['sales'].iloc[0] = 0
#    df['Stock_Quantity1'].iloc[0] = 0
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv('/home/uvionics/Downloads/check/new.csv', sep='\t', encoding='utf-8',index=False)
