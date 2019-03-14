import numpy as np

def creat_action_list():
    action_list = []
    action_list.append((150, np.array([1,0,0])))
    action_list.append((30, np.array([1,1,0])))
    action_list.append((85, np.array([1,0,0])))
    action_list.append((25, np.array([1,-1,0])))
    action_list.append((40, np.array([1,0,0])))
    action_list.append((50, np.array([0,0,0])))
    action_list.append((3, np.array([0,-1,0])))
    action_list.append((370, np.array([0,0,0])))
    action_list.append((90, np.array([1,1,0])))
    action_list.append((20, np.array([0,0,0])))
    action_list.append((10, np.array([0,-1,0])))
    action_list.append((20, np.array([0,0,0])))
    action_list.append((30, np.array([0,0,1])))
    return action_list
