import pandas as pd

df = pd.read_excel(r'C:\Users\mayan\Downloads\Clean_Files000.xlsx')


new_df = df[df['Close'].between(200,300) & df["Ticker"].str.startswith("BANKNIFTY", na = False) & df["Time"].str.endswith("10:00:59", na = False)]
print(new_df)

new_df.to_excel("output.xlsx")
