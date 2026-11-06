package main

import "fmt"

func analyzeCounts(counts[] int) (int, int, float64) {
	s := 0
	max := counts[0]
	for _, val := range counts {
		s += val
		if val > max {
			max = val
		}
	}

	return s, max, float64(s) / float64(len(counts))
}

func main() {
	counts := make([]int, 5)
	counts[0] = 4
	counts[1] = 8
	counts[2] = 12
	counts[3] = 6
	counts[4] = 10


	s, max, avg := analyzeCounts(counts)
	fmt.Println(s, max, avg)

	_, max, _ = analyzeCounts(counts)
	fmt.Println(max)
}
