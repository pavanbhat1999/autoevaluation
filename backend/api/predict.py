from backend.api.preprocessing import preprocessing

class Model:
    def __init__(self):
        pass
    def training(self):
            X_train,X_test,y_train,y_test = preprocessing()

            print("\n Shapes of content ",X_train.shape,X_test.shape)
    def predict(self,answer):
        
        return("#################   Marks given by Composite should Display#################################")
def execute(answer):

    
    y_pred = answer
    print(answer.shape)
    model = Model()
    prediction = model.predict(y_pred)    

    
    return(prediction)

