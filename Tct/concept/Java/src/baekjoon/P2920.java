package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2920 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int before = Integer.parseInt(st.nextToken());
		String answer = "";
		while (st.hasMoreTokens()) {
			int next = Integer.parseInt(st.nextToken());
			if (before < next) {
				if (answer.equals("descending")) {
					answer = "mixed";
					break;
				}
				answer = "ascending";
			} else if (before > next) {
				if (answer.equals("ascending")) {
					answer = "mixed";
					break;
				}
				answer = "descending";
			}
			before = next;
		}
		System.out.println(answer);
	}
}
