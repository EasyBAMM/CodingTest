package chapter05;

import java.util.LinkedList;
import java.util.Queue;

public class P2 {
	public static void main(String[] args) {
		Queue<Integer> queue = new LinkedList<>();
		queue.add(5);
		queue.add(2);
		queue.add(3);
		queue.add(7);
		queue.poll();
		queue.add(1);
		queue.add(4);
		queue.poll();

		while (!queue.isEmpty()) {
			System.out.println(queue.peek());
			queue.poll();
		}
	}
}
