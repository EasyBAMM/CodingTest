package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class PosXY {
	private int x;
	private int y;

	public PosXY(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

}

public class P2178 {

	public static int n, m;
	public static int[][] graph;
	public static int[][] visited;
	public static int[] dx = { -1, 1, 0, 0 };
	public static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		graph = new int[n][m];
		visited = new int[n][m];
		for (int i = 0; i < n; i++) {
			String line = bf.readLine();
//			String[] line = bf.readLine().split("");
			for (int j = 0; j < m; j++)
				graph[i][j] = line.charAt(j) - '0'; // 136ms
//				graph[i][j] = Integer.parseInt(line[j]); // 196ms
		}

		bfs();

		System.out.println(visited[n - 1][m - 1]);
	}

	public static void bfs() {
		Queue<PosXY> q = new LinkedList<>();
		q.add(new PosXY(0, 0));
		visited[0][0] = 1;

		while (!q.isEmpty()) {
			PosXY v = q.remove();
			int x = v.getX();
			int y = v.getY();

			for (int i = 0; i < 4; i++) {
				int nx = v.getX() + dx[i];
				int ny = v.getY() + dy[i];

				// 인덱스 초과하거나, 방문했던 곳이거나 graph에서 1이 아닌 곳이면 넘어감
				if (nx < 0 || ny < 0 || nx >= n || ny >= m || visited[nx][ny] != 0 || graph[nx][ny] == 0)
					continue;
				q.add(new PosXY(nx, ny));
				visited[nx][ny] = visited[x][y] + 1;
			}
		}
	} // bfs

}
