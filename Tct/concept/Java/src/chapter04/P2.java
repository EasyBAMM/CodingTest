package chapter04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P2 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		int result = 0;

		for (int i = 0; i <= n; i++) {
			for (int j = 0; j < 60; j++) {
				for (int k = 0; k < 60; k++) {
					String timeString = String.valueOf(i) + String.valueOf(j) + String.valueOf(k);
					if (timeString.contains(String.valueOf(n))) {
						result += 1;
					}
				}
			}
		}

		System.out.println(result);
	}
}
