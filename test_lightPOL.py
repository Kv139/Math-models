
def lp(sc, pop_d, tot_a, adj_loc):
    adj_spaces = 1
    local_pol = 0
    local_pol = float(sc * pop_d * tot_a)
    for i in adj_loc:
        for j in i:
            adj_spaces = adj_spaces * j
    return(adj_spaces + local_pol)



scalar = 1.0
pop_density = 80000
total_area = 643.78

adj_spaces = [[1,500,4000],[.5,.5,2000]]

print(lp(scalar,pop_density,total_area,adj_spaces))

#SQM measurements range from 16 - 22 with 22 being the lease amount
# of light pllution

# TEST CASE SAN FERNANDO CA - SQM = 18.35 mag./arc sec^2
# actual SQM = (how much light hits the sensor)
# Amount of light into untis of magnitudes  per square arc-second
# The larger the number read on the meter display, the darker the sky

area = 2.37 #San Fernando miles
pop_density = 23726/ area # density per mile
sqm_f = 18.35
alpha = 1 #TBD

fernando = [1,area, pop_density]
#Near by populations (arleta, Norhtridge)

area_arleta = 3.1
pop_density_a = 103683/3.1
sqm_a = 18.31

arleta = [1,area_arleta,pop_density_a ]

area_forest = 1094
pop_desity_f = 1
sqm_for = 20.27

forest = [1,area_forest,pop_desity_f]

adj_spaces_forest= [fernando, arleta]
adj_spaces_fernando= [forest, arleta]
adj_spaces_arleta= [fernando, forest]

actual_LP = [sqm_f,sqm_a,sqm_for]

modelscoreA=lp(arleta[0],arleta[1],arleta[2], adj_spaces_arleta)
modelscoreFERN=lp(fernando[0],fernando[1],fernando[2], adj_spaces_fernando)
modelscoreFor=lp(forest[0],forest[1],forest[2], adj_spaces_forest)

results = [modelscoreFERN,modelscoreA,modelscoreFor]
labels = ["Ferndale: ", "Arleta: ", "Forest: "]

for i in range(0,len(results)):
    print("Algorithm produced for:",labels[i], results[i], "Actual Pollution is:", actual_LP[i])






