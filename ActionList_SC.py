import numpy as np

def creat_action_list():
    action_list = []
    action_list.append((300, np.array([1,0,0])))
    action_list.append((225, np.array([0,0,0])))
    action_list.append((87, np.array([1,1,0])))
    action_list.append((40, np.array([0,0,0])))
    action_list.append((40, np.array([0,0,1])))
    return action_list
