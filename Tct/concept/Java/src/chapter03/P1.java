package chapter03;

public class P1 {
	public static void main(String[] args) {
		int n = 1260;
		int count = 0;
		int[] coin_types = { 500, 100, 50, 10 };

		for (int i = 0; i < coin_types.length; i++) {
			count += n / coin_types[i];
			n %= coin_types[i];
		}

		System.out.println(count);
	}
}
