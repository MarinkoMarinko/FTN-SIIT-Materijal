# Mnozenje dva broja pomocu sabiranja
.section .data
.section .text
.globl main
main:
	movl $2, %eax		# prvi broj
	movl $3, %ebx		# drugi broj
	movl $0, %ecx		# zbir
	movl $0, %edx		# brojac
	cmpl %ebx, %eax
	ja zameni
	jmp mnozi
zameni:
	xchgl %eax, %ebx
mnozi:
	cmpl %edx, %eax
	je kraj
	addl %ebx, %ecx
	incl %edx
	jmp mnozi
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
