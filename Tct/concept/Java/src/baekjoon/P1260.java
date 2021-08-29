package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P1260 {

	public static int n, m, start;
	public static ArrayList<ArrayList<Integer>> graph;
	public static boolean[] visited;
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		start = Integer.parseInt(st.nextToken());

		graph = new ArrayList<ArrayList<Integer>>();
		visited = new boolean[n + 1];
		for (int i = 0; i < n + 1; i++) {
			graph.add(new ArrayList<Integer>());
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(bf.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			// 양방향 그래프
			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		// 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
		for (int i = 0; i < n + 1; i++) {
			Collections.sort(graph.get(i));
		}

		dfs(start);
		sb.append("\n");
		visited = new boolean[n + 1]; // 방문처리 초기화
		bfs(start);
		System.out.println(sb);
	}

	// DFS 함수 정의
	public static void dfs(int x) {
		visited[x] = true;
		sb.append(x).append(" ");

		// 현재 노드와 연결된 다른 노드를 재귀적으로 방문
		for (int i = 0; i < graph.get(x).size(); i++) {
			int y = graph.get(x).get(i);
			if (!visited[y])
				dfs(y);
		}
	}

	// BFS 함수 정의
	public static void bfs(int x) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(x);
		// 현재 노드를 방문 처리
		visited[x] = true;
		// 큐가 빌 때까지 반복
		while (!q.isEmpty()) {
			// 큐에서 하나의 원소를 뽑아 출력
			int v = q.remove();
			sb.append(v).append(" ");
			// 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
			for (int i = 0; i < graph.get(v).size(); i++) {
				int y = graph.get(v).get(i);
				if (!visited[y]) {
					q.add(y);
					visited[y] = true;

				}
			}
		}
	}

}
