# Zbir 2 broja preko potprograma
.section .data
	a: .long 5
	b: .long 2
	s: .long 0
.section .text
.globl main
main:
	# void zbir(int a, int b, int* s)
	pushl $s
	pushl b
	pushl a
	call saberi
	addl $12, %esp
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
