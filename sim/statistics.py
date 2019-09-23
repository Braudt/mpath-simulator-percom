class Statistics:

    def __init__(self,name,tasklist,combinations):
        self.name=name
        self.tasklist=tasklist
        self.combinations=combinations
        self.late=0
        self.ontime=0
        self.completion=0
        self.latency=0
        self.total=0
        self.linkdict={}
        self.serverdict={}

    def calcontime(self):
        self.late=0
        self.ontime=0
        self.latency=0
        self.completion=0
        for index,(time,tasks) in enumerate(self.tasklist.items()):
            for t in tasks:
                self.total+=1
                if t.deadline<t.completion:
                    self.late+=1
                    self.latency+=t.completion-t.deadline
                else:
                    self.ontime+=1
                self.completion+=t.completion-t.time

    def calcload(self):
        self.serverdict={}
        self.linkdict={}
        # Fill the load on each server
        for link,server in self.combinations:
            self.linkdict[link.name]=0
            self.serverdict[server.name]=0
        # Fill the load on each link
        for index,(time,tasks) in enumerate(self.tasklist.items()):
            for task in tasks:
                self.serverdict[task.server.name]+=1
                self.linkdict[task.link.name]+=1

    def compute(self):
        self.calcontime()
        self.calcload()


    def printstats(self):
        print("Global Stats:")
        print("Tasks",self.late+self.ontime)
        print("Late Tasks",self.late)
        print("Percentage Late Tasks", self.late*100/(self.late+self.ontime))
        if self.late>0:
            print("Average Latency",self.latency/self.late)
        else:
            print("Average Latency",0)

        print("Average Completion Time",self.completion/(self.late+self.ontime))
        print("----")
        print("Server Load:")
        for index,(key,value) in enumerate(self.serverdict.items()):
            print(key,value)
        print("----")
        print("Link Load:")
        for index,(key,value) in enumerate(self.linkdict.items()):
            print(key,value)
