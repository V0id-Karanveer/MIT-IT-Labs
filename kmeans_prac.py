import pandas
import numpy as np

def kmeans(data,k,max_iters=100):
    centroids = data[np.random.choice(len(data),k,replace=False)]
    for _ in range(max_iters):
        dist = np.sqrt(((data-centroids[:,np.newaxis])**2).sum(axis = 2))
        closest_center = np.argmin(dist,axis=0)
        clusters = [data[closest_center == i] for i in range(k)]
        new_centers = np.array([np.mean(cluster,axis=0) for cluster in clusters])
        if np.allclose(centroids,new_centers):
            break
        centroids = new_centers
    return centroids,clusters

df = pandas.read_excel("kmeans.xlsx")
data = df[['X','Y']].to_numpy()

centroids,clusters = kmeans(data,2)
for i,j in enumerate(clusters):
    print(i," ",j)
    print("\n")
