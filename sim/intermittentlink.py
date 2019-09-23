import random
import math
from sim.randomlink import RandomLink

class IntermittentLink(RandomLink):

    def __init__(self,name:str, tpup:float, vartpup:float, latup:float,
            varlatup:float, tpdown:float, vartpdown:float, latdown:float,
            varlatdown:float, problink:float) -> None:
        super().__init__(name,tpup,vartpup,latup,varlatup,tpdown,vartpdown,latdown,varlatdown)
        self.availability={}
        self.problink=problink

    def getparams_up(self,time):
        tp,lat=super().getparams_up(time)
        if round(time) not in self.availability:
            var=random.uniform(0, 1)
            if var<self.problink:
                self.availability[round(time)]=1
            else:
                self.availability[round(time)]=0
        if self.availability[round(time)]==0:
            return 0.00000000000001,0
        else:
            return tp,lat

    def getparams_down(self,time):
        tp,lat=super().getparams_down(time)
        if round(time) not in self.availability:
            var=random.uniform(0, 1)
            if var<self.problink:
                self.availability[round(time)]=1
            else:
                self.availability[round(time)]=0
        if self.availability[round(time)]==0:
            return 0.00000000000001,0
        else:
            return tp,lat

