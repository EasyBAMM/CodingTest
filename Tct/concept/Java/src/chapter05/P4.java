package chapter05;

public class P4 {
	public static void recursive_func(int i) {
		if (i == 5)
			return;
		System.out.println(i + " 안녕");
		recursive_func(i + 1);
		System.out.println(i + "하세요");
	}

	public static void main(String[] args) {
		recursive_func(0);
	}
}
