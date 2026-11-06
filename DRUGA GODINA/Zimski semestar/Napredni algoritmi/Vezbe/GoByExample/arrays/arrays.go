package main

import "fmt"

func main() {
	var a [5]int

	a[0] = 3
	a[1] = 7
	a[2] = 2
	a[3] = 9
	a[4] = 5

	fmt.Println(a)
	fmt.Println(len(a))

	var s int = 0
	for i := range(len(a)) {
		s += a[i]
	}
	fmt.Println(s)

	max := a[0]
	for i := range len(a) {
		if a[i] > max {
			max = a[i]
		}
	}
	fmt.Println(max)

	copyCounts := a 
	copyCounts[0] = 100
	fmt.Println(copyCounts)
	fmt.Println(a)
}
