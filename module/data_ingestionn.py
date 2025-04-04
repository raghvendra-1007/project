import pandas as pd

def load_dataset(filepath):
    try:
        df=pd.read_csv(filepath)

        print(df.info())

        print(df.isnull().sum())

        print(df.head())

        return df

    except Exception as e:
        print(f"Error:{e}")
        return None

if __name__ == "__main__":
    df = load_dataset("messy_tech_jobs.csv")