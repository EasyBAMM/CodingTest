package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P9663 {
	public static int[] rows;
	public static int result = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		rows = new int[n];

		dfs(0, n);
		System.out.println(result);
	}

	public static void dfs(int x, int n) {
		if (x == n) {
			result += 1;
			return;
		}

		for (int i = 0; i < n; i++) {
			rows[x] = i;
			if (adjacent(x)) {
				dfs(x + 1, n);
			}
		}
	}

	public static boolean adjacent(int x) {
		for (int i = 0; i < x; i++) {
			if (rows[x] == rows[i] || Math.abs(rows[x] - rows[i]) == x - i)
				return false;
		}
		return true;
	}

}
