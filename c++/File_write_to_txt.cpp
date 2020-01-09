// for c
FILE *imgWrite = fopen("e://landmarks_test//test_nv12//rgb//img_eye_64.txt", "w");

if (!imgWrite) {
	printf("fopen fail");
  return 1;
}
fprintf(imgWrite, "%d ", *(p + i*imgw + j));

fclose(imgWrite);

// for c++
std::ofstream out_pnt(outpntpath);
out_pnt << 226 << std::endl;
for (int k = 0; k < 226; k++)
{
	out_pnt <<x<< " " << y<< std::endl;
}
out_pnt.close();
