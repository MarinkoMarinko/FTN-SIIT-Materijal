package main

import "fmt"

func main() {
	numbers := []int {4, 8, 12, 6, 10}
	for i, val := range numbers {
		fmt.Printf("%d: %d\n", i, val)
	}

	frequencies := map[string]int {"go": 5, "python": 3, "java": 7}
	s := 0
	for _, val := range frequencies {
		s += val
	}
	fmt.Println(s)

	word := "Bloom"
	for _, c := range word {
		fmt.Printf("%c\n", c)
	}

	for i := range 5 {
		fmt.Print(i, " ")
	}
}