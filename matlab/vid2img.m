clear
clc
%strAviFile='E:\deepfake\FaceSwapKowalski\data\test_me3.mp4';
%strAviFile='E:\deepfake\test_video\test2\zao2-1.mp4';
%strAviFile='E:\deepfake\test_video\siyao\siyao.mp4';
%strAviFile='E:\deepfake\test_video\test_same_pose\test_91\MI8_CENTER_0091.mp4';
%strAviFile='E:\deepfake\test_video\test_neil3\test_neil2.mp4';
strAviFile='E:\landmarks_test\overlap1.mp4';
bdObj=VideoReader(strAviFile);

k = 1;
while (hasFrame(bdObj) && k<50)% && k<100)
    k
    str=sprintf('%04d',k);
    %image_name=strcat('E:\deepfake\test_video\test_neil2\imgs1\imgs1-',str);
    image_name=strcat('E:\landmarks_test\test_overlap_imgs\imgs-',str);
    image_name=strcat(image_name,'.jpg');
    I= readFrame(bdObj);
    %imwrite(I,image_name,'jpg');
    %imwrite(imrotate(I,90),image_name,'jpg');
    %imwrite(flip(I,2),image_name,'jpg');
    imwrite(I,image_name,'jpg');
    k = k+1;
    I=[]; 
end
