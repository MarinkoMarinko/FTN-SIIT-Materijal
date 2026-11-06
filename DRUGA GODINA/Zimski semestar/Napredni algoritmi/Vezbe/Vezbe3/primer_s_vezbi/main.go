package main

import (
	"fmt"
	"os"
)

func main() {
	s1 := Student{
		Ime:         "pera peric",
		GodinaUpisa: 20222,
		Upisan:      true,
	}

	fmt.Println(s1.Serialize())

	s2 := Student{
		Ime:         "mika mikic",
		GodinaUpisa: 2024,
		Upisan:      false,
	}

	fmt.Println(s2.Serialize())

	file, err := os.OpenFile("students.bin", os.O_CREATE|os.O_RDWR, 0644)
	if err != nil {
		fmt.Println(err)
		return
	}

	_, err = file.Write(s1.Serialize())
	if err != nil {
		fmt.Println(err)
		return
	}

	_, err = file.Write(s2.Serialize())
	if err != nil {
		fmt.Println(err)
		return
	}

	file.Seek(0, 0)

	s3 := Student{}
	s4 := Student{}

	err = s3.Deserialize(file)
	if err != nil {
		fmt.Println(err)
		return
	}

	err = s4.Deserialize(file)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(s3)
	fmt.Println(s4)
}
