# Proizvod preko sabiranja (sa promenjivama)
.section .data
	a: .long 2
	b: .long 3
	p: .long 0
.section .text
.globl main
main:
	movl a, %eax
	movl b, %ebx
	movl p, %ecx
	cmpl %eax, %ebx
	ja zameni
	jmp mnozi
zameni:
	xchgl %eax, %ebx
mnozi:
	cmpl $0, %ebx
	je kraj
	addl %eax, %ecx
	decl %ebx
	jmp mnozi
kraj:
	movl %ecx, p
	movl $1, %eax
	movl $0, %ebx
	int $0x80
