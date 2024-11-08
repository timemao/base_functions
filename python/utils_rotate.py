import math
import numpy as np
import sys

# 小写为内旋，大写为外旋
# scipy.Rotation 大写为内旋
# 理论推导 大写为内旋，123为标号，旋转顺序按照矩阵乘法顺序

# todo 注意：万向锁部分没写对，先写了个输出

def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    if(n<0.1):
        return n < 0.1
    else:
        print("isRotationMatrix n=",n)
    #return n<2.0\

def float_equal(a,b):
    if(np.fabs(a-b)<1e-6):
        return True
    else:
        return False

def rotationMatrixToEulerAngles(R,order="XYZ"):
    # r.t. https://eecs.qmul.ac.uk/~gslabaugh/publications/euler.pdf
    # r.t. https://blog.csdn.net/c20081052/article/details/89479970?spm=1001.2014.3001.5506
    # 总共有6x2=12种

    if(order=="XYZ"):
        return np.array(rotationMatrixToEulerAngles_XYZ(R))
    elif(order=="zyx"):
        return -np.array(rotationMatrixToEulerAngles_XYZ(R))
    elif(order=="ZYX"):
        return np.array(rotationMatrixToEulerAngles_ZYX(R))
    elif(order=="xyz"):
        return -np.array(rotationMatrixToEulerAngles_ZYX(R))
    elif(order=="YXZ"):
        return np.array(rotationMatrixToEulerAngles_YXZ(R))
    elif(order=="zxy"):
        return -np.array(rotationMatrixToEulerAngles_YXZ(R))
    elif(order=="ZXY"):
        return np.array(rotationMatrixToEulerAngles_ZXY(R))
    elif(order=="yxz"):
        return -np.array(rotationMatrixToEulerAngles_ZXY(R))
    else:
        print("rotationMatrixToEulerAngles error, order=%s"%order)
        return None
        #raise Exception("rotationMatrixToEulerAngles error, order=%s"%order)

def angle_over_border(angles):
    angles_modi = angles.copy()
    for i in range(3):
        if (angles[i] < -180):
            angles_modi[i] = angles[i] + 360
        if (angles[i] > 180):
            angles_modi[i] = angles[i] - 360
    return angles_modi

def rotationMatrixToEulerAngles_XYZ(R):
    # atan2(0,0) undefined
    # 理论推导 对应 5行2列
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])  # cos: axis-y

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)   # 为啥不直接 arcsin(-R[2,0])???:值范围atan2更大（-180,180）
        z = math.atan2(R[1, 0], R[0, 0])

        # y=theta, z=phi, x=persi
        y1=-np.arcsin(R[2,0])
        y2=np.pi-y1

        x1=np.arctan2(R[2,1]/np.cos(y1),R[2,2]/np.cos(y1))
        x2=np.arctan2(R[2,1]/np.cos(y1),R[2,2]/np.cos(y2))

        z1=np.arctan2(R[1,0]/np.cos(y1),R[0,0]/np.cos(y1))
        z2=np.arctan2(R[1,0]/np.cos(y2),R[0,0]/np.cos(y2))

        angles1=np.array([x1,y1,z1])/np.pi*180
        angles2=np.array([x2,y2,z2])/np.pi*180

        angles1_border=angle_over_border(angles1)
        angles2_border = angle_over_border(angles2)

        print("angles1: ",angles1,angles1_border)
        print("angles2: ", angles2,angles2_border)

    else:
        # 矩阵退化，x+z=满足矩阵即可，定其中一个值为x=0,z=theta-x=theta
        print("R=",R)
        if(float_equal(-R[2,0],1)):
            y=math.pi/2
            x=0
            theta=math.atan2(R[0,1],-R[1,1])
            z=theta-x

        elif(float_equal(-R[2,0],-1)):
            y=-math.pi/2
            x=0
            theta = math.atan2(R[0, 1], -R[1, 1])
            z = theta - x
        else:
            raise Exception("rotationMatrixToEulerAngles_XYZ error")

        # x = 0+math.atan2(-R[1, 2], R[1, 1]) # around axis-x: roll
        # y = math.atan2(-R[2, 0], sy)  # around axis-y: pitch
        # z = 0  # around axis-z: yaw

    return [x,y,z]

