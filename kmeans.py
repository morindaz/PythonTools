    X_embedded = MDS(random_state=0,dissimilarity='euclidean').fit_transform(X)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X_embedded)
    y = kmeans.labels_
    centers = kmeans.cluster_centers_
#    color = ['r','y','k','b','g']
#    color_ = ['red point','yellow point','black point','blue point','green point']
#    fig = pl.figure()
#    ax = fig.add_subplot(111)
#    ax.set_title('frame clustering')
#    for j in range(5):
#        z = np.argwhere(y==j)
#        ax.scatter(X_embedded[z,0],X_embedded[z,1],c = color[j],marker = 'o')
#    pl.show()