package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P1149 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());

		int[][] houses = new int[n][3];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < 3; j++) {
				houses[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[][] dp = new int[n][n];
		dp[0][0] = houses[0][0];
		dp[0][1] = houses[0][1];
		dp[0][2] = houses[0][2];

		for (int i = 1; i < n; i++) {
			dp[i][0] = dp[i][0] + Math.min(dp[i][1], dp[i][2]);
			dp[i][1] = dp[i][1] + Math.min(dp[i][0], dp[i][2]);
			dp[i][2] = dp[i][2] + Math.min(dp[i][0], dp[i][1]);
		}
		int answer = Integer.MAX_VALUE;
		for (int i = 0; i < 3; i++) {
			answer = Math.min(answer, dp[n - 1][i]);
		}
		System.out.println(answer);
	}
}
