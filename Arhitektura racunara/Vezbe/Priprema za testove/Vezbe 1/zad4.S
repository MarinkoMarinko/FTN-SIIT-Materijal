# Faktorijel broja n
.section .data
.section .text
.globl main
main:
	movl $1, %eax	# faktorijel
	movl $4, %ebx	# n
faktorijel:
	cmpl $1, %ebx
	je kraj
	mull %ebx
	decl %ebx
	jmp faktorijel
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
