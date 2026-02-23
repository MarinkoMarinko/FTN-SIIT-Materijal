# Zbir prvih n brojeva
.section .data
.section .text
.global main
main:
	movl $5, %eax	# n
	movl $0, %ebx	# zbir
dodaj:
	cmpl $0, %eax	# n == 0
	je kraj
	addl %eax, %ebx
	decl %eax
	jmp dodaj		
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
