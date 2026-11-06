package main

import "fmt"

type BloomFilter struct {
	Name string
	Bits []bool
}

func (bf *BloomFilter) SetBit(index int) {
	bf.Bits[index] = true
}

func (bf BloomFilter) CheckBit(index int) bool {
	return bf.Bits[index]
}

func (bf BloomFilter) CountSetBits() int {
	cnt := 0
	for _, val := range bf.Bits {
		if val {
			cnt += 1
		}
	}
	return cnt
}
func main() {
	bf := BloomFilter {
		Name: "Moj Bloom Filter",
		Bits: make([]bool, 8),
	}

	bf.SetBit(1)
	bf.SetBit(3)
	bf.SetBit(5)
	fmt.Println(bf.Bits)

	fmt.Println(bf.CheckBit(3), bf.CheckBit(4))
	fmt.Println(bf.Name)
	fmt.Println(bf.CountSetBits())
}