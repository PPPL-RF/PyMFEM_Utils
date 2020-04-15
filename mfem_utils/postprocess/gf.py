import numpy as np

def griddata_from_scalar_gf(meshfile, gffile,
                            origin=(0,0,0), e1=(1, 0, 0), e2=(0,1,0),
                            x=(0, 1), y=(0, 1),
                            ndimx=100, ndimy=100, do_plot=False ):
    '''
    collect dat from 
       point = origin + e1 * x + e2 * y
       e1 : vector for x axis
       e2 : vector for y axis
       x  : xmin and xmax
       y  : ymin and ymax
       ndimx : number of x grid
       ndimy : number of y grid

    '''
    import mfem.ser as mfem

    mesh = mfem.Mesh(meshfile)
    gf = mfem.GridFunction(mesh, gffile)


    x = np.linspace(x[0], x[1], ndimx)
    y = np.linspace(y[0], y[1], ndimy)
    X, Y = np.meshgrid(x, y)
    e1 = np.array(e1, copy=False)
    e2 = np.array(e2, copy=False)    
    ptx = (np.array(origin, copy=False) + e1*X.reshape(-1,1) + e2*Y.reshape(-1,1))
    
    count, elem, int_points = mesh.FindPoints(ptx)

    data = np.array([gf.GetValue(e, i) for e, i in zip(elem, int_points)]).reshape(X.shape)
    if do_plot:
        from ifigur.interative import figure
        v = figure()
        v.image(x, y, data)


    return ptx, data
