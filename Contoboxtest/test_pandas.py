import pandas as pd
import math
x = pd.read_clipboard()

print(x)


data_dictionary ={}
device = []
domain =[]
city=[]

d = x['device_type_id']
f = x['domain']
g= x['city_id']




dev_type=len(x)
domain_list =len(f)
city_list=len(g)



for i in range(0,dev_type):
    if math.isnan(d[i]) :
        pass
    else:
        device.append(d[i])


for i in range(0,domain_list):

    domain.append(f[i])

for i in range(0,city_list):
    if math.isnan(g[i]) :
        pass
    else:
        city.append(g[i])

data_dictionary['device'] = device
data_dictionary['domain'] = domain
data_dictionary['city']  = city

print(data_dictionary)



