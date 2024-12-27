import pandas as pd
DATA_DIR = "F:\\elections\\"
df = pd.read_pickle(f"{DATA_DIR}\\election_data_2020.pkl")

df = df.dropna(subset=["Proposition A City of Austin (FP) (2015)"])

cd2 = pd.pivot_table(df,index='President/Vice President', columns=['Austin City Council District 2'],values=['Cast Vote Record'],aggfunc="count", margins=True)
cd4 = pd.pivot_table(df,index='President/Vice President', columns=['Austin City Council District 4'],values=['Cast Vote Record'],aggfunc="count", margins=True)
cd6 = pd.pivot_table(df,index='President/Vice President', columns=['Austin City Council District 6'],values=['Cast Vote Record'],aggfunc="count", margins=True)
cd7 = pd.pivot_table(df,index='President/Vice President', columns=['Austin City Council District 7'],values=['Cast Vote Record'],aggfunc="count", margins=True)
cd10 = pd.pivot_table(df,index='President/Vice President', columns=['Austin City Council District 10'],values=['Cast Vote Record'],aggfunc="count", margins=True)
sen = pd.pivot_table(df,index='President/Vice President', columns=['United States Senator'],values=['Cast Vote Record'],aggfunc="count", margins=True)
rr = pd.pivot_table(df,index='President/Vice President', columns=['Railroad Commissioner'],values=['Cast Vote Record'],aggfunc="count", margins=True)

def output_f(file,file_name):
    file.to_csv(f"{file_name}.csv")

output_f(cd2,"cd2")
output_f(cd4,"cd4")
output_f(cd6,"cd6")
output_f(cd7,"cd7")
output_f(cd10,"cd10")
output_f(sen,"sen")
output_f(rr, "rr")



print(df)

