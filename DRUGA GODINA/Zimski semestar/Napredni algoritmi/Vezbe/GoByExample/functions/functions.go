package main

import "fmt"

func sumCounts(counts []int) int {
	s := 0
	for i := range len(counts) {
		s += counts[i]
	}
	return s
}

func maxCount(counts []int) int {
	max := counts[0]
	for i := range len(counts) {
		if counts[i] > max {
			max = counts[i]
		}
	}
	return max
}

func increaseCount(counts []int, index, amount int) {
	counts[index] += amount
}


func main() {
	counts := []int {3, 7, 2, 9, 5}
	fmt.Println(counts)

	increaseCount(counts, 2, 10)
	fmt.Println(counts)
	fmt.Println(sumCounts(counts), maxCount(counts))

}