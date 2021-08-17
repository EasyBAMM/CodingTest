package chapter05;

import java.util.Stack;

public class P1 {
	public static void main(String[] args) {
		Stack<Integer> stack = new Stack<>();
		stack.add(5);
		stack.add(2);
		stack.add(3);
		stack.add(7);
		stack.pop();
		stack.add(1);
		stack.add(4);
		stack.pop();

		while (!stack.empty()) {
			System.out.println(stack.peek());
			stack.pop();
		}
	}
}
