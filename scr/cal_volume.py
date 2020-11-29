import numpy as np
import sys
import ast
import os

def find_tri(name_of_meshinfo):
    """
    Function for creating the triangle based on the elements.\n
    """
    sys.path.append(name_of_meshinfo)
    import meshInformation as parameters
    elem_for_volume = []
    print(len(parameters.meshinfo['surfs_netting']))
    for item in parameters.meshinfo['surfs_netting']:
        if len(item) == 3:
            elem_for_volume.append((np.array(item)-1).tolist())
        else:
            elem_for_volume.append((np.array(item)-1).tolist()[0:3])
            elem_for_volume.append((np.array(item)-1).tolist()[1:4])
    print("intial volume is " +
          str(method1(parameters.meshinfo['Nodes_netting'], elem_for_volume)))
    return elem_for_volume



def method1(list_of_nodes, elem):
    """A function to calculate volume of a cage based on scalar triple product method

    Args:
        list_of_nodes (np.array(n,3))|Unit [m]: The coordinates of nodes
        elem (python list)| Unit [-]: The list of index for trigular planes

    Returns:
        scalar |Unit [m3]: volume of a fish cage
    """
    volume = 0
    origin = np.mean(list_of_nodes, axis=0)
    for each in elem:
        A = list_of_nodes[each[0]]-origin
        B = list_of_nodes[each[1]]-origin
        C = list_of_nodes[each[2]]-origin
        volume += 1/6*abs(np.dot(A, np.cross(B, C)))
    return volume


def method2(list_of_nodes, elem):
    """A function to calculate volume of a cage based on divergence method

    Args:
        list_of_nodes (np.array(n,3))|Unit [m]: The coordinates of nodes
        elem (python list)| Unit [-]: The list of index for trigular planes

    Returns:
        scalar |Unit [m3]: volume of a fish cage
    """
    volume = 0
    origin = np.mean(list_of_nodes, axis=0)
    for each in elem:
        p1 = list_of_nodes[each[0]]
        p2 = list_of_nodes[each[1]]
        p3 = list_of_nodes[each[2]]
        v1 = p1-p2
        v2 = p1-p3
        center = (p1+p2+p3)/3.0
        area = 0.5*np.linalg.norm(np.cross(v1, v2))
        normal_vector = np.cross(v1, v2)/np.linalg.norm(np.cross(v1, v2))
        if np.dot(normal_vector, center-origin) < 0:
            normal_vector = -normal_vector
        volume += np.dot(normal_vector,
                         np.array([1*center[0], 0*center[1], 0*center[2]]))*area
    return volume


if __name__ == "__main__":
    print(os.getcwd())
    # path_to_result='E:\\UbuntuFiles\\roxelaqua\\U0.4\\asterinput'
    path_to_case='.\\U0.7'
    # path_to_result='.\\U0.4\\asterinput'
    elem111=find_tri(os.path.join(path_to_case,'asterinput'))
    dt=0.02
    tend=100
    t=[]
    volume=[]
    for k in range(int(tend/dt)):
        # posi_files='E:\\UbuntuFiles\\roxelaqua\\U0.4\\pythonOutput\\posi_'+str(i)+'.0.txt'
        posi_files= os.path.join(os.path.join(path_to_case,'pythonOutput'),'posi_'+str(round((k)*dt,3))+'.txt')
        posi=np.loadtxt(posi_files)
        t.append(round((k)*dt,3))
        volume.append(method1(posi,elem111))
        print(round((k)*dt,3))

    np.savez(os.path.join(path_to_case,'result_volume2'),time=t,volume=volume)
    print(np.mean(np.array(volume)))
    print(np.max(np.array(volume)))
    print(np.min(np.array(volume)))
    print(np.std(np.array(volume)))