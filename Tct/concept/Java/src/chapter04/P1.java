package chapter04;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P1 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		String[] direction = bf.readLine().split(" ");
		int[] dx = { 1, -1, 0, 0 };
		int[] dy = { 0, 0, 1, -1 };
		int x = 1;
		int y = 1;
		int nx = 0, ny = 0;
		for (int i = 0; i < direction.length; i++) {
			if (direction[i].equalsIgnoreCase("U")) {
				nx = x + dx[1];
				ny = y + dy[1];
			} else if (direction[i].equalsIgnoreCase("D")) {
				nx = x + dx[0];
				ny = y + dy[0];
			} else if (direction[i].equalsIgnoreCase("L")) {
				nx = x + dx[3];
				ny = y + dy[3];
			} else if (direction[i].equalsIgnoreCase("R")) {
				nx = x + dx[2];
				ny = y + dy[2];
			}

			if (nx < 1 || nx > n || ny < 1 || ny > n)
				continue;

			x = nx;
			y = ny;
		}

		System.out.println(x + " " + y);
	}
}
