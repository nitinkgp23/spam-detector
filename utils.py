import pandas as pd
import string

def load_data(path):
	'''
	Path to to csv file
	'''
	
	return pd.read_csv(path)

def preprocessing(data):
    '''
    Removes all punctuations from the data
    '''
    table = str.maketrans('', '', string.punctuation)
    for index, row in data.iterrows():
        stripped = " ".join([w.translate(table) for w in row['v2'].split()])
        row['v2'] = stripped
        
    return data