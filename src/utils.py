import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import pickle



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {} 
        best_models = {}       
        for model_name, model in models.items():
            model_params = param.get(model_name, {})

            gs = GridSearchCV(
                estimator=model,
                param_grid=model_params,
                cv=3,
                scoring="r2",
                n_jobs=-1
            )

            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_
            best_models[model_name] = best_model

            y_test_pred = best_model.predict(X_test)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score

        return report, best_models


    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)

            