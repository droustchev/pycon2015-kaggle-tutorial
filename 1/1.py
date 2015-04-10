import pandas as pd

def load_feature_matrix(path):
	df = pd.read_csv(path, parse_dates=['PostCreationDate','OwnerCreationDate'])
	df["TitleLength"] = df.Title.apply(len)
	df['TimeToPost'] = df.PostCreationDate.astype('i8') - df.OwnerCreationDate.astype('i8')
	return df