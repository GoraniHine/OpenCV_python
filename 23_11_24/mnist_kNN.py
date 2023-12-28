#10.3.2
import cv2, numpy as np
import pickle, gzip, os
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

def load_mnist(filename):
    if not os.path.exists(filename):
        print("Downloading")
        link = "http://figshare.com/ndownloader/files/25635053"
        urlretrieve(link, filename)
    with gzip.open(filename, 'rb') as f:
        return pickle.load(f, encoding = 'latin1')

def graph_image(data, lable, title, nsample):
    plt.figure(num = title, figsize = (10, 10))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28)
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.imshow(img, cmap = 'gray')
        plt.title("%s: %d" % (title, lable[id]))
    plt.tight_layout()

train_set, valid_set, test_set = load_mnist("mnist.pk1.gz")
train_data, train_lable, = train_set
test_data, test_lable = test_set

print("train_set >=",train_set[0].shape)
print("valid_set >=",valid_set[0].shape)
print("test_set >=",test_set[0].shape)

print("training")
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_lable)

nsample = 100
print("%d 개 predicting..." % nsample)
_, resp, _ , _ = knn.findNearest(test_data[:nsample], k = 5)
accur = sum(resp.flatten() == test_lable[:nsample])

print("정확도 =", accur / nsample * 100, '%')
graph_image(train_data, train_lable, 'label', 24)
graph_image(test_data[:nsample], resp, 'predict', 24)
plt.show()