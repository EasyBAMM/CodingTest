package programmers;

import java.util.HashMap;

public class L1완주하지못한선수 {
	public String solution(String[] participant, String[] completion) {
		String answer = "";

		HashMap<String, Integer> people = new HashMap<>();

		for (String parti : participant) {
			if (!people.containsKey(parti)) {
				people.put(parti, 1);
			} else {
				people.put(parti, people.get(parti) + 1);
			}
		}

		for (String comple : completion) {
			people.put(comple, people.get(comple) - 1);
		}

		for (String key : people.keySet()) {
			if (people.get(key) == 1) {
				answer = key;
			}
		}

		return answer;
	}
}
