# Zbir 2 broja
.section .data
.section .text
.global main
main:
	movl $3, %eax
	movl $2, %ebx
	addl %ebx, %eax		# a = a + b
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
