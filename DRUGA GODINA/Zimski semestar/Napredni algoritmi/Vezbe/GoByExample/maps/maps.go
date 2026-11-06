package main

import (
	"fmt"
)

func main() {
	tags := map[string]int { "go": 10, "python": 15, "java": 8 }
	tags["cpp"] = 12
	tags["go"] += 5
	delete(tags, "java")
	val, ok := tags["rust"]
	fmt.Println(val, ok)
	fmt.Println(len(tags))

	s := 0
	for _, val := range tags {
		s += val
	}
	fmt.Println(s)
	
	maxFreq := 0
	for _, value := range tags {
		if value > maxFreq {
			maxFreq = value
		}
	}
	fmt.Println(maxFreq)
}
