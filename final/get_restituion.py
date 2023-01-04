import pandas as pd

dataset = pd.read_csv('height.csv')
data = dataset.iloc[:, :].values

def get_local_max(l):
    res = []
    for i in range(1,len(l)-1, 1):
        if(l[i-1]<l[i] & l[i]>=l[i+1]):
            if(len(res)==0):
                res.append(l[i])
            if(res[-1]!=l[i]):
                res.append(l[i])
    return res

h = []

for i in range(360):
    h.append(data[i][1])

# print(h)
res = get_local_max(h)
import pandas as pd
pd.DataFrame(res).to_csv('max.csv')