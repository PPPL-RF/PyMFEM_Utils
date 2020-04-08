import numpy as np

from petram.mfem_config import use_parallel
if use_parallel:
   import mfem.par as mfem   
else:
   import mfem.ser as mfem

def get_edge_vertex_indices(mesh):
    '''
    return vertex index of edges
    '''
    return np.array([mesh.GetEdgeVertices(iedge) for iedge in range(mesh.GetNEdges())])


def get_edge_length(mesh):
    '''
    compute the length of all edges
    '''
    from mfem_utils.mesh.vertex import get_meshvertices
    
    vv = get_meshvertices(mesh)
    idx = get_edge_vertex_indices(mesh)

    vv1 = vv[idx[:,0]]
    vv2 = vv[idx[:,1]]
    return np.sqrt(np.sum((vv1-vv2)**2, -1))
    

def find_smalledge_loc(mesh, frac = 1e-5):
    '''
    find the location of small edges
    '''
    from mfem_utils.mesh.vertex import get_meshvertices
    
    vv = get_meshvertices(mesh)
    idx = get_edge_vertex_indices(mesh)
    elen = get_edge_length(mesh)

    ratio = elen/np.max(elen)

    ii = np.where(ratio < frac)[0]
    
    return (vv[idx[ii,0]]+ vv[idx[ii,1]])/2.0
