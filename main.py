from classifiers import NB_classifier
from utils import load_data

def main():

	data = load_data('spam.csv')
	train = int(len(data)*0.8)

	classifier = NB_classifier(data.iloc[:train])
	classifier.predict(data.iloc[train:])

if __name__ == '__main__':
	main()