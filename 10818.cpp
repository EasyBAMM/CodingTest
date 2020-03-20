#include<iostream>

using namespace std;

int main()
{
	int num, count, min = 1000001, max = -1000001;
	cin >> count;

	for(int i=0;i<count;i++){
		cin >> num;
		max = num > max ? num : max;
		min = num < min ? num : min;
	}

	
	cout<< min << " " << max << "\n";

	return 0;
}
