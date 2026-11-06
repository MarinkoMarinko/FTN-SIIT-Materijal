package main

import (
	"encoding/binary"
	"os"
)

type Student struct {
	Upisan      bool
	GodinaUpisa int64
	Ime         string
}

func (s Student) Serialize() []byte {
	b := make([]byte, 0)

	// polje Upisan
	if s.Upisan {
		b = append(b, 1)
	} else {
		b = append(b, 0)
	}

	// polje GodinaUpisa
	guBytes := make([]byte, 8)
	binary.BigEndian.PutUint64(guBytes, uint64(s.GodinaUpisa))
	b = append(b, guBytes...)

	// polje Ime
	imeBytes := []byte(s.Ime)
	imeLen := len(imeBytes)
	imeLenBytes := make([]byte, 4)
	binary.BigEndian.PutUint32(imeLenBytes, uint32(imeLen))
	b = append(b, imeLenBytes...)
	b = append(b, imeBytes...)

	return b
}

func (s *Student) Deserialize(file *os.File) error {
	// polje Upisan
	upisanBytes := make([]byte, 1)
	_, err := file.Read(upisanBytes)
	if err != nil {
		return err
	}
	if upisanBytes[0] == 0 {
		s.Upisan = false
	} else {
		s.Upisan = true
	}

	// polje GodinaUpisa
	godinaUpisaBytes := make([]byte, 8)
	_, err = file.Read(godinaUpisaBytes)
	if err != nil {
		return err
	}
	godinaUpisa := binary.BigEndian.Uint64(godinaUpisaBytes)
	s.GodinaUpisa = int64(godinaUpisa)

	// polje Ime
	imeLenBytes := make([]byte, 4)
	_, err = file.Read(imeLenBytes)
	if err != nil {
		return err
	}
	imeLen := binary.BigEndian.Uint32(imeLenBytes)
	imeBytes := make([]byte, imeLen)
	_, err = file.Read(imeBytes)
	if err != nil {
		return err
	}
	s.Ime = string(imeBytes)

	return nil
}
