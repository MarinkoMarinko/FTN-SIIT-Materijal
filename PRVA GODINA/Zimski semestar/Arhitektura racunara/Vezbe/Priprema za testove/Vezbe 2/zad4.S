# Fibonacijevi brojevi preko promenjivih

.section .data
	n: .long 8
	f: .long 0
.section .text
.globl main
main:
	movl $1, %eax
	movl $1, %ebx
fibo:
	cmpl $2, n
	je kraj
	addl %eax, %ebx
	xchgl %eax, %ebx
	decl n
	jmp fibo
kraj:
	movl %eax, f
	movl $1, %eax
	movl $0, %ebx
	int $0x80
