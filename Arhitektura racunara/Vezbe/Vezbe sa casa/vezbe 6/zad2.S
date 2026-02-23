# Mnozenje pomocu sabiranja i pomeranja
.section .data
	rezultat: .long 0
.section .text
.globl main
main:
	movl $7, %eax
	movl $5, %ebx
	movl %eax, %ecx
	movl %ebx, %edx
petlja:
	cmpl $0, %edx
	je kraj
	testl $1, %edx
	jz sledeci
	addl %ecx, rezultat
sledeci:
	shll $1, %ecx
	shrl $1, %edx
	jmp petlja
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
