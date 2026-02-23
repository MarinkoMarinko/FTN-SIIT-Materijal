# NZD 2 broja (uz promenjive)
.section .data
	a: .long 7
	b: .long 3
	nzd: .long 0
.section .text
.globl main
main:
	movl a, %eax
	movl b, %ebx
uporedi:
	cmpl %ebx, %eax
	je kraj
	ja vece
	subl %eax, %ebx
	jmp uporedi
vece:
	subl %ebx, %eax
	jmp uporedi
kraj:
	movl %eax, nzd
	movl $1, %eax
	movl $0, %ebx
	int $0x80
