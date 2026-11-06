package main

import "fmt"

func main() {
	capacity := 100
	inserted := 75
	newElements := 10

	if inserted + newElements > capacity {
		fmt.Println("Nema dovoljno mesta.")
	} else if inserted + newElements == capacity {
		fmt.Println("Bice potpuno popunjena.")
	} else {
		fmt.Println("Dodavanje uspesno. Trenutno", inserted + newElements, "elemenata")

	}

	if remaining := capacity - inserted - newElements; remaining > 0 {
		fmt.Println("Slobodnih mesta:", remaining)
	}
}