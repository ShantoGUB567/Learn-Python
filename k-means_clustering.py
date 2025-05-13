import random

# Sample data points (2D)
data = [
    [1, 2],
    [2, 1],
    [3, 1],
    [6, 5],
    [7, 7],
    [8, 6]
]

# Read data from local file 
# import csv

# data = []
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         point = [float(x) for x in row]
#         data.append(point)

# Read data from online/github
# import requests

# url = 'https://raw.githubusercontent.com/yourusername/yourrepo/main/data.csv'
# response = requests.get(url)
# lines = response.text.strip().split('\n')

# data = []
# for line in lines:
#     x, y = map(float, line.split(','))
#     data.append([x, y])

# Read data from local using Panda
# import pandas as pd

# df = pd.read_csv('data.csv')
# data = df.values.tolist()

#  User input
# n = int(input("Enter number of points: "))
# data = []
# for _ in range(n):
#     x, y = map(float, input("Enter x y: ").split())
#     data.append([x, y])



# Number of clusters
K = 4

# Randomly initialize K centroids
centroids = random.sample(data, K)

# Function to calculate Euclidean distance
def euclidean(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

while True:
    # Step 1: Assign points to nearest centroid
    clusters = [[] for _ in range(K)]
    for point in data:
        distances = [euclidean(point, c) for c in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    
    # Step 2: Calculate new centroids
    new_centroids = []
    for cluster in clusters:
        x_vals = [p[0] for p in cluster]
        y_vals = [p[1] for p in cluster]
        avg_x = sum(x_vals) / len(x_vals)
        avg_y = sum(y_vals) / len(y_vals)
        new_centroids.append([avg_x, avg_y])
    
    # Step 3: Check if centroids have changed
    if new_centroids == centroids:
        break  # Stop if centroids did not change
    else:
        centroids = new_centroids

# Print the final clusters
for i, cluster in enumerate(clusters):
    print(f"\nCluster {i+1}:")
    for point in cluster:
        print(point)

print("\nFinal centroids:", centroids)
