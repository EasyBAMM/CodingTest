#include<iostream>

using namespace std;

int main()
{
	cin.tie(NULL); //cin과 cout의 묶음을 풀어준다.
	ios_base::sync_with_stdio(false);//c와 c++의 버퍼를 분리한다.

	int T,A,B;

	cin>>T;

	for(int i=0;i<T;i++){
		cin >> A >> B;
		cout<< A + B << "\n";
	}

	return 0;
}


