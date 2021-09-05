package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class P1764 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		StringBuilder sb = new StringBuilder();

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		Set<String> hearSet = new HashSet<>();
		List<String> answer = new ArrayList<String>();
		for (int i = 0; i < n; i++)
			hearSet.add(bf.readLine());
		for (int j = 0; j < m; j++) {
			String seestr = bf.readLine();
			if (hearSet.contains(seestr))
				answer.add(seestr);
		}

		Collections.sort(answer);

		System.out.println(answer.size());
		for (String ans : answer) {
			sb.append(ans).append("\n");
		}

		System.out.println(sb);
	}
}
