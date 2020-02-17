import os
from shutil import copyfile

def check_file(file_path):
    os.chdir(file_path)
    print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    file_paths=[]
    for f in all_file:
        if os.path.isdir(f):
            out1,out2=check_file(file_path+'/'+f)
            files.extend(out1)
            file_paths.extend(out2)
            os.chdir(file_path)
        else:
            file_paths.append(file_path)
            files.append(f)
    return files,file_paths

#all_dir="F:/dataset/landmark_data/new_large_pose_img_2018_0320"
#all_dir="E:/landmark_data/landmark_dataset/landmark_train_data/133_extract_result-check"
all_dir="E:/landmark_data/landmark_dataset/landmark_train_data/test_new_20171005"
