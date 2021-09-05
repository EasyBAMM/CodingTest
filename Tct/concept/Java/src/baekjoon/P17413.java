package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class P17413 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuffer sbf = new StringBuffer(); // string 거꾸로 만들 수 있다
		StringBuilder sbd = new StringBuilder();
		String str = bf.readLine();
		int i = 0;

		while (i < str.length()) {
			char curr = str.charAt(i);
			if (curr == ' ') { // 공백이면 sbf에 있는 거 뒤집기
				sbd.append(sbf.reverse().toString() + " ");
				sbf = new StringBuffer();
			} else if (curr == '<') { // < 이면 sbf있는 거 뒤집고 > 만날 때까지 그냥 더하기
				if (sbf.length() != 0) {
					sbd.append(sbf.reverse().toString());
					sbf = new StringBuffer();
				}
				while (true) {
					curr = str.charAt(i);
					sbd.append(curr);
					if (curr == '>')
						break;
					i++;
				}
			} else { // 평소에 그냥 sbf에 넣기
				sbf.append(curr);
			}
			i++;
		} // while

		if (sbf.length() != 0)
			sbd.append(sbf.reverse().toString());

		System.out.println(sbd);
	}
}

//public class Main{
//	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		char[] arr = br.readLine().toCharArray();
//		int idx=0;
//		while(idx<arr.length) {
//			//1.tag 처리
//			if(arr[idx]=='<') {
//				while(arr[idx++]!='>') {}
//			}
//			//2.단어 처리
//			else if(Character.isLetterOrDigit(arr[idx])) {
//				int start = idx;
//				while(idx<arr.length && arr[idx]!=' ' && arr[idx]!= '<') {
//					idx++;
//				}
//				int end = idx-1;
//				reverse(arr,start,end);
//				if(idx<arr.length && arr[idx]!='<')
//					idx++;
//			}
//		}
//		System.out.println(arr);
//	}
//
//	private static void reverse(char[] arr, int start, int end) {
//		while(start<end) {
//			char tmp = arr[start];
//			arr[start] = arr[end];
//			arr[end] = tmp;
//			start++; end--;
//		}
//	}
//}
