import cv2
import os
import numpy as np

def read_obj(obj_path):
    vertices,faces=[],[]
    infos=list(open(obj_path,"r"))

    for idx,info in enumerate(infos):
        info=info.strip()
        if("v " in info):
            _,x,y,z=info.split()
            x,y,z=float(x),float(y),float(z)
            vertices.append([x,y,z])

        if("f " in info):
            _,idx1,idx2,idx3=info.split()
            if("/" in idx1):
                idx1,idx2,idx3=idx1.split("/")[0],idx2.split("/")[0],idx3.split("/")[0]

            idx1,idx2,idx3=int(idx1),int(idx2),int(idx3)
            faces.append([idx1,idx2,idx3])

    vertices=np.array(vertices)
    faces=np.array(faces)

    return vertices,faces

def save_obj(vertices,faces,obj_path):
    fw=open(obj_path,"w")
    n_ver,n_face=vertices.shape[0],faces.shape[0]
    for i in range(n_ver):
        fw.write("v %f %f %f\n"%(vertices[i,0],vertices[i,1],vertices[i,2]))
    for i in range(n_face):
        fw.write("f %d %d %d\n"%(faces[i,0],faces[i,1],faces[i,2]))
    fw.close()
