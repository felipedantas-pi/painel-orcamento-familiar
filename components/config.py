import pandas as pd

# Carregador os dados

def load_dataset(sheet_name: str) -> object:
  """
  Load a dataset from an Excel file and preprocess it.

  Args: sheet_name (str): Name of the sheet to load.

  Returns: object: A pandas DataFrame with the loaded and preprocessed dataset.
  """
  df = pd.read_excel(io='assets/datasets/dataset_full.xlsx', engine='openpyxl', sheet_name=sheet_name, decimal=',')
  df.insert(1, column='mes', value=df["data"].dt.month)
  df['data'] = df['data'].sort_values().dt.date
  return df