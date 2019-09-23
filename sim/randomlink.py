import random
import math
from sim.link import Link

class RandomLink(Link):

    def __init__(self,name:str, tpup:float, stdtpup:float, latup:float, stdlatup:float, tpdown:float, stdtpdown:float, latdown:float, stdlatdown:float) -> None:
        super().__init__(name,tpup,latup,tpdown,latdown)
        # The typical stdiance
        self.stdtpup=stdtpup
        self.stdlatup=stdlatup
        self.stdtpdown=stdtpdown
        self.stdlatdown=stdlatdown

        # Dictionary to store the values
        self.randomtpup={}
        self.randomlatup={}
        self.randomtpdown={}
        self.randomlatdown={}

        # Init random
        random.seed(12345)

    def getparams_up(self,time):
        if round(time) not in self.randomtpup:
            self.randomtpup[round(time)]=random.gauss(self.throughputup,self.stdtpup)
        if round(time) not in self.randomlatup:
            self.randomlatup[round(time)]=random.gauss(self.latencyup,self.stdlatup)
        return max(self.randomtpup[round(time)],0.00000000000001),max(self.randomlatup[round(time)],0)

    def getparams_down(self,time):
        if round(time) not in self.randomtpdown:
            self.randomtpdown[round(time)]=random.gauss(self.throughputdown,self.stdtpdown)
        if round(time) not in self.randomlatdown:
            self.randomlatdown[round(time)]=random.gauss(self.latencydown,self.stdlatdown)
        return max(self.randomtpdown[round(time)],0.00000000000001),max(self.randomlatdown[round(time)],0)
