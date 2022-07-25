import pickle
import os
import sys
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", message="Reloaded modules: <module_name>")

def train():
    data = pd.read_csv('heart.csv')
    
    Y = data["target"]
    X = data.drop('target',axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state = 0)

    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='liblinear')
    loj_reg=model.fit(X_train,Y_train.values.ravel())
    
    with open('svc.pkl','wb') as m:
        pickle.dump(loj_reg,m)
    test(X_test,Y_test)
    
def test(X_test,Y_test):
    with open('svc.pkl','rb') as mod:
        p=pickle.load(mod)
    
    pre=p.predict(X_test)
    print (accuracy_score(Y_test,pre))
    
def find_data_file(filename):
    if getattr(sys, "frozen", False):
        
        datadir = os.path.dirname(sys.executable)
    else:
        
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)


def check_input(data) ->int :
    df=pd.DataFrame(data=data,index=[0])
    with open(find_data_file('svc.pkl'),'rb') as model:
        p=pickle.load(model)
    op=p.predict(df)
    
    return op[0]
if __name__=='__main__':
    train() 
   