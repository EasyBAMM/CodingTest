#include<iostream>

using namespace std;

int main()
{
	int n;

	cin>>n;

	for(int i=1;i<=n;i++){
		for(int j=1;j<=i-1;j++)
			cout<<" ";
		for(int k=1;k<=2*n-(i-1)*2-1;k++)
			cout<<"*";
		cout<<"\n";
	}

	for(int i=2;i<=n;i++){
		for(int j=1;j<=n-i;j++)
			cout<<" ";
		for(int k=1;k<=2*i-1;k++)
			cout<<"*";
		cout<<"\n";
	}

	return 0;
}
