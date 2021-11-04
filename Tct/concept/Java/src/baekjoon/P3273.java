package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P3273 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		int[] arr = new int[n];
		StringTokenizer st = new StringTokenizer(bf.readLine());

		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int x = Integer.parseInt(bf.readLine());

		Arrays.sort(arr); // 정렬

		int left = 0;
		int right = n - 1;
		int result = 0;
		while (left < right) {
			int sumVal = arr[left] + arr[right];
			if (sumVal < x) { // 작으면 왼쪽++
				left++;
			} else if (sumVal > x) { // 크면 오르쪽--
				right--;
			} else { // 같으면 왼쪽, 오른쪽 가까이
				result++;
				left++;
				right--;
			}
		}

		System.out.println(result);
	}
}
