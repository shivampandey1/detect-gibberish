#!/usr/bin/python

import pickle
import gib_detect_train

model_data = pickle.load(open('gib_model.pki', 'rb'))

print("shakesperean is good, spanish is bad. type in stop to exit the program")
while True:
    l = input()
    if l == "stop":
        break
    model_mat = model_data['mat']
    threshold = model_data['thresh']
    print(gib_detect_train.avg_transition_prob(l, model_mat) > threshold)
    
print('thanks for trying my model! :)')
