package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P14888 {
	public static int n;
	public static int[] nums;
	public static int maxVal = -1000000000;
	public static int minVal = 1000000000;
	public static int add;
	public static int sub;
	public static int mul;
	public static int div;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String line = bf.readLine();
		n = Integer.parseInt(line);
		nums = new int[n];
		StringTokenizer st = new StringTokenizer(bf.readLine());
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(bf.readLine());
		add = Integer.parseInt(st.nextToken());
		sub = Integer.parseInt(st.nextToken());
		mul = Integer.parseInt(st.nextToken());
		div = Integer.parseInt(st.nextToken());

		// depth, sum, oper
		dfs(1, nums[0], add, sub, mul, div);
		System.out.println(maxVal);
		System.out.println(minVal);
	}

	public static void dfs(int depth, int sumVal, int add, int sub, int mul, int div) {
		if (depth == n) {
			maxVal = Math.max(maxVal, sumVal);
			minVal = Math.min(minVal, sumVal);
			return;
		}

		if (add != 0)
			dfs(depth + 1, sumVal + nums[depth], add - 1, sub, mul, div);
		if (sub != 0)
			dfs(depth + 1, sumVal - nums[depth], add, sub - 1, mul, div);
		if (mul != 0)
			dfs(depth + 1, sumVal * nums[depth], add, sub, mul - 1, div);
		if (div != 0)
			dfs(depth + 1, sumVal / nums[depth], add, sub, mul, div - 1);
	}
}
