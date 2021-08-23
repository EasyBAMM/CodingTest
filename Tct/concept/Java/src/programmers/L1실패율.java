package programmers;

import java.util.ArrayList;
import java.util.Collections;

public class L1실패율 {
	class Info implements Comparable<Info> {
		int idx;
		double fail;

		Info(int idx, double fail) {
			this.idx = idx;
			this.fail = fail;
		}

		@Override
		public int compareTo(Info info) {
			if (this.fail < info.fail) {
				return 1;
			} else if (this.fail > info.fail) {
				return -1;
			}
			return 0;
		}

	}

	class Solution {
		public int[] solution(int N, int[] stages) {
			int[] answer = new int[N];
			int failure = 0;
			int success = stages.length;
			ArrayList<Info> result = new ArrayList<>();

			for (int i = 1; i < N + 1; i++) {
				failure = 0;
				for (int j = 0; j < stages.length; j++) {
					if (stages[j] == i)
						failure++;
				}
				double percent = (failure == 0) ? 0 : (double) failure / success;
				result.add(new Info(i, percent));
				// System.out.println("idx: " + i + " failure: " + failure + " success: " +
				// success + " percent: " + percent);

				success -= failure;
			}

			Collections.sort(result);

			int i = 0;
			for (Info inf : result) {
				answer[i++] = inf.idx;
			}

			return answer;
		}
	}

}
