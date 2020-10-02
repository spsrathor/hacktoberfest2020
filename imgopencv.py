import cv2 
img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


model = tf.keras.models.load_model("rps_sentdex.model")
path=r'E:path\rps_training\rock\rock01-000.png'
prediction = model.predict([prepare(path)])
#print(prediction[0])
a=np.ndarray.tolist(prediction[0])
print(a)
for i in range(0,3):
    if a[i]==1.0:
        print(CATEGORIES[i])
        output=CATEGORIES[i]
img = cv2.imread(path,3)
org = (10, 20)
fontScale = 1
color = (0, 0, 223)
thickness = 4


import numpy as np
import cv2
import tensorflow as tf

model = tf.keras.models.load_model("rps_sentdex.model")
CATEGORIES = ["paper", "rock","scissors"]
font = cv2.FONT_HERSHEY_SIMPLEX