def rotationMatrixToEulerAngles_ZYX(R):
    # 理论推导 对应 2行2列
    assert(isRotationMatrix(R))
    sy=math.sqrt(R[0,0]*R[0,0]+R[0,1]*R[0,1])

    singular=sy<1e-6
    #print("debug R=",R)
    if not singular:
        x=math.atan2(-R[1,2],R[2,2])
        y=math.atan2(R[0,2],sy)
        z=math.atan2(-R[0,1],R[0,0])
    else:
        #print("singular R=", R)
        if(float_equal(R[0,2],1)):
            y=math.pi/2
            z=0
            x=math.atan2(R[1,0],R[1,2])-z
        elif(float_equal(R[0,2],-1)):
            y = -math.pi / 2
            z=0
            x = math.atan2(-R[1, 0], R[1, 2]) +z
        else:
            raise Exception("rotationMatrixToEulerAngles_ZYX error")
    #print("x,y,z=",x,y,z)

    return [x,y,z]

def rotationMatrixToEulerAngles_YXZ(R):
    # 理论推导 对应 6行2列
    assert(isRotationMatrix(R))
    sx=math.sqrt((R[2,0]*R[2,0]+R[2,2]*R[2,2]))

    singular=sx<1e-6
    if(not singular):
        x = math.atan2(R[2, 1], sx)
        y = math.atan2(-R[2, 0], R[2, 2])
        z = math.atan2(R[1, 1], -R[0, 1])
    else:
        print("R=", R)
        if(float_equal(R[2,1],1)):
            x=math.pi/2
            y=0
            theta=math.atan2(R[1,1],R[0,0])
            z=theta-y
        elif(float_equal(R[2,1],-1)):
            x=-math.pi/2
            y=0
            theta=math.atan2(R[1,0],R[0,0])
            z=theta-y
        else:
            raise Exception("rotationMatrixToEulerAngles_YXZ error")

    return [x,y,z]

def rotationMatrixToEulerAngles_ZXY(R):
    assert(isRotationMatrix(R))
    sx=math.sqrt(R[1,0]*R[1,0]+R[1,1]*R[1,1])

    singular=sx<1e-6
    if(not singular):
        x=math.atan2(-R[1,2],sx)
        z=math.atan2(R[1,0],R[1,1])
        y=math.atan2(R[0,2],R[2,2])
    else:
        print("R=", R)
        if(float_equal(-R[1,2],1)):
            y=math.pi/2
            x=0
            theta=math.atan2(R[0,0],R[2,0])
            z=theta-x
        elif(float_equal(-R[1,2],-1)):
            y=-math.pi/2
            x=0
            theta=math.atan2(R[0,0],R[2,0])
            z=theta-x
        else:
            raise Exception("rotationMatrixToEulerAngles_ZXY error")

    return [x,y,z]

def mat_mul(R3,R2,R1):
    tmp=np.dot(R2,R1)
    res=np.dot(R3,tmp)
    # print("tmp=",tmp)
    # print("res=",res)
    return res

def eulerAnglesToRotationMatrix(theta, order="XYZ"):
    # theta = [x,y,z]

    if(order in ["xyz","xzy","yxz","yzx","zxy","zyx"]):
        theta=-theta   # 这一步没有影响：只会改变当角度变大/变小时，旋转对应的方向顺时针/逆时针

    c1, s1 = math.cos(theta[0]), math.sin(theta[0])
    c2, s2 = math.cos(theta[1]), math.sin(theta[1])
    c3, s3 = math.cos(theta[2]), math.sin(theta[2])

    Rx = np.array([[1, 0, 0],
                   [0, c1, -s1],
                   [0, s1, c1]
                   ])

    Ry = np.array([[c2, 0, s2],
                   [0, 1, 0],
                   [-s2, 0, c2]
                   ])

    Rz = np.array([[c3, -s3, 0],
                   [s3, c3, 0],
                   [0, 0, 1]
                   ])

    # print("Rx=",Rx)
    # print("Ry=",Ry)
    # print("Rz=",Rz)

    # 外旋(extrinsic rotation) == 定轴（fixed angles)
    # 先绕着转的先乘以点坐标，位置在最右边，依次类推
    if (order == "XYZ"):
        R = mat_mul(Rz,Ry,Rx)
    elif (order == "XZY"):
        R = mat_mul(Ry,Rz,Rx)

    elif (order == "YXZ"):
        R = mat_mul(Rz,Rx,Ry)
    elif (order == "YZX"):
        R= mat_mul(Rx,Rz,Ry)

    elif (order == "ZXY"):
        R = mat_mul(Ry,Rx,Rz)
    elif (order == "ZYX"):
        R = mat_mul(Rx,Ry,Rz)

    # 内旋（intrinsic rotation) == euler angles
    # 与外旋相反顺序
    elif (order == "xyz"):
        R = mat_mul(Rx,Ry,Rz)
    elif (order == "xzy"):
        R = mat_mul(Rx,Rz,Ry)

    elif (order == "yxz"):
        R = mat_mul(Ry,Rx,Rz)
    elif (order == "yzx"):
        R = mat_mul(Ry,Rz,Rx)

    elif (order == "zxy"):
        R = mat_mul(Rz,Rx,Ry)
    elif (order == "zyx"):
        R = mat_mul(Rz,Ry,Rx)

    return R

