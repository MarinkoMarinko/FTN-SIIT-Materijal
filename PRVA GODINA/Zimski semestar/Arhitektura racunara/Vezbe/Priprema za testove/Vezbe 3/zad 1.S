# Suma elemenata podniza
.section .data
	ind1: .long 1
	ind2: .long 6
	niz: .long 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
	NELEM = 10
	s: .long 0
.section .text
.globl main
main:
	movl ind1, %eax			# pocetni index
	movl ind2, %ebx			# krajnji index
petlja:
	cmpl %ebx, %eax
	ja kraj
	movl niz(, %eax, 4), %esi	# vrednost elementa na indexu ind1
	addl %esi, s
	incl %eax
	jmp petlja	
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
