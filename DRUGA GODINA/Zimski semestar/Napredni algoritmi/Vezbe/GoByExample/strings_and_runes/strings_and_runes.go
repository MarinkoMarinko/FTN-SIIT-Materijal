package main

import "fmt"

func countRunes(s string) int {
	cnt := 0
	for range s {
		cnt += 1
	}
	return cnt
}

func main() {
	word := "Go😊ć"
	fmt.Println(word)
	fmt.Println(len(word))

	var runes []rune = []rune(word)
	fmt.Println(len(runes))
	for idx, c := range word {
		fmt.Printf("%d: %c\n", idx, c)
	}
	fmt.Println(countRunes(word))
}