import numpy as np
import matplotlib.pyplot as plt
from SimCityEnv import SimCityEnv
from ActionList_TL import creat_action_list

env = SimCityEnv('./TrafficLightEnv/TrafficLight.x86_64')
env.seed(0)
ob, _, _, _ = env.reset()

action_list = creat_action_list()

for kv in action_list:
    step = kv[0]
    action = kv[1]
    for i in range(step):
        ob, reward, done, _ = env.step(action)
        print(i, ob[-1], action, reward, done)
#        if i > 0 and i % 100 == 0:
        if i == 300:
            plt.figure(1)
            plt.subplot(2, 3, 1).imshow(ob[0])
            plt.subplot(2, 3, 2).imshow(ob[1])
            plt.subplot(2, 3, 3).imshow(ob[2])
            plt.subplot(2, 3, 4).imshow(ob[3])
            plt.subplot(2, 3, 5).imshow(ob[4])
            plt.show()

env.close()

