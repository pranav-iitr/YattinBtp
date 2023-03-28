import xgboost as xgb
import pandas as pd

def predict_winter(data):
    model = xgb.Booster()
    model.load_model(r"Ml\weights\model_winter.json")
    test_list = data
    df= pd.DataFrame(test_list, columns=['Time', 'T_amb', 'T_in'])
    datas = xgb.DMatrix(df)
    print(model.predict(datas))
    return model.predict(datas)[0]