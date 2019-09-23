class TaskPattern:

    def __init__(self,name,X,S,U,d):
        self.name=name
        self.complexity=X
        self.size=S
        self.output=U
        self.d=d


class Task:

    def __init__(self,taskpattern,time):
        self.name=taskpattern.name
        self.complexity=taskpattern.complexity
        self.size=taskpattern.size
        self.output=taskpattern.output
        self.deadline=taskpattern.d+time
        self.time=time
        self.running=False

    def set_completion(self,link,server,time):
        self.link=link
        self.server=server
        self.completion=time

