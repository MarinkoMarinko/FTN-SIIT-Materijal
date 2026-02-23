.section .data
.section .text
.globl main
main:
	movl $5, %eax	# n
	movl $0, %ebx	# zbir
saberi:
	cmpl $0, %eax
	je kraj
	addl %eax, %ebx
	decl %eax
	jmp saberi
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
