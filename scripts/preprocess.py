
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_input(input_dict):
    """
    Accepts a dictionary of raw input values and returns a preprocessed list.
    Example input_dict: {"protocol_type": "tcp", "service": "http", ...}
    """

    df = pd.DataFrame([input_dict])

    # Encode categorical features
    categorical_columns = ["protocol_type", "service", "flag"]
    for col in categorical_columns:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

    # Ensure correct feature ordering (only keys from input_dict will be used here)
    processed_data = df.values.tolist()[0]

    return processed_data
