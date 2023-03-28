import xgboost as xgb
import pandas as pd

M=0.775
C=4187
def getHeat(t_in,t_pred):
    return abs(M*C*(t_pred-t_in))

def predict_summer(data):
    model = xgb.Booster()
    model.load_model(r"Ml\weights\model_summer.json")
    # xgtrain = xgb.DMatrix(data)
    test_list = data

    df= pd.DataFrame(test_list, columns=['Time', 'T_amb', 'T_in'])
    datas = xgb.DMatrix(df)
    print(model.predict(datas))
    return model.predict(datas)[0]
