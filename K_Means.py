import pandas as pd
from sklearn.cluster import KMeans

wholesale = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv', header=None)
tmp1 = wholesale.drop([0])# Remoção das labels para poder introduzir os dados ao KMeans # Em outros exemplos isso é X

kmeans = []
ajustesK = []
clustersK = []

for i in range(2,8):# Repetição
    kmeans = KMeans(n_clusters=i)# Inicialização
    tmp2 = kmeans.fit(tmp1)# KMeans labelado para os clusters de vários tamanhos
    tmp3 = tmp2.labels_# Resultado com os labels do kmeans.fit(tmp1)
    ajustesK.append(tmp2)# Atualização
    clustersK.append(tmp3)# Alocação

K_SET = set(kmeans.predict(tmp1))
print("Esse data set possui" , len(K_SET), " clusters diferentes!")





