# NZD dva broja koristeci potprogram
.section .data
	a: .long 12
	b: .long 8
	nzd: .long 0
.section .text
.globl main
main:
	# int NZD(int a, int b)
	pushl b
	pushl a
	call NZD
	addl $8, %esp
	movl %eax, nzd
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
