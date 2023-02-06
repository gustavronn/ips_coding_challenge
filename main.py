import scipy as sp
import scipy.spatial
import time

radius = 0.05
positions_file = "positions.xyz"

def read_positions(positions_file):
    positions = []
    with open(positions_file, "r") as file:
        for line in file:
            x_y_z = line.split(" ")
            x, y, z = float(x_y_z[0]),float(x_y_z[1]),float(x_y_z[2])
            positions.append([x, y, z])
    return positions

def proximity_check(positions, radius):
    tree = sp.spatial.KDTree(positions)
    indices = []
    no_of_pairs=0
    for i,x in enumerate(positions):
        pairs = tree.query_ball_point(x, radius)
        for j,y in enumerate(pairs):
            if i != y:
                indices.append([i, y])
                no_of_pairs += 1
    return indices, no_of_pairs

cur_time = time.time()
positions = read_positions(positions_file)
indices_time = time.time()-cur_time

cur_time = time.time()
indices, no_of_pairs = proximity_check(positions, radius)
prox_time = time.time()-cur_time

print(indices)
print("Time to read positions       %5.5f"%indices_time)
print("Time to check proximity       %5.5f"%prox_time)
print("Total time                    %5.5f"%(indices_time+prox_time))
print("Number of pairs               %5i"%no_of_pairs)