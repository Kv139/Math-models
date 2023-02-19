import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def area_pollution(sc,total_area,pod_d, adjacent_locations):
    adj_escaped_light = 1
    local_pol = (sc * pod_d * total_area)/total_area #pollution per mile FUCKKKK
    for i in adjacent_locations:
        for j in i:
            adj_escaped_light =adj_escaped_light * j
    adj_escaped_light = adj_escaped_light * .1 # only ten percent of generated light actually escapes
    if(local_pol == 0):
        #protected area = protective factor
        return((adj_escaped_light/total_area)*.001)
    else:
        return((adj_escaped_light/total_area) + local_pol)

pop_density = 23726/ 2.37 # density per mile
sqm_f = 18.35
alpha = 1 #TBD

fernando = [1,2.37, pop_density]
#Near by populations (arleta, Norhtridge)

area_arleta = 3.1
pop_density_a = 103683/3.1
sqm_a = 18.31

arleta = [1,3.1,pop_density_a ]

area_forest = 1094
sqm_for = 20.27

forest = [1,1094,0]

adj_spaces_forest= [fernando, arleta]
adj_spaces_fernando= [forest, arleta]
adj_spaces_arleta= [fernando, forest]

actual_LP = [sqm_f,sqm_a,sqm_for]


modelscoreA=area_pollution(arleta[0],arleta[1],arleta[2], adj_spaces_arleta)
modelscoreFERN=area_pollution(fernando[0],fernando[1],fernando[2], adj_spaces_fernando)
modelscoreFor=area_pollution(forest[0],forest[1],forest[2], adj_spaces_forest)

results = [modelscoreFERN,modelscoreA,modelscoreFor]
labels = ["Ferndale: ", "Arleta: ", "Forest: "]

#for i in range(0,len(results)):
 #   print("Algorithm produced for:",labels[i], results[i], "Actual Pollution is:", actual_LP[i])

def v2light_pollution(pop_density,build_density,road_density,bright_light,area,adj_pol):
    sum = (pop_density**3 + build_density**2 + road_density**2)*bright_light * area
    outside_light = 1
    if len(adj_pol) == 0:
        return(sum)
    for i in adj_pol:
        outside_light += calculate_adjacency(i)
    return(outside_light + sum)

def calculate_adjacency(matrix):
    sum = matrix[3]*(matrix[0]**3 + matrix[1]**2 + matrix[2]**2) * .1 * matrix[3]
    return sum

def calc_risk(light_estimate):
    risk = 10*(1-(abs(132001.0 - light_estimate)/132001.0))
    return risk


print("TESTING FUCK TION")
#print("This is a protected land closer to populated area")
#print(v2light_pollution(1,3,2,1,1,[[9,9,9,9,2],[8,8,8,8,3]]))
#print("This is like an urban area by nothingness LIKE MY SOUL")
#print(v2light_pollution(9,9,9,9,1,[[1,1,1,1,1],[2,2,3,1,1]]))
#print(v2light_pollution(8,8,8,8,1,[[1,1,1,1,1],[2,2,3,1,1]]))



empty_adj = []
max_caseN = v2light_pollution(10,10,10,10,10,[[10,10,10,10,10]])
max_case = [10,10,10,10,10,max_caseN,10]

#params = ['pop_density','build_density','road_density', 'lightybrity','area','light-estimation']
urban_l = v2light_pollution(10,10,8,10,10,[[7,5,10,10,3]])
suburban_l = v2light_pollution(7,5,10,10,10,[[10,10,8,10,1],[2,1,3,10,10]])
rural_1 = v2light_pollution(2,1,3,10,10,[[10,10,8,10,1],[.1,0,1,10,7]])
protected_1 = v2light_pollution(0.1,0,1,10,7,[[10,10,8,10,1]])

print("Urban risk with area=1 ",calc_risk(urban_l))
print("suburban risk with area=1 " ,calc_risk(suburban_l))

urban = [10,10,8,10,1,urban_l,calc_risk(urban_l)]
suburban = [7,5,10,10,1,suburban_l,calc_risk(suburban_l)]
rural =[2,1,3,10,10,rural_1,calc_risk(rural_1)]
protected =[0.1,0,1,10,7,protected_1,calc_risk(protected_1)]

data2 = [max_case,urban,suburban,rural,protected]



params = ['pop_density','build_density','road_density', 'lightybrity','area','light-estimation','risk-assesment']
df = pd.DataFrame(data2,columns=params)
df.to_csv('./dataset.csv')


triples=pd.read_csv("./dataset.csv")

# Need to find a good way to visualize
# Also more data variations, along with negative
# instances to make the data more interesting!

#sns.catplot(data=triples,kind='swarm', x='mew',y='total',hue='lam')
#sns.relplot(
 #       alpha=.5, palette="muted",
  #     height=5, data=triples)
#plt.show()
