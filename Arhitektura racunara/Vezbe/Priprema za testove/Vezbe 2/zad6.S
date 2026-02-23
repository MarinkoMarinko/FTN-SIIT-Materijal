# Faktorijel broja n (uz promenjive)
.section .data
	n: .long 5
	p: .long 1
.section .text
.globl main
main:
	movl p, %eax
mnozi:
	cmpl $1, n
	je kraj
	mull n
	decl n
	jmp mnozi
kraj:
	movl %eax, p
	movl $1, %eax
	movl $0, %ebx
	int $0x80