def angles_limit(theta):
    x,y,z=theta


def vali_convert():
    order="ZYX"
    #angles=np.array([0,50,0])/180*np.pi
    angles = np.array([0, 95, 0]) / 180 * np.pi
    #angles=np.array([-3.14159265,  1.48352986, -3.14159265])
    print("angles=",angles)

    R=eulerAnglesToRotationMatrix(angles,order=order)
    print("R=",R)

    angles_=rotationMatrixToEulerAngles(R,order=order)
    print("angles_new=",angles_)

    if(not (angles_[0]>=-np.pi/2 and angles_[0]<=np.pi/2)):
        angles_2=np.zeros(shape=3)
        angles_2[1]=np.pi-angles_[1]
        angles_2[0]=angles_[0]+np.pi
        angles_2[2]=angles_[2]+np.pi

        print("another solution=",angles_2)

    R_new=eulerAnglesToRotationMatrix(angles_,order=order)
    print("R=",R_new)
    print("diff_R=",np.sum(np.abs(R-R_new)))

if __name__=="__main__":
    # rot=np.array([[ 0.998581, -0.0329814, -0.0418222],
    #               [-0.0377931,  -0.992049,  -0.120041],
    #               [-0.0375306,   0.121451 , -0.991888]])
    # rot=np.array([[0.997978 ,0.0272944 ,0.0574071],
    #               [-0.0346956 ,0.990621, 0.132163],
    #               [-0.0532613, -0.133887, 0.989564 ]])
    # print(isRotationMatrix(rot))

    # rot=np.array([[0.994467 ,-0.005012, -0.001665],
    #               [0.005159, 0.994456, 0.105028],
    #               [0.001129, -0.105035 ,0.994468 ]])   # femto mega 安装误差 对应角度 yxz= [ 6.02877906  0.09592806 -0.29723414]
    # rot=np.array([[0.999947 ,0.00432361, 0.00929419],  # kinect v2安装误差 对应角度 yxz= [ 0.8620073  -0.53258561  0.25574884]
    #               [-0.00446314, 0.999877, 0.0150443],
    #               [-0.009228, -0.015085, 0.999844 ]])
    # print('yxz=',rotationMatrixToEulerAngles(rot,order='yxz')/np.pi*180)

    #rot=np.array([[0.924688, -0.016105, -0.380384],
    #              [-0.128279, -0.953864, -0.271454],
    #              [-0.358463, 0.299806, -0.884093]])
    #print('xyz',rotationMatrixToEulerAngles(rot,order='xyz')/np.pi*180)
    #print('yxz=', rotationMatrixToEulerAngles(rot, order='yxz') / np.pi * 180)
    #print('yxz=', rotationMatrixToEulerAngles(rot, order='YXZ') / np.pi * 180)

    #angles=np.array([0.25*np.pi, 0.5*np.pi, 0.33*np.pi])
    #angles = np.array([0.1 * np.pi, 0.1 * np.pi, 0.1 * np.pi])
    #angles=-angles
    #print(eulerAnglesToRotationMatrix(angles,order='ZYX'))

    #print(eulerAnglesToRotationMatrix(-angles, order='xyz'))
    #vali_convert()

    r,y,p=-0.06,39.95,15.21
