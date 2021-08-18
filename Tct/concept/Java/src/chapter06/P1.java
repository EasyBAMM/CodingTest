package chapter06;

public class P1 {
	public static void main(String[] args) {
		// 선택 정렬
		int[] array = { 7, 5, 9, 8, 3, 1, 6, 2, 4, 8 };

		for (int i = 0; i < array.length; i++) {
			int minIdx = i;
			for (int j = i + 1; j < array.length; j++) {
				if (array[minIdx] > array[j])
					minIdx = j;
			}
			int temp = array[i];
			array[i] = array[minIdx];
			array[minIdx] = temp;
		}

		for (int num : array) {
			System.out.print(num + " ");
		}
	}
}
