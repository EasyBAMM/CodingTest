package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1697 {

	public static int[] dp = new int[100001];
	public static int n, k;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		bfs(n);

		if (n == k)
			System.out.println(0);
		else
			System.out.println(dp[k]);
	}

	public static void bfs(int num) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(num);
		dp[num] = 1;

		while (!q.isEmpty()) {
			int x = q.remove();

			// 3가지 조건 수행, 걸린 시간 dp에 저장
			for (int i = 0; i < 3; i++) {
				int nx;
				if (i == 0)
					nx = x + 1;
				else if (i == 1)
					nx = x - 1;
				else
					nx = x * 2;

				// 조건 만족 시 그만
				if (nx == k) {
					dp[nx] = dp[x];
					return;
				}
				// 모두 만족해야함.
				if (nx < 0 || nx >= dp.length || dp[nx] != 0)
					continue;
				q.add(nx);
				dp[nx] = dp[x] + 1;
			}
		}
	}
}
