class Link:
    
    def __init__(self,name:str, tpup:float,latup:float,tpdown:float,latdown:float) -> None:
        self.name=name
        # Basic uplink and downlink parameters
        self.throughputup=tpup
        self.latencyup=latup
        self.throughputdown=tpdown
        self.latencydown=latdown

        # Variables to keep track of the queue waiting to be sent
        self.timeavailup=0
        self.timeavaildown=0

    # 
    def getparams_up(self,time):
        return (self.throughputup,self.latencyup)

    def upload(self,time,size):
        # Get the bandwidth and latency at this time
        bandwidth,latency=self.getparams_up(time)

        ttransmit=latency+size/bandwidth*1000
        timeavailup=self.timeavailup
        if time>timeavailup:
            timeavailup=time+ttransmit
        else:
            timeavailup+=ttransmit

        return timeavailup

    def upload_commit(self,time,size):
        self.timeavailup=self.upload(time,size)
        return self.timeavailup

    def getparams_down(self,time):
        return (self.throughputdown,self.latencydown)

    def download(self,time,size):
        # Get the bandwidth and latency at this time
        bandwidth,latency=self.getparams_down(time)

        ttransmit=latency+size/bandwidth*1000
        timeavaildown=self.timeavaildown
        if time>timeavaildown:
            timeavaildown=time+ttransmit
        else:
            timeavaildown+=ttransmit

        return timeavaildown

    def download_commit(self,time,size):
        self.timeavaildown=self.download(time,size)
        return self.timeavaildown


