#include<iostream>

using namespace std;

int main()
{
	int n1, n2;

	cin>>n1>>n2;

	int n3, n4, n5, n6;

	n3 = n1*(n2%10);
	n4 = n1*(n2%100/10);
	n5 = n1*(n2/100);

	n6 = n1*n2;

	cout<<n3<<endl<<n4<<endl<<n5<<endl<<n6;


	return 0;
}
