import pandas as pd
import numpy as np

df=pd.read_csv("messy_tech_jobs.csv")

def clean_dataset(df):
    df.dropna(subset=["company_name"], inplace=True)

    df["skills"].fillna("not specified",inplace=True)

    df["employment_type"].fillna("Unknown",inplace=True)

    df["salary"] = df["salary"].replace("Negotiable", np.nan)
    df["salary"] = df["salary"].fillna("0")

    print(df["salary"])

    def cleaned_salary(salary):
        salary = str(salary).strip().replace("$", "").replace(",", "").replace("k", "000")
        return pd.to_numeric(salary, errors="coerce")
    df["salary"]=df["salary"].apply(cleaned_salary)
        
    mean_salary = df[df["salary"] > 0]["salary"].mean()
    df["salary"] = df["salary"].replace(0, mean_salary)
    
    df["salary"]=df["salary"].round(2)

    df["posting_date"]=pd.to_datetime(df["posting_date"],errors="coerce")
    df["year"]=pd.to_datetime(df["posting_date"]).dt.year

    return df

print(clean_dataset(df))