package tip.permutation;

import java.util.ArrayList;

class Permutation {
	private int n;
	private int r;
	private int[] now; // 현재 순열
	private ArrayList<ArrayList<Integer>> result; // 모든 순열

	public ArrayList<ArrayList<Integer>> getResult() {
		return result;
	}

	public Permutation(int n, int r) {
		this.n = n;
		this.r = r;
		this.now = new int[r];
		this.result = new ArrayList<ArrayList<Integer>>();
	}

	public void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public void permutation(int[] arr, int depth) {
		// 현재 순열의 길이가 r일 때 결과 저장
		if (depth == r) {
			ArrayList<Integer> temp = new ArrayList<>();
			for (int i = 0; i < now.length; i++) {
				temp.add(now[i]);
			}
			result.add(temp);
			return;
		}
		for (int i = depth; i < n; i++) {
			swap(arr, i, depth);
			now[depth] = arr[depth];
			permutation(arr, depth + 1);
			swap(arr, i, depth);
		}
	}
}

public class Main {
	public static void main(String[] args) {
		int[] arr = { 1, 3, 5, 7, 9 };
		int r = 3;

		Permutation perm = new Permutation(arr.length, r);
		perm.permutation(arr, 0);
		ArrayList<ArrayList<Integer>> result = perm.getResult();

		System.out.println("모든 순열의 수: " + result.size());
		for (int i = 0; i < result.size(); i++) {
			for (int j = 0; j < result.get(i).size(); j++) {
				System.out.print(result.get(i).get(j) + " ");
			}
			System.out.println();
		}
	}
}
