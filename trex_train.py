import glob
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns

# for warnings
import warnings
warnings.filterwarnings("ignore")

imgs = glob.glob("./img/*.png")

# img size
width = 250
height = 100

X = []
Y = []

for img in imgs:
    
    fileName = os.path.basename(img)
    label = fileName.split('_')[0] 
    
    # "L" for grayscale. normalized with 255
    im = np.array(Image.open(img).convert("L").resize((width, height))) / 255
    X.append(im)
    Y.append(label)

X = np.array(X)
X = X.reshape(X.shape[0], width, height, 1)  # 1 is channel

def onehotLabels(values):
    labelEncoder = LabelEncoder()
    integerEncoded = labelEncoder.fit_transform(values)
    onehotEncoder = OneHotEncoder(sparse=False)
    integerEncoded = integerEncoded.reshape(len(integerEncoded), 1)
    onehot_encoded = onehotEncoder.fit_transform(integerEncoded)
    return onehot_encoded

Y = onehotLabels(Y)

#train_test_split
trainX, testX, trainY, testY = train_test_split(X, Y, test_size = 0.25, random_state = 2)  


# CNN Model
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(width, height, 1)))
model.add(Conv2D(64, kernel_size=(3,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.4))
model.add(Dense(3, activation="softmax"))      

model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics= ["accuracy"])  

model.fit(trainX, trainY, epochs=35, batch_size=64)

# Load Trained Weights
# if os.path.exists("./trex_weight.h5"):
#     model.load_weights("trex_weight.h5")
#     print("Weights loaded.")    

score_train = model.evaluate(trainX, trainY)
print("Training Accuracy: %",score_train[1]*100)    
    
score_test = model.evaluate(testX, testY)
print("Test Accuracy: %",score_test[1]*100)  


open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.h5")   


























