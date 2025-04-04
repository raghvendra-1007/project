from eda_summary import clean_dataset
import pandas as pd

def job_posting_yearwise(df):
    return df["year"].value_counts().sort_index()

def salary_by_year_and_title(df):
    return df.groupby(["year","job_title"])