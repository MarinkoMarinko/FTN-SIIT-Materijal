package main

import "fmt"

type BloomFilter struct {
	Name 		string
	Size 		int
	HashCount 	int
	Bits 		[]bool

}

func main() {
	bf := BloomFilter{
		Name: 		"Moj Bloom Filter",
		Size: 		8,
		HashCount: 	3,
	 	Bits: 		make([]bool, 8),
	}
	fmt.Println(bf.Name, bf.Size, bf.HashCount)
	bf.Bits[1] = true
	bf.Bits[3] = true
	bf.Bits[5] = true
	fmt.Println(bf.Bits)
	ptr := &bf
	ptr.HashCount = 4
	(*ptr).Size = 4
	ptr.Size = 20
	fmt.Println(bf)
}