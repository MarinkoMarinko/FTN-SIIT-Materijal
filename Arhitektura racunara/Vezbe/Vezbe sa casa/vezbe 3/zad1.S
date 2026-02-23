# Suma elemenata niza
.section .data
	NELEM = 10
	niz: .long 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
	s: .long 0
.section .text
.globl main
main:
	movl $niz, %esi		# adresa prvog elementa niza
	movl s, %ebx		# suma
petlja:
	cmpl $niz + NELEM*4, %esi
	jae kraj
	addl (%esi), %ebx	# (%esi) -> vrednost elementa niza
	addl $4, %esi
	jmp petlja
kraj:
	movl %ebx, s
	movl $1, %eax
	movl $0, %ebx
	int $0x80
