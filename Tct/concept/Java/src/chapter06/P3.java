package chapter06;

public class P3 {
	public static void main(String[] args) {
		// 삽입 정렬
		int[] array = { 7, 5, 9, 0, 3, 1, 6, 2, 4, 8 };

		for (int i = 1; i < array.length; i++) {
			for (int j = i; j > 0; j--) {
				if (array[j] < array[j - 1]) {
					int temp = array[j];
					array[j] = array[j - 1];
					array[j - 1] = temp;
				} else
					break;
			}
		}

		for (int num : array) {
			System.out.print(num + " ");
		}
	}
}
