from library import RSA
import pandas as pd

obj = RSA(512)

USD_TO_INR = 82

df = pd.read_csv("ds_salaries.csv")

usd_df = df['salary_in_usd']
e_usd_df = usd_df.apply(lambda elem: obj.encrypt(elem))

e_inr_df = e_usd_df.apply(lambda elem: elem * obj.encrypt(USD_TO_INR))
inr_df = e_inr_df.apply(lambda elem: obj.decrypt(elem))
print(usd_df, inr_df)


