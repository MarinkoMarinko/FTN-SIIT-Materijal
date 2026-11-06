package main

import "fmt"

func main() {
	choice := 2
	switch choice {
		case 1: 
			fmt.Println("Bloom filter.")
			fmt.Println("Proverava pripadnost elementa skupu.")
		case 2: 
			fmt.Println("Count-Min Sketch.")
			fmt.Println("Procenjunje frekvenciju elemenata.")
		case 3: 
			fmt.Println("HyperLogLog")
			fmt.Println("Procenjuje broj razlicitih elemenata.")
		default:
			fmt.Println("Nepoznata struktura.")
	}

	switch {
		case choice >= 1 && choice <= 3:
			fmt.Println("Ispravan izbor.")
		default:
			fmt.Println("Neispravan izbor.")
	}
}