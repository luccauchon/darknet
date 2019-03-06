# Stupid python path shit.
# Instead just add darknet.py to somewhere in your python path
# OK actually that might not be a great idea, idk, work in progress
# Use at your own risk. or don't, i don't care

import sys, os
sys.path.append('/gpfs/home/cj3272/14a/AMATEUR/modeles/LCLCL_ObjectDetection/darknet/python/')
import darknet as dn
import pdb
import time

dn.set_gpu(1)
net = dn.load_net("../cfg/yolo-voc.2.odema.cfg", "../backup/yolo-voc_100.weights", 0)
meta = dn.load_meta('../data/odema.data')

while (True):
    start = time.time()
    r = dn.detect(net, meta, "/gpfs/home/cj3272/14a/AMATEUR/modeles/LCLCL_ObjectDetection/darknet/data/eagle.jpg")
    for clazz,probability,(x1,y1,x2,y2) in r:
        pass
    end = time.time()
    print(str(end-start)+' seconds.')
