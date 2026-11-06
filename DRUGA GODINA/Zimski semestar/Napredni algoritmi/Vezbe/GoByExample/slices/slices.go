package main

import (
	"fmt"
)

func main() {
	counts := []int {3, 7, 2, 9, 5}

	counts = append(counts, 4)
	counts = append(counts, 6)
	fmt.Println(counts, "len:", len(counts), "cap:", cap(counts))

	selected := counts[1:4]
	fmt.Println(selected)

	selected[0] = 100
	fmt.Println(selected)
	fmt.Println(counts)

	countsCopy := make([]int, len(counts))
	copy(countsCopy, counts)
	countsCopy[0] = 200
	fmt.Println(countsCopy)
	fmt.Println(counts)
}
