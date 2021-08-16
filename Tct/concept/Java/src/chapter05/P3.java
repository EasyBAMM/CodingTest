package chapter05;

public class P3 {
	public static void recursive_func() {
		System.out.println("재귀 함수를  호출합니다.");
		recursive_func();
	}

	public static void main(String[] args) {
		recursive_func();
	}
}
