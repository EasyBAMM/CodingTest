package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P1003 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		StringBuilder sb = new StringBuilder();
		int[] arr = new int[n];

		for (int i = 0; i < n; i++)
			arr[i] = Integer.parseInt(bf.readLine());

		int[] zero = new int[41];
		int[] one = new int[41];

		zero[0] = 1;
		zero[1] = 0;
		one[0] = 0;
		one[1] = 1;

		for (int i = 2; i < 41; i++) {
			zero[i] = zero[i - 1] + zero[i - 2];
			one[i] = one[i - 1] + one[i - 2];
		}

		for (int i = 0; i < n; i++) {
			System.out.println(zero[arr[i]] + " " + one[arr[i]]);
		}
	}

}
