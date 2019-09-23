from sim.link import Link
from sim.server import Server
from sim.task import Task,TaskPattern

# Base system

# Display info
DEBUG=True

# Name of the configuration
NAME="E1+E2"

# Cloud added latency
cd=7.5

#Links
d2dlink=Link("D2D",50000000., 1.75, 50000000., 1.75)
ltelink=Link("LTE",30000000., 9.95, 30000000., 9.95)
ltecloudlink=Link("LTE2Cloud",30000000., 9.95+cd, 30000000., 9.95+cd)
wifilink=Link("WiFi",100000000., 1.85,100000000., 1.85)
wificloudlink=Link("WiFi2Cloud",100000000., 1.85+cd,100000000., 1.85+cd)

#Set the one way added delay to connect to the cloud
device1=Server("Device",200.)
edge1=Server("Edge1",1000.)
edge2=Server("Edge2",1000.)
cloud1=Server("Cloud1",5000.)
cloud2=Server("Cloud2",5000.)
cloud3=Server("Cloud3",5000.)


# Connect the devices with a given link
combinations=[ (ltelink,edge1),
        (wifilink,edge2),
        ]

# Defining our Task Patterns
Tr=TaskPattern("Rendering",2,100000,100000,20)
Tt=TaskPattern("Tracking",10,64000,4000,60)
Tm=TaskPattern("Mapping",26,64000,12000,90)
To=TaskPattern("Object_Recogniton",15,64000,4000,120)

#Generate timeline
# Unit is frame, 33FPS
deltat=33

tsimul=0
Lsimul=6000*33
tasklist={}
timesteps=[]

while tsimul<Lsimul:
    # Initialize our timeline for this given step
    timesteps.append(tsimul)
    tasklist[tsimul]=[]
    
    # Render every frame
    if tsimul%deltat==0:
        tasklist[tsimul].append(Task(Tr,tsimul))
        tasklist[tsimul].append(Task(Tr,tsimul))
        tasklist[tsimul].append(Task(Tr,tsimul))
    # Track every other frame
    if tsimul%(deltat*2)==0:
        tasklist[tsimul].append(Task(Tt,tsimul))
    # Update map once every three frames
    if tsimul%(deltat*3)==0:
        tasklist[tsimul].append(Task(Tm,tsimul))
    # Detect objects every 6 frames
    if tsimul%(deltat*4)==0:
        tasklist[tsimul].append(Task(To,tsimul))
    tsimul+=deltat
