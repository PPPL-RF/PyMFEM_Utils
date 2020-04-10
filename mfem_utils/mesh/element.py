import numpy as np

def get_element_sizes(mesh):
    ele_size=np.array([mesh.GetElementSize(i) for i in range(mesh.GetNE())])


def get_element_loc(mesh, index, mean = True):
    ptx = np.vstack([mesh.GetVertexArray(i) for i in mesh.GetElementVertices(index)])
    if mean:
       ptx = np.mean(ptx, 0)
    return ptx
