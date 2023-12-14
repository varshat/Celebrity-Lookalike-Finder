import os
import pickle

actors = os.listdir('data')

filenames = []

#loop through the folders and find the append the each actor folder to a list
for actor in actors:
    for file in os.listdir(os.path.join('data',actor)):
        filenames.append(os.path.join('data',actor,file))

pickle.dump(filenames,open('filenames.pkl','wb'))

