# Horizontalni paritet za binarni broj
.section .data
.section .text
.globl main
main:
	movl $7, %ebx
	# unsigned short SetParity(unsigned short x)
	pushl %ebx
	call SetParity
	addl $4, %esp
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
