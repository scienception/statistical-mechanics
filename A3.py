import random

print('more "elegant" solution')
coordinates=[0]*3
alpha=0
delta = 0.1
n_trials = 1000000
n_hits = 0
deltas=[0]*3

for a in range (6):
    for i in range(n_trials):

        #gets random deltas, and random alpha for 4th dimension
        deltas=[random.uniform(-delta, delta) for coordinate in deltas]
        alpha=random.uniform(-1.0, 1.0)
    
        #sum of the (n-1) first components
        sum_components=sum((coordinates[j]+deltas[j])**2 for j in range(3))

        #if the sample is inside the cylinder
        if sum_components< 1.0:
          coordinates=[coordinates[z]+deltas[z] for z in range(3)]

        #if the sample is inside the sphere
        if (sum_components+alpha**2)< 1.0:
            n_hits += 1
        
    print (2.0 * float(n_hits) / float(n_trials)) #2V_sph(4)/V_cyl(4) where V_sph=hits Vcyl=trials
    coordinates=[0]*3
    n_hits = 0

x, y,z, alpha = 0.0, 0.0,0.0,0.0
delta = 0.1
n_trials = 1000000
n_hits = 0
      
print("typical solution. There's redundacy in the code.")
for k in range (6):
    for i in range(n_trials):

        #gets random deltas, and random alpha for 4th dimension
        del_x, del_y, del_z, alpha = random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-delta, delta), random.uniform(-1, 1)

        #if the sample is inside the cylinder
        if ((x + del_x)**2+(y + del_y)**2+(z + del_z)**2)< 1.0: 
          x, y, z= x + del_x, y + del_y, z + del_z

        #if the sample is inside the sphere
        if (x**2+y**2+z**2+alpha**2)< 1.0:
            n_hits += 1
    print (2.0 * n_hits / float(n_trials)) #2V_sph(4)/V_cyl(4) where V_sph=hits Vcyl=trials
    x, y,z, alpha = 0.0, 0.0,0.0,0.0
    n_hits = 0





