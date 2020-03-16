#include<stdio.h>

int main()
{
	int min_d=2000, min, menu[5];

	for(int i=0; i<5; i++)
		scanf("%d", &menu[i]);

		
	for(int i=0;i<3;i++){
		for(int j=3;j<5;j++){
			min = menu[i] + menu[j]-50;
			if(min<min_d)
				min_d = min;
		}
	}
	
	printf("%d",min_d);

	return 0;
}
