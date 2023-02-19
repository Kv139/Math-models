import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from test import v2light_pollution
from test import calculate_adjacency
from test import calc_risk


urban_2 = v2light_pollution(10,10,8,5,6,[[7,5,10,5,9]])
suburban_2 = v2light_pollution(7,5,10,5,9,[[10,10,8,5,6],[2,1,3,5,10]])
rural_2 = v2light_pollution(2,1,3,5,10,[[7,5,10,5,9],[.1,0,1,5,7]])
protected_2 = v2light_pollution(0.1,0,1,5,7,[[2,1,0,5,10]])

urban_1 = [10,10,8,5,6,urban_2,calc_risk(urban_2)]
suburban_2 = [7,5,10,5,9,suburban_2,calc_risk(suburban_2)]
rural_3 =[2,1,3,5,10,rural_2,calc_risk(rural_2)]
protected_4 =[0.1,0,1,5,7,protected_2,calc_risk(protected_2)]


data2 = [urban_1,suburban_2,rural_3,protected_4]


#Creating a second CSV
params = ['pop_density','build_density','road_density', 'lightybrity','area','light-estimation','risk-assesment']
df = pd.DataFrame(data2,columns=params)
df = df.set_index('risk-assesment')
df.to_csv('./DBdataset2.csv')