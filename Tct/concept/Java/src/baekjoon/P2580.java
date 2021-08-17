package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

class Node {
	private int x;
	private int y;

	public Node(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}

	public int getPosX() {
		return x;
	}

	public int getPosY() {
		return y;
	}
}

public class P2580 {
	public static int[][] sudoku = new int[9][9];;
	public static ArrayList<Node> zeros = new ArrayList<>();
	public static boolean flag = false;
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0; i < 9; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine(), " ");

			for (int j = 0; j < 9; j++) {
				int x = Integer.parseInt(st.nextToken());
				sudoku[i][j] = x;
				if (x == 0) {
					zeros.add(new Node(i, j));
				}
			}
		}

		dfs(0);

		System.out.println(sb);
	}

	public static void dfs(int depth) {
		if (flag)
			return;
		if (depth == zeros.size()) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					sb.append(sudoku[i][j]).append(' ');
				}
				sb.append('\n');
			}
			flag = true;
			return;
		}

		int x = zeros.get(depth).getPosX();
		int y = zeros.get(depth).getPosY();
		ArrayList<Integer> possible = is_possible(x, y);

		for (int i = 0; i < possible.size(); i++) {
			sudoku[x][y] = possible.get(i);
			dfs(depth + 1);
			sudoku[x][y] = 0;
		}
	}

	public static ArrayList<Integer> is_possible(int x, int y) {
		ArrayList<Integer> possible = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));

		for (int i = 0; i < 9; i++) {
			if (possible.contains(sudoku[x][i]))
				possible.remove(possible.indexOf(sudoku[x][i]));
			if (possible.contains(sudoku[i][y]))
				possible.remove(possible.indexOf(sudoku[i][y]));
		}

		x /= 3;
		y /= 3;

		for (int j = x * 3; j < (x + 1) * 3; j++) {
			for (int k = y * 3; k < (y + 1) * 3; k++) {
				if (possible.contains(sudoku[j][k]))
					possible.remove(possible.indexOf(sudoku[j][k]));
			}
		}

		return possible;
	}
}
