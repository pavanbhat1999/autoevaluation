from backend.api.preprocessing import preprocessing,preprocessing_features

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
        
        return("#################   Marks given by Composite should Display#################################")
def execute(answer):

    
    y_pred = answer
    print(answer.shape)
    model = Model()
    #model.training()
    prediction = model.predict(y_pred)    

    
    return(prediction)

