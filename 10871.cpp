#include<iostream>

using namespace std;

int main()
{
	cin.tie(NULL);

	int N, X;

	cin >> N >> X;

	int value;
	for(int i=0;i<N;i++){
		cin >> value;
		if(value < X)
			cout<<value<<" ";
	}
	
	return 0;
}
