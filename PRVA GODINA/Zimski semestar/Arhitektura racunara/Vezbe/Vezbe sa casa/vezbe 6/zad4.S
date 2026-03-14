# Vertikalni paritet
.section .data
	NELEM = 6
	niz: 
	    .word 0b1010101010101010
	    .word 0b0101010101010101
	    .word 0b1100110011001100
	    .word 0b0011001100110011
	    .word 0b1111000011110000
	    .word 0b0000111100001111
	parity_sum: .long 0
.section .text
.globl main
main:
	# unsigned int SetArrayParity(unsigned int niz, int n)
	pushl $NELEM
    	pushl $niz
	call SetArrayParity
	addl $8, %esp
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
