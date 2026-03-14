# Program koji sabira dva niza
.section .data
	A: .long 1, 2, 3
	B: .long 4, 5, 6
	C: .fill 3, 4, 0
	NELEM = 3
.section .text
.globl main
main:
	movl $0, %eax
petlja:
	cmpl $NELEM, %eax
	je kraj
	movl A(, %eax, 4), %ebx
	movl B(, %eax, 4), %ecx
	addl %ebx, %ecx
	movl %ecx, C(, %eax, 4)
	incl %eax
	jmp petlja
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
