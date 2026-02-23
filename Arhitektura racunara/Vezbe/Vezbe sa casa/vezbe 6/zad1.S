# Prebrojavanje jedinica u binarnom broju
.section .data
.section .text
.globl main
main:
	movl $123, %eax			# ovaj broj ima 5 jedinica
	movl $0, %ecx
petlja:
	cmpl $0, %eax
	je kraj
	testl $1, %eax
	jz sledeci
	incl %ecx
sledeci:
	shrl $1, %eax
	jmp petlja
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
