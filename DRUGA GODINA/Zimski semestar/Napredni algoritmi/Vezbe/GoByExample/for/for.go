package main

import "fmt"

func main() {
	capacity := 5

	for i := 1; i <= capacity; i++ {
		fmt.Println("Dodajem element:", i)
	}

	i := capacity
	for i > 0 {
		fmt.Println("Preostalo elemenata:", i)
		i -= 1
	}

	fmt.Println("Bloom filter je popunjen!")
}
