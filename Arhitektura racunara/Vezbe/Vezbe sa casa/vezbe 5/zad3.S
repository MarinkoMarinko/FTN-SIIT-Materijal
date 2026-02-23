# Suma elemenata niza preko potprograma
.section .data
	niz: .long 1, 2, 3, 4, 5
	NELEM =  5
	s: .long 0
.section .text
.globl main
main:
	# int suma_elemenata(int* niz, int n)
	pushl $NELEM		# broj elemenata na stek
	pushl $niz		# adresa niza na stek
	call suma_elemenata
	addl $8, %esp
	movl %eax, s
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
