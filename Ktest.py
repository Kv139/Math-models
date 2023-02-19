import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from test import v2light_pollution
from test import calculate_adjacency
from test import calc_risk


urban_3 = v2light_pollution(7.5,10,8,10,6,[[4.5,5,10,10,9]])
suburban_3 = v2light_pollution(4.5,5,10,10,9,[[7.5,10,8,10,6],[2,1,3,10,10]])
rural_3 = v2light_pollution(2,1,3,10,10,[[4.5,5,10,10,9],[0.1,0,1,10,7]])
protected_3 = v2light_pollution(0.1,0,1,10,7,[[2,1,3,10,10]])

urban_1 = [7.5,10,8,10,6,urban_3,calc_risk(urban_3)]
suburban_2 = [4.5,5,10,10,9,suburban_3,calc_risk(suburban_3)]
rural_3 =[2,1,3,10,10,rural_3,calc_risk(rural_3)]
protected_4 =[0.1,0,1,10,7,protected_3,calc_risk(protected_3)]


data4 = [urban_1,suburban_2,rural_3,protected_4]


#Creating a second CSV
params = ['pop_density','build_density','road_density', 'lightybrity','area','light-estimation','risk-assesment']
df = pd.DataFrame(data4,columns=params)
df = df.set_index('risk-assesment')
df.to_csv('./Kdataset4.csv')