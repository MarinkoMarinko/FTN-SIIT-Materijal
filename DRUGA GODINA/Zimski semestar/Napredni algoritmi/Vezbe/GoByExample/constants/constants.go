package main

import "fmt"

func main() {
	const appName = "Bloom Filter"
	const maxElements = 1000
	const bitsPerByte = 8
	const errorRate = 0.01
	bytesNeeded := maxElements / bitsPerByte

	fmt.Println(appName)
	fmt.Println(maxElements)
	fmt.Println(bytesNeeded)
	fmt.Println(errorRate)

}