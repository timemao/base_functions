import os
import numpy as np
import cv2

def read_pose_txt(pose_txt):
    infos=list(open(pose_txt,"r"))

    R_mat=np.eye(3)
    T_mat=np.zeros(shape=3)

    for i in range(3):
        x,y,z=infos[i].strip().split()
        x,y,z=float(x),float(y),float(z)
        R_mat[i]=[x,y,z]

    x,y,z=infos[4].strip().split()
    x, y, z = float(x), float(y), float(z)
    T_mat=[x,y,z]
    return R_mat,T_mat

def test_read_pose_txt():
    pose_txt=r"D:\download\datasets\biwi\faces_0\01\frame_00003_pose.txt"

    R_mat,T_mat=read_pose_txt(pose_txt)
    print(R_mat)
    print(T_mat)

def read_depth_rgb_cal(txt_path):
    infos=list(open(txt_path,"r"))

    K_mat=np.eye(3)
    dist=np.zeros(shape=4)
    for i in range(3):
        x,y,z=infos[i].strip().split()
        x, y, z = float(x), float(y), float(z)
        K_mat[i] = [x, y, z]

    d1,d2,d3,d4=infos[4].strip().split()
    d1, d2, d3, d4 =float(d1),float(d2),float(d3),float(d4)

    #infos[5:8]
    R_mat = np.eye(3)
    T_mat = np.zeros(shape=3)
    for i in range(3):
        x,y,z=infos[i+6].strip().split()
        x, y, z = float(x), float(y), float(z)
        R_mat[i] = [x, y, z]

    #infos[9]
    x,y,z=infos[10].strip().split()
    x,y,z=float(x),float(y),float(z)
    T_mat=[x,y,z]
    return K_mat,dist,R_mat,T_mat

def test_read_cal():
    #cal_path=r"D:\download\datasets\biwi\faces_0\01\rgb.cal"
    cal_path = r"D:\download\datasets\biwi\faces_0\01\depth.cal"

    K_mat, dist, R_mat, T_mat=read_depth_rgb_cal(cal_path)
    print(K_mat)
    print(dist)
    print(R_mat)
    print(T_mat)

if __name__=="__main__":
    test_read_pose_txt()
    test_read_cal()
