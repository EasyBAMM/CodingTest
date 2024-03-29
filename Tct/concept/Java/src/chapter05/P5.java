package chapter05;

public class P5 {
	public static int factorial_iterative(int n) {
		int result = 1;
		for (int i = 1; i < n + 1; i++) {
			result *= i;
		}
		return result;
	}

	public static int factorial_recursive(int n) {
		if (n == 1)
			return 1;

		return n * factorial_recursive(n - 1);
	}

	public static void main(String[] args) {
		System.out.println(factorial_iterative(5));
		System.out.println(factorial_recursive(5));
	}
}
