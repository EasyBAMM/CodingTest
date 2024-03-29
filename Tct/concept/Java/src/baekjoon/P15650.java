package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P15650 {
	public static int n, m;
	public static StringBuilder sb = new StringBuilder();
	public static int[] out;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] line = bf.readLine().split(" ");
		n = Integer.parseInt(line[0]);
		m = Integer.parseInt(line[1]);

		out = new int[m];

		btk(1, 0);

		System.out.println(sb);
	}

	public static void btk(int at, int depth) {
		if (depth == m) {
			for (int val : out) {
				sb.append(val).append(' ');
			}
			sb.append('\n');
			return;
		}

		for (int i = at; i <= n; i++) {
			out[depth] = i;
			btk(i + 1, depth + 1);
		}
	}

}
