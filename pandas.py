[2:43 PM] Priyanka
#Example 7:Using the Pandas library to Handle CSV files
#Pandas is a popular data science library in Python for data manipulation and analysis.
# If we are working with huge chunks of data,
# it's better to use pandas to handle CSV files for ease and efficiency.(after execute)
# import pandas as pd
# data=pd.read_csv("PandasCSV.csv")
# print(pd)
# print(data)
#To write to a CSV file, we need to call the to_csv()
# function of a DataFrame. (fist execute)
import pandas as pd

# creating a data frame
df = pd.DataFrame([[1,'Jack', 567], [2,'Rose', 222]], columns = ['Sno','Name', 'Age'])

# writing data frame to a CSV file
df.to_csv('PandasCSV.csv')

#Example 9
# import pandas
# df = pandas.read_csv('PandasCSV.csv', index_col='Sno')
# print(df)
#
# import pandas
# df = pandas.read_csv('PandasCSV.csv', header=0,names=['Serial no', 'Employee name', 'Employee age'])
# print(df)


