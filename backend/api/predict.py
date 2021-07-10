from backend.api.preprocessing import preprocessing,preprocessing_features
import pickle

class Model:
    def __init__(self):
        pass
    def training(self):
        # Training using both POW and features
        X_train,X_test,y_train,y_test = preprocessing(answer=None,isTest=False)
        # Training Using only features
        # X_train,X_test,y_train,y_test = preprocessing_features(answer=None,isTest=False)
            

        print("\n Shapes of content ",X_train.shape,X_test.shape)
    def predict(self,answer):
        filename = "static/finalized_model.sav"
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict([[6,148,72,35,0,33.6,0.627,50]])
        print(result)

        
        return(result)
def execute(answer):

    
    y_pred = answer
    print(answer.shape)
    model = Model()
    #model.training()
    prediction = model.predict(y_pred)    

    
    return(prediction)

