package tip.minmaxsum;

import java.util.Arrays;
import java.util.IntSummaryStatistics;

public class MinMaxSum {
	public static void main(String[] args) {
		int[] arr = { 10, 20, 30, 40, 24, 4, 4 };

		// Sum of Array in One Line
		int sumofArray = Arrays.stream(arr).sum();
		System.out.println(sumofArray);

		// get Minimum Value in an array in One Line
		int minimumValue = Arrays.stream(arr).min().getAsInt();
		System.out.println(minimumValue);

		// Get Maximum Value of an Array in One Line
		int MaxmumValue = Arrays.stream(arr).max().getAsInt();
		System.out.println(MaxmumValue);

		// 한 번에 구하려면
		IntSummaryStatistics stat = Arrays.stream(arr).summaryStatistics();
		int min = stat.getMin();
		int max = stat.getMax();
		System.out.println(min);
		System.out.println(max);
	}
}
