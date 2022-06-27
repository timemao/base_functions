#include "timer.h"
#include <iostream>

int main()
{
	struct timeval time_s,time_e;
	long long curTime_s,curTime_e;
	gettimeofday(&time_s, NULL);
	curTime_s = ((long long)(time_s.tv_sec)) * 1000 *1.0 + time_s.tv_usec*1.0 / 1000;
	
	sleep(1000);
	
	gettimeofday(&time_e, NULL);
	curTime_e = ((long long)(time_e.tv_sec)) * 1000 *1.0+ time_e.tv_usec *1.0/ 1000;
	printf("bodypose: detect_forward_time %fms\n", (curTime_e - curTime_s));
	
	float time_use=(timer->end.tv_sec - timer->begin.tv_sec) * 1000 + (timer->end.tv_usec - timer->begin.tv_usec) / 1000.0;
	printf("use time= %.03f ms",time_use);
		
}