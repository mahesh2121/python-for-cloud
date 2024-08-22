import pandas as pd

data = {
    'Name': ['Mahesh', 'Suresh'],
    'Age': [30, 28],
    'City': ['Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)