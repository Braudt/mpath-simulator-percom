from sim.randomlink import RandomLink
from sim.intermittentlink import IntermittentLink
from sim.link import Link
from sim.server import Server
from sim.task import Task,TaskPattern

# Base system
NAME="Single Server WiFi"

# Display info
DEBUG=True

# Cloud added latency
cd=7.5

#Links
d2dlink=Link("D2D",50000000., 1.75, 50000000., 1.75)
ltelink=RandomLink("LTE",30000000.,15000000*15000000, 9.95,1.29, 30000000.,15000000*15000000, 9.95,1.29)
ltecloudlink=RandomLink("LTE2Cloud",30000000.,15000000, 9.95+cd,1.29, 30000000.,15000000*15000000, 9.95+cd,1.29)
wifilink=IntermittentLink("WiFi",100000000.,50000000, 1.85,1.20,100000000.,50000000, 1.85,1.20,0.7)
wificloudlink=IntermittentLink("WiFi2Cloud",100000000.,50000000, 1.85+cd,1.20,100000000.,50000000, 1.85+cd,1.20,0.7)

#Set the one way added delay to connect to the cloud
device1=Server("Device",200.)
edge1=Server("Edge1",1000.)
edge2=Server("Edge2",1000.)
cloud1=Server("Cloud1",5000.)
cloud2=Server("Cloud2",5000.)
cloud3=Server("Cloud3",5000.)


# Connect the devices with a given link
combinations=[
        (wifilink,edge2),
        ]



# In a single scenario, we only consider one task per frame, that include all
# the other tasks
Tr=TaskPattern("Rendering",6,100000,100000,20)
Tt=TaskPattern("Tracking",16,64000,104000,20)
Tm=TaskPattern("Mapping",30,64000,112000,20)
To=TaskPattern("Object_Recogniton",18,64000,104000,20)

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
    # Track every other frame
    elif tsimul%(deltat*2)==0:
        if tsimul%(deltat*4)==0:
            tasklist[tsimul].append(Task(To,tsimul))
        else:
            tasklist[tsimul].append(Task(Tt,tsimul))
    # Update map once every three frames
    elif tsimul%(deltat*3)==0:
        tasklist[tsimul].append(Task(Tm,tsimul))
    # Detect objects every 6 frames
    tsimul+=deltat
