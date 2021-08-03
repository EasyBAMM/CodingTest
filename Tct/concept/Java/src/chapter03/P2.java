package chapter03;

import java.util.Arrays;
import java.util.Scanner;

public class P2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		int result = 0;
		int[] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		Arrays.sort(arr);
		int first = arr[n - 1];
		int second = arr[n - 2];

		// 가장 큰 수가 더해지는 횟수 계산
		int cnt = (m / (k + 1)) * k;
		cnt += m % (k + 1);

		result += cnt * first; // 가장 큰 수 더하기
		result += (m - cnt) * second; // 두 번째로 큰 수 더하기

//		while (true) {
//			for (int i = 0; i < m; i++) {
//				if (m == 0)
//					break;
//				result += first;
//				m -= 1;
//			}
//			if (m == 0)
//				break;
//			result += second;
//			m -= 1;
//		}

		System.out.println(result);
	}
}
