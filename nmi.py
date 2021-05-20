import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn import datasets

wine    = datasets.load_wine()
hc      = AgglomerativeClustering(n_clusters=3, linkage='ward')
hc.fit(wine.data)
ans     = hc.fit_predict(wine.data)
eval    = normalized_mutual_info_score(ans, wine.target)
print('wine          :', eval)

wine    = datasets.load_wine()
hc      = AgglomerativeClustering(n_clusters=3, linkage='single')
hc.fit(wine.data)
ans     = hc.fit_predict(wine.data)
eval    = normalized_mutual_info_score(ans, wine.target)
print('single-link   :', eval)

wine    = datasets.load_wine()
hc      = AgglomerativeClustering(n_clusters=3, linkage='complete')
hc.fit(wine.data)
ans     = hc.fit_predict(wine.data)
eval    = normalized_mutual_info_score(ans, wine.target)
print('complete-link :', eval)

wine    = datasets.load_wine()
hc      = AgglomerativeClustering(n_clusters=3, linkage='average')
hc.fit(wine.data)
ans     = hc.fit_predict(wine.data)
eval    = normalized_mutual_info_score(ans, wine.target)
print('average       :', eval)
