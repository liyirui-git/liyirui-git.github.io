#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX_LEN 2048

int main(void){
	char *message = (char *)calloc(MAX_LEN, sizeof(char));
	char *command = (char *)calloc(MAX_LEN*2, sizeof(char));
	printf("Please input the commit message: (no more than %d chars)\n", MAX_LEN - 1);
	char c = getchar();
	int i = 0;
	while(c != '\n'){
		message[i++] = c;
		if(i == MAX_LEN - 1) break;
		c = getchar();
	}
	strcat(command, "git commit -m \"");
	strcat(command, message);
	strcat(command, " (by push.cpp)\"");
	system("git add -A");
	system(command);
	system("git push");
	return 0;
} 
