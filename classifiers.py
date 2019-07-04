import pandas as pd

from utils import load_data, preprocessing



class NB_classifier(object):
    def __init__(self, data):
        print("Initialised")
        self.table = preprocessing(data)
        self.spam = self.table[data['v1'] == 'spam']
        self.ham = self.table[data['v1'] == 'ham']
        self.data = self.spam, self.ham
        self.length = len(self.ham), len(self.spam)

    
    def predict(self, data):
        print("predicting..")
        pred_data = preprocessing(data)
        pred = []
        gt = []
        for index, row in pred_data.iterrows():
            pred.append(self.predict_single(row['v2']))
            gt.append(row['v1'])
        self.get_metrics(pred, gt)
    
    def get_metrics(self, pred, gt):
        count = 0
        for p,t in zip(pred,gt):
            if round(p) == t:
                count+=1
        return count/len(pred)

    def predict_single(self, msg):
        prob_spam = self.P_X_given_y(msg, y=1) * self.P_y(y=1) 
        prob_ham = self.P_X_given_y(msg, y=0) * self.P_y(y=0)

        return prob_spam/(prob_spam+prob_ham)

    def P_y(self, y):
        return self.length[y]/(self.length[0] + self.length[1])

    def P_X_given_y(self, msg, y):
        prod = 1
        for word in msg.split():
            try:
                prod *= self.P_xj_given_y(word, y)
            except:
                pass

    def P_xj_given_y(self, word, y):
        count = 0
        data = self.data[y]
        for index, row in data.iterrows():
            if word in row['v2']:
                count += 1
        return count/self.length[y]



