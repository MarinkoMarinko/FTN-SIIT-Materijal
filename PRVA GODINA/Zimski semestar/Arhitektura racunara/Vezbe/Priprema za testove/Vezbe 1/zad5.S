# Deljenje preko oduzimanja, uz pamcenje ostatka
.section .data
.section .text
.globl main
main:
	movl $5, %eax	# prvi broj
	movl $2, %ebx	# drugi broj
	movl $0, %ecx	# kolicnik
	movl $0, %edx	# ostatak
deli:
	cmpl %eax, %ebx
	ja kraj
	incl %ecx
	subl %ebx, %eax
	jmp deli
kraj:
	movl %eax, %edx
	movl $1, %eax
	movl $0, %ebx
	int $0x80
