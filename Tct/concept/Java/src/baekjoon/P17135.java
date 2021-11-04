package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P17135 {
	public static int N, M, D;
	public static int[][] map;

	public static void main(String[] args) throws Exception {
		// https://haerang94.tistory.com/286
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());

		map = new int[N + 1][M + 1];

		for (int i = 1; i < N + 1; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 1; j < M + 1; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < N + 1; i++) {
			map[i][0] = 1;
		}
		for (int j = 0; j < M + 1; j++) {
			map[0][j] = 1;
		}

	}
}
