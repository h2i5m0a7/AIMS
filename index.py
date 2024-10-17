## we need to make one hot encoding and ordinal encoding in python . nit in ML 
# Steps to Perform Ordinal Encoding:

# Identify Categorical Variables: Look at your dataset and identify which columns are categorical and have a meaningful order.
# Create a Mapping: For each categorical column, create a dictionary that maps each category to a number based on its order.
# Replace Categories with Numbers: Use this mapping to replace the categorical values in your dataset with their corresponding numbers.

import pandas as pd
import numpy as np

data={
    'Name':['Himani','Prisha','Punya','Riddhi','Japreet','Divya','Ishita','Devanshi','Dipesh','Abhinab'],
    'Gender':['Female','Female','Female','Female','Female','Female','Female','Female','Male','Male'],
    'Occupation':['Student','Student','Engineer', 'Teacher', 'Student', 'Manager','Engineer', 'Teacher', 'Student', 'Manager'],
    'size':['small','large','medium','small','large','medium','small','small','large','medium']
}
df= pd.DataFrame(data)

print("Original DataFrame:")
print(df)

#ordinal encoding - isme we use map() to trasform the value . we can change size since it can have a specific order . 
size_mapping= {"small":0, "medium":1 , "large":2 }
df['sizeEncoded']= df['size'].map(size_mapping)
print("after encoding")
print(df)

## one hot encoding isme we use get_dummies for converting categorial values to one hot enocding . get_dummies converts columns to binary columns . 
# it doesnt modify the dataframne . hence we concatenate it explicitly. 
# df['Gender'] = df['Gender'].astype(int)
# dummies = pd.get_dummies(df['Gender'])
# df_with_dummies = pd.concat([df, dummies], axis=1)
# print(df_with_dummies)  


# gender_mapping = {'Male': 0, 'Female': 1}

# # Apply the mapping
# df['Gender_Encoded'] = df['Gender'].map(gender_mapping)

# # Print the updated DataFrame
# print(df)

for i in df.Gender.unique():
    df[i] = (df['Gender'] == i).astype(int) 

print(df) 

# here df[i] creates a new column , then df[gender] makes a new list , and then that list is being used to check if it is false ot true and the n int chnages it to one or zero 
# now th