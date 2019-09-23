class Simulator:

    DEBUG=False

    def __init__(self, tasklist, combinations):
        self.tasklist=tasklist
        self.combinations=combinations

    def run(self):
        for index,(time,tasks) in enumerate(self.tasklist.items()):
            # Process task with shortest deadline first
            tasks.sort(key=lambda x: x.deadline)
            for t in tasks:
                if self.DEBUG:
                    print(t.name,t.time,str(t.deadline))
                # Calculate the time it takes to go through every combination
                deadlines=[]
                for index,(link,server) in enumerate(self.combinations):
                    tup=link.upload(t.time,t.size)
                    tcalc=server.compute(tup,t.complexity)
                    tout=link.download(tcalc,t.output)
                    deadlines.append((index,tout))
                    if self.DEBUG:
                        print(index,link.name,server.name,tout)
                # Select the combination that takes the minimum amount of time
                deadlines.sort(key=lambda tup: tup[1])
                link,server=self.combinations[deadlines[0][0]]
                tup=link.upload_commit(t.time,t.size)
                tcalc=server.compute_commit(tup,t.complexity)
                tout=link.download_commit(tcalc,t.output)
                # Insert the final decision on the task
                t.set_completion(link,server,tout)
                if self.DEBUG:
                    print("Selected pair",deadlines[0])
                    print("================")

