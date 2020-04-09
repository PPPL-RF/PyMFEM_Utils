import numpy as np

from petram.mfem_config import use_parallel
if use_parallel:
   import mfem.par as mfem   
else:
   import mfem.ser as mfem


def get_meshvertices(mesh):
    '''
    return mesh verteices as an numpy array
    '''
    v = mfem.Vector()
    mesh.GetVertices(v)
    vv = v.GetDataArray().copy()
    vv = vv.reshape(3, -1).transpose()
    return vv
    

