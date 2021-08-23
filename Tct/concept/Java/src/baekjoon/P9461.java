package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9461 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(bf.readLine());
		long[] dp = new long[101];
		getDp(dp);
		for (int i = 0; i < n; i++) {
			int m = Integer.parseInt(bf.readLine());
			sb.append(dp[m]).append('\n');
		}

		System.out.println(sb);

		for (int i = 0; i < dp.length; i++) {
			System.out.print(dp[i] + " ");
		}
	}

	public static void getDp(long[] dp) {
		dp[1] = 1;
		dp[2] = 1;
		dp[3] = 1;
		dp[4] = 2;
		dp[5] = 2;
		dp[6] = 3;
		dp[7] = 4;
		dp[8] = 5;
		dp[9] = 7;
		dp[10] = 9;
		for (int i = 5; i < dp.length; i++) {
			dp[i] = dp[i - 5] + dp[i - 1];
		}
	}
}
