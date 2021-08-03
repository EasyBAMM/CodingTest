package chapter03;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class P3 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int n = scanner.nextInt();
		int m = scanner.nextInt();
		int result = 0;

		for (int i = 0; i < n; i++) {
			int min_value = 10001;
			for (int j = 0; j < m; j++) {
				int x = scanner.nextInt();
				min_value = Math.min(min_value, x);
			}
			result = Math.max(result, min_value);
		}
		System.out.println(result);
	}
}