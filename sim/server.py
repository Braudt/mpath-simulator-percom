class Server:
    
    def __init__(self,name,CPU):
        self.name=name
        self.CPU=CPU
        self.timeavailable=0

    def compute(self,time,complexity):
        timeavailable=self.timeavailable
        if time>timeavailable:
            timeavailable=time+complexity/self.CPU*1000
        else:
            timeavailable+=complexity/self.CPU*1000
        return timeavailable

    def compute_commit(self,time,complexity):
        self.timeavailable=self.compute(time,complexity)
        return self.timeavailable

