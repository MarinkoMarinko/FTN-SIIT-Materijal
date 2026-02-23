.section .text
.globl NZD
NZD:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %eax		# a
	movl 12(%ebp), %ebx		# b
petlja:
	cmpl %ebx, %eax
	je kraj
	ja vece
	subl %eax, %ebx
	jmp petlja
vece:
	subl %ebx, %eax
	jmp petlja
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
