package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2475 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int sumval = 0;
		for (int i = 0; i < 5; i++) {
			int val = Integer.parseInt(st.nextToken());
			sumval += Math.pow(val, 2);
		}
		System.out.println(sumval % 10);
	}
}
