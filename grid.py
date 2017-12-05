import scipy as sp

class Curve:
    ''' Curve data type and operations '''

    def __init__(self,definition=None,np=11,feature=False):
        self.np = np

        if definition is None:
            #Make up one based on default values 
            np = self.np
            x = sp.linspace(0,1,np)
            y = sp.zeros_like(x)
            z = sp.zeros_like(x)
            self.defCurveXYZ = sp.concatenate((x,y,z))
        # elif type(definition) is list or numpy.ndarray:
        # curve is defined as a set of discrete points. Use them. ignore np. Or interpolate?
        # elif type(definition) is string
        # curve is defined by a python expressions t=[0,1]; x=x(t); y=y(t); z=z(t). Eval. it
        # tip: Consider using x,y,z,=t as the default when definition==None. 

        if feature is True: #This is a feature curve
            self.feat = True
            #Consider this as the best definition available.
        else:
            self.feat = False

    def __str__(self):
        sp.set_printoptions(precision=8)
        return self.defCurveXYZ.__str__()

class Grid:
    '''structured grid data and operations.'''

    totalGridCount = 0

    def __init__(self, jmax=11, kmax=1, lmax=1):
        Grid.totalGridCount += 1
        self.gridNumber = Grid.totalGridCount
        #Maximum indices in each direction. Minimum is 1 for all.
        self.jmax_ind=jmax
        self.kmax_ind=kmax
        self.lmax_ind=lmax
        
        #Curves that bound a JK-surface grid
        self.bnd_cur = ('jmin_cur', 'jmax_cur', 'kmin_cur', 'kmax_cur')

        for attr in self.bnd_cur:
            setattr(self,attr,None)

    def defineBoundary(self,boundary=None,definition=None):

        if boundary in self.bnd_cur:
            if getattr(self,boundary):
                print("WARNING: {0:%s} boundary for grid {1:%d} is already defined.".format(self.boundary,self.gridNumber))
            setattr(self,boundary,Curve())
        else:
            print("ERROR: The boundary must be specified as one of these: %s".format(self.bnd_cur))

    def redist(self,curve,ds1=0.1,sr=1.2,ds2=0.2,n=11):
        ksi = sp.linspace(0,1,n)
        s  = 1 + sp.tanh(sr*(ksi-1))/sp.tanh(sr)
        curve_redist = s*(curve[-1]-curve[0]) + curve[0]



        







