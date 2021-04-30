#include<iostream>

using namespace std;

int main()
{
	int N;
	cin >> N;

	int result = N;
	int count=0;
	int a, b, c, newN;

	while(true){
		a = N/10;
		b = N%10;
		c = (a+b)%10;
		newN = 10*b+c;
		N = newN;
		count++;
		if(result == N)
			break;
	}
	
	cout<<count;

	return 0;
}

