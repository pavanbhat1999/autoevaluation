from backend.api.preprocessing import preprocessing

class Model:
    def __init__(self):
        pass
    def predict(self,answer):
        
        return("#################   Marks given by Composite should Display#################################")
def predict(answer):
    X_train,X_test,y_train,y_test = preprocessing()

    print("\n Shapes of content ",X_train.shape,X_test.shape,answer.shape)
    y_pred = answer
    model = Model()
    prediction = model.predict(y_pred)    

    
    return(prediction)

