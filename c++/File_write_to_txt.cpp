// for c
FILE *imgWrite = fopen("e://landmarks_test//test_nv12//rgb//img_eye_64.txt", "w");

if (!imgWrite) {
	printf("fopen fail");
  return 1;
}
fprintf(imgWrite, "%d ", *(p + i*imgw + j));

fclose(imgWrite);
