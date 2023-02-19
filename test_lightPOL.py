import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




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

for i in range(0,len(results)):
    print("Algorithm produced for:",labels[i], results[i], "Actual Pollution is:", actual_LP[i])

def v2light_pollution(pop_density,build_density,road_density,bright_light,adj_pol):
    sum = (pop_density**3 + build_density**2 + road_density**2)*bright_light
    outside_light = 1
    for i in adj_pol:
        outside_light += calculate_adjacency(i)
    return(outside_light + sum)

def calculate_adjacency(matrix):
    sum = matrix[3]*(matrix[0]**3 + matrix[1]**2 + matrix[2]**2) * .1
    return sum


print("TESTING FUCK TION")
print("This is a protected land closer to populated area")
print(v2light_pollution(1,3,2,1,[[9,9,9,9],[8,8,8,8]]))
print("This is like an urban area by nothingness LIKE MY SOUL")
print(v2light_pollution(9,9,9,9,[[1,1,1,1],[2,2,3,1]]))
print(v2light_pollution(8,8,8,8,[[1,1,1,1],[2,2,3,1]]))

#print(v2light_pollution(1,3,2,1,[[9,9,9,9],[8,8,8,8]]))


data2 = [[1,3,2,1,1328.9],[9,9,9,9,8022.4],[8,8,8,8,0]]

params = ['pop_density','build_density','road_density', 'lightybrity','light-estimation']
df = pd.DataFrame(data2,columns=params)
df.to_csv('./dataset.csv')


triples=pd.read_csv("./dataset.csv")

# Need to find a good way to visualize
# Also more data variations, along with negative 
# instances to make the data more interesting!

#sns.catplot(data=triples,kind='swarm', x='mew',y='total',hue='lam')
sns.relplot(x="mew", y="lam", hue="total",
        alpha=.5, palette="muted",
        height=5, data=triples)

plt.show()


