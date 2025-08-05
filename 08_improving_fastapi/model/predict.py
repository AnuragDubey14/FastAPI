
import pickle 
import pandas as pd 
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "model.pkl")

print(f"Loading model from: {file_path}")  # Optional debug log

with open(file_path, 'rb') as f:
    model = pickle.load(f)


# MLFlow
MODEL_VERSION='1.0.0'

class_labels=model.classes_.tolist()


def predict_output(user_input:dict):
    input_df=pd.DataFrame([user_input])
    predict_result=model.predict(input_df)[0]
    probabilities=model.predict_proba(input_df)[0]
    confidence=max(probabilities)

    class_probs=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))

    return {
        "predicted_category":predict_result,
        "confidence":round(confidence,4),
        "class_probabilities":class_probs
    }