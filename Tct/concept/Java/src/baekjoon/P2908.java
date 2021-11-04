package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P2908 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] numbers = new int[2];
		numbers[0] = Integer.parseInt(st.nextToken());
		numbers[1] = Integer.parseInt(st.nextToken());

		numbers[0] = reverseNum(numbers[0]);
		numbers[1] = reverseNum(numbers[1]);

		int answer = Math.max(numbers[0], numbers[1]);
		System.out.println(answer);
	}

	public static int reverseNum(int n) {
		int reverseNum = 0;

		while (n != 0) {
			reverseNum = reverseNum * 10 + n % 10;
			n /= 10;
		}
		return reverseNum;
	}
}
