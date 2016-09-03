import pandas as pd

# improve portability
import os

folder = r'C:\Users\daniel\scripts\csv_cleaner'
in_file = r'VisitorAnswer2.csv'
out_file = r'VisitorAnswer2_clean.csv'
in_path = os.path.join(folder, in_file)

df = pd.read_csv(in_path, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

# df["AnswerText"].apply(str)

df["AnswerText"] = df["AnswerText"].astype(str).str.replace('/n', '')
df["AnswerText"] = df["AnswerText"].astype(str).str.replace('/r', '')
df["AnswerText"] = df["AnswerText"].astype(str).str.replace('/', '')
df["AnswerText"] = df["AnswerText"].astype(str).str.replace('\\', '')
df["AnswerText"] = df["AnswerText"].astype(str).str.replace('*', '')
df["AnswerText"] = df["AnswerText"].astype(str).str.replace(',', '')

df.to_csv(os.path.join(folder, out_file))
