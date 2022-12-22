import pandas as pd

# pip install pandas

# df = pd.read_csv('.ouput.txt',sep="\t",encoding='utf-8')
# print(df)
# df.to_excel('newResult.xlsx',index=True)

import pandas as pd

df = pd.DataFrame(pd.read_csv('400_3.txt',sep='    '))

print(df)

df.to_excel('테스트2.xlsx',index=False) 