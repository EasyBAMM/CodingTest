package chapter06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Student implements Comparable<Student> {
	private String name;
	private int grade;

	public Student(String name, int grade) {
		this.name = name;
		this.grade = grade;
	}

	public String getName() {
		return this.name;
	}

	public int getGrade() {
		return this.grade;
	}

	// 정렬 기준은 '점수가 낮은 순서'
	@Override
	public int compareTo(Student student) {
		if (this.grade < student.grade) {
			return -1;
		}
		return 1;
	}
}

public class P11 {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		List<Student> students = new ArrayList<Student>();

		for (int i = 0; i < n; i++) {
			String[] line = bf.readLine().split(" ");
			students.add(new Student(line[0], Integer.parseInt(line[1])));
		}

		Collections.sort(students);

		for (int i = 0; i < students.size(); i++) {
			System.out.print(students.get(i).getName() + " ");
		}
	}
}
