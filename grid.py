import scipy as sp


class Curve:
''' Curve data type and operations '''

	def __init__(self,np=11,feat=None,func=None):
		self.np = np

		if feat is True: #Is a feature curve
			self.feat = True
		else:
			self.feat = False

		if func is None: #Is not defined by a math function. 
			self.func = None
			pass
		else:
			np = self.np
			x = sp.linspace(0,1,np)
			y = sp.zero_like(x)
			z = sp.zeros_like(x)
			defCurve = sp.vstack(x,y,z)






class Grid:
'''structured grid data and operations.'''

	gridCount = 0

	def __init__(self, jmax=11, kmax=1, lmax=1):
		sGrid.gridCount += 1
		self.jmax = jmax
		self.KminCurve = None

	def initKminCurve(self,defCurve=None):
		if defCurve is None:

	
		self.KminCurve = defCurve

	def redist(self,curve,ds1=0.1,sr=1.2,ds2=0.2,n=11):
		ksi = sp.linspace(0,1,n)
		s  = 1 + sp.tanh(sr*(ksi-1))/sp.tanh(sr)
		self.KminCurve = s*(curve[-1]-curve[0]) + curve[0]



		







