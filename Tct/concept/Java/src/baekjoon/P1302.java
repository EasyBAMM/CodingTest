package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

class Book implements Comparable<Book> {
	String name;
	int number;

	Book(String name, int number) {
		this.name = name;
		this.number = number;
	}

	@Override
	public int compareTo(Book o) {
		if (this.number < o.number)
			return 1;
		else if (this.number > o.number)
			return -1;
		else {
			return this.name.compareTo(o.name);
		}
	}
}

public class P1302 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		Map<String, Integer> books = new HashMap<String, Integer>();

		// 일단 map에 넣어서 개수 파악
		for (int i = 0; i < n; i++) {
			String book = bf.readLine();
			books.put(book, books.getOrDefault(book, 0) + 1);
		}

		ArrayList<Book> bookList = new ArrayList<Book>();

		// list에 (책이름, 개수)로 넣기
		for (String name : books.keySet()) {
			bookList.add(new Book(name, books.get(name)));
		}

		// 정렬하기 정렬 방식은 class에다가 정의함
		Collections.sort(bookList);

		System.out.println(bookList.get(0).name);
	}
}
