# Suma elemenata niza preko potprograma
.section .text
.globl suma_elemenata
suma_elemenata:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl $0, %eax		# suma
	movl $0, %ebx		# index
	movl 8(%ebp), %esi	# pokazivac kroz niz
	movl 12(%ebp), %ecx	# broj elemenata niza
petlja:
	cmpl %ecx, %ebx
	je kraj
	addl (%esi, %ebx, 4), %eax
	incl %ebx
	jmp petlja
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
