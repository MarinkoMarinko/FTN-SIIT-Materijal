# Broj cifara u stringu
.section .data
	string1: .ascii "Te67k31s!t***\0"
.section .text
.globl main
main:
	movl $string1, %esi	# pokazivac kroz string
	movl $0, %eax		# brojac
petlja:
	cmpb $0, (%esi)
	je kraj
	cmpb $'0', (%esi)
	jb preskoci
	cmpb $'9', (%esi)
	ja preskoci
	incl %eax
preskoci:
	incl %esi
	jmp petlja
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
