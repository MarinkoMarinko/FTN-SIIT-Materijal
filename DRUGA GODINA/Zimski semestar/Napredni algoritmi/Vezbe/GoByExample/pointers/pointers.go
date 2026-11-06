package main

import "fmt"

func increase(x *int, amount int) {
	*x += amount
}

func swap(a, b *int) {
	*a, *b = *b, *a
}

func main() {
	x := 10
	y := 20

	fmt.Println(x, y)
	increase(&x, 5)
	fmt.Println(x)
	swap(&x, &y)
	fmt.Println(x, y)
}