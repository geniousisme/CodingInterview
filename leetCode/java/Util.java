package util.func;

import java.util.ArrayList;
import java.util.List;

public class Util {
	public static void print_int_array(int[] int_arr) {
		System.out.print("[ ");
		for (int elem: int_arr) {
			System.out.print(elem + " ");
		}
		System.out.println("]");
	}

	public static void print_str_array(String[] str_arr) {
		System.out.print("[ ");
		for (String elem: str_arr) {
			System.out.print(elem + " ");
		}
		System.out.println("]");
	}

	public static void print_str_lst(List<String> str_lst) {
		System.out.print("[ ");
		for (String elem: str_lst) {
			System.out.print(elem + " ");
		}
		System.out.println("]");
	}
}