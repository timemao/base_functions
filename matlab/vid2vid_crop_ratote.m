clear;clc
%vid_path='E:\landmark_OEM\demo1\test_boundbox\20190913_190636.mp4';
vid_path='E:\landmarks_test\huaweimeiyan\doudong2.mp4';
strAviFile=vid_path;
bdObj=VideoReader(strAviFile);

%videoName = 'E:\landmark_OEM\demo1\test_boundbox\20190913_190636_rotate.mp4';
videoName='E:\landmarks_test\huaweimeiyan\doudong2_1.mp4';
fps = 30;
startFrame = 1;
aviobj=VideoWriter(videoName);
aviobj.FrameRate=fps;
open(aviobj);%Open file for writing video data

k = 1;
while (hasFrame(bdObj) && k<1200)% && k<100)
    k
    str=sprintf('%05d',k);
    %image_name=strcat('E:\deepfake\test_video\test_neil2\imgs1\imgs1-',str);
    image_name=strcat('E:\landmarks_test\test_overlap_imgs\imgs-',str);
    image_name=strcat(image_name,'.jpg');
    I= readFrame(bdObj);
    %imwrite(I,image_name,'jpg');
    %imwrite(imrotate(I,90),image_name,'jpg');
    %imwrite(flip(I,2),image_name,'jpg');
    %imwrite(I,image_name,'jpg');
    k = k+1;
    %I=[]; 
    if(k>900)
        writeVideo(aviobj,I);
    end
end
close(aviobj);
