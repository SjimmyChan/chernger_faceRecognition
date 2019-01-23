#-*-coding:utf8-*-
from dataSet import DataSet
from keras.models import Sequential,load_model
from keras.layers import Dense,Activation,Convolution2D,MaxPooling2D,Flatten,Dropout
from photo_shot import check_user_exist
import numpy as np

#create CNN base on face recognition
class Model(object):
    FILE_PATH = "C:\\Users\\CN\\Desktop\\intern\\chernger_faceRecognition\\model\\model.h5"
    IMAGE_SIZE = 128    #picture pixel limit

    def __init__(self):
        self.model = None

    # def set_userName(self,name):
    #     FILE_PATH = "C:\\Users\\CN\\Desktop\\intern\\chernger_faceRecognition\\dataset\\%s\\%s" % (name, FILE_PATH)   #model read, model store

    #read dataset for training source
    def read_trainData(self,dataset):
        self.dataset = dataset

    #create CNN module : 1 conv -> 1 pooling -> 1 conv -> 1 pooling -> flatten -> fully connected
    def build_model(self):
        self.model = Sequential()
        self.model.add(
            Convolution2D(
                filters=32,
                kernel_size=(5, 5),
                padding='same',
                dim_ordering='th',
                input_shape=self.dataset.X_train.shape[1:]
            )
        )

        self.model.add(Activation('relu'))
        self.model.add(
            MaxPooling2D(
                pool_size=(2, 2),
                strides=(2, 2),
                padding='same'
            )
        )    

        self.model.add(Convolution2D(filters=64, kernel_size=(5, 5), padding='same'))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'))
        
        self.model.add(Flatten())
        self.model.add(Dense(512))
        self.model.add(Activation('relu'))
        
        self.model.add(Dense(self.dataset.num_classes))
        self.model.add(Activation('softmax'))
        self.model.summary()

    #training
    def train_model(self):
        self.model.compile(
            optimizer='adam',  
            loss='sparse_categorical_crossentropy',  #can compare "squared_hinge" with loss
            metrics=['accuracy'])

        #epochs、batch_size is flexible parameter，epochs = round、 batch_size = number of sample
        self.model.fit(self.dataset.X_train,self.dataset.Y_train,epochs=7,batch_size=20)

    def evaluate_model(self):
        print('\nTesting---------------')
        loss, accuracy = self.model.evaluate(self.dataset.X_test, self.dataset.Y_test)

        print('test loss;', loss)
        print('test accuracy:', accuracy)

    def save(self, file_path = FILE_PATH):
        print('Model Saved.')
        self.model.save(file_path)

    def load(self, file_path = FILE_PATH):
        print('Model Loaded.')
        self.model = load_model(file_path)

    def predict(self,img):
        img = img.reshape((1, 1, self.IMAGE_SIZE, self.IMAGE_SIZE)) #make sure input img is on "channel = 1" and img size is "IMAGE_SIZE"
        img = img.astype('float32')
        img = img/255.0 #img is gray scale

        result = self.model.predict_proba(img)  #calculate img probability in label
        max_index = np.argmax(result) #find highest probability

        return max_index,result[0][max_index] #first parameter = highest probability label，second parameter = probability ratio


if __name__ == '__main__':
    dataset = DataSet("C:\\Users\\CN\\Desktop\\intern\\chernger_faceRecognition\\dataset")
    model = Model()
    model.read_trainData(dataset)
    model.build_model()
    model.train_model()
    model.evaluate_model()
    model.set_userName(user_name)
    model.save()














