import pandas as pd

googleSheetId = '1wuHLUD9QZNnf8STTkXylxxDCc0czEYjhoVfIVCwTv5Y'
worksheetName = 'Form'
URL = f'https://docs.google.com/spreadsheets/d/{googleSheetId}/gviz/tq?tqx=out:csv&sheet={worksheetName}'

df = pd.read_csv(URL)
print(df.info())