import scipy as sp

class sGrid:

	gridCount = 0

	def __init__(self, jmax=11, kmax=1, lmax=1):
		self.jmax = jmax
		sGrid.gridCount += 1
		self.KminCurve = None

	def initKminCurve(self,curve=None):
		if curve is None:
			jj = self.jmax
			x = sp.linspace(0,1,self.jmax)
			y = sp.zero_like(x)
			z = sp.zeros_like(x)
			curve = sp.vstack(x,y,z)

		self.KminCurve = curve

	def redist(self,ds1=0.1,sr=1.2,ds2=0.2,n=11):
		ksi = sp.linspace(0,1,n)
		s  = 1 + sp.tanh(sr*(ksi-1))/sp.tanh(sr)
		self.KminCurve = s*(self.KminCurve[-1]-self.KminCurve[0]) + self.KminCurve[0]



		







