import pandas as pd

df = pd.DataFrame({"aaa": [4, 5, 6, 7], "bbb": [10, 20, 30, 40], "ccc": [100, 50, -30, -50]})

df['logic'] = pd.np.where(df['aaa'] > 5, 'high', 'low')
print(df)

# 在列上操作，当 aaa 列大于等于 5 时，bbb 列对应的值为 -1
df.loc[df.aaa >= 5, 'bbb'] = -1

df.loc[df.aaa >= 5, ['bbb', 'ccc']] = 555

df.loc[df.aaa < 5, ['bbb', 'ccc']] = 2000
print(df)

df_mask = pd.DataFrame({"aaa": [True] * 4, "bbb1": [True] * 4, "ccc": [True, False] * 2, "ddd": [True, False] * 2})
print(df_mask)

# 把 df 中和 df_mask 处于同样位置的 false 值置为 -1000
print(df.where(df_mask, -1000))
