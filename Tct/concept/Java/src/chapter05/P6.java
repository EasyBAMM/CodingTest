package chapter05;

public class P6 {

	public static final int INF = 99999999;

	public static int[][] graph = { { 0, 7, 5 }, { 7, 0, INF }, { 5, INF, 0 } };

	public static void main(String[] args) {
		for (int i = 0; i < graph.length; i++) {
			for (int j = 0; j < graph[0].length; j++) {
				System.out.print(graph[i][j] + " ");
			}
			System.out.println();
		}

	}
}
