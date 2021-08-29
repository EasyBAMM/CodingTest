package chapter06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class P10 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());

		// Wrapper 클래스 (객체)
		Integer[] arr = new Integer[n];

		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(bf.readLine());
		}

		// 기본 정렬 라이브러리를 이용하여 내림차순 정렬 수행
		Arrays.sort(arr, Collections.reverseOrder());

		for (int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}
