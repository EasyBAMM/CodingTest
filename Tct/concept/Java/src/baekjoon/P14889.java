package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class P14889 {

	static int N;
	static int[][] map;
	static boolean[] visit;

	static int Min = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		// https://st-lab.tistory.com/122
		BufferedReader bReader = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(bReader.readLine());

		map = new int[N][N];
		visit = new boolean[N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(bReader.readLine(), " ");

			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] count = { 0, 0, 0 };
		combi(0, 0);
		System.out.println(Min);
	}

	// idx는 인덱스, count는 조합 개수(=재귀 깊이)
	public static void combi(int idx, int count) {
		// 팀 조합이 완성될 경우
		if (count == N / 2) {
			diff();
			return;
		}

		for (int i = idx; i < N; i++) {
			if (!visit[i]) {
				visit[i] = true;
				combi(i + 1, count + 1);
				visit[i] = false;
			}
		}
	}

	public static void diff() {
		int team_start = 0;
		int team_link = 0;

		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				// i 번째 사람과 j 번째 사람이 true라면 스타트팀으로 점수 플러스
				if (visit[i] == true && visit[j] == true) {
					team_start += map[i][j];
					team_start += map[j][i];

				}
				// i 번째 사람과 j 번째 사람이 false라면 링크팀으로 점수 플러스
				else if (visit[i] == false && visit[j] == false) {
					team_link += map[i][j];
					team_link += map[j][i];
				}
			}
		}
		int val = Math.abs(team_start - team_link);

		if (val == 0) {
			System.out.println(val);
			System.exit(0);
		}

		Min = Math.min(val, Min);

	}
}
