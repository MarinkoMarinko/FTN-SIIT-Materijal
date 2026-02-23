.section .text
.globl saberi
saberi:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %eax	# a
	movl 12(%ebp), %ebx	# b
	addl %ebx, %eax
	movl 16(%ebp), %ecx	# adresa sume
	movl %eax, (%ecx)
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
