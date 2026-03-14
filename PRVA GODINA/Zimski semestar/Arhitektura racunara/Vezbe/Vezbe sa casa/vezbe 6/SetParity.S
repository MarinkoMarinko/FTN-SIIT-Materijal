.section .text
.globl SetParity
SetParity:
	pushl %ebp
	movl %esp, %ebp
	pushl %esi
	pushl %edi
	pushl %ebx
	movw 8(%ebp), %cx		# broj
	movl $0, %edx			# brojac jedinica
	shlw $1, %cx			# prva cifra se zanemaruje
petlja:
	cmpw $0, %cx
	je parnost
	testw $1, %cx
	jz sledeci 
	incl %edx
sledeci:
	shrw $1, %cx
	jmp petlja
parnost:
	testl $1, %edx
	jz paran
	movl $1, %eax
	jmp kraj
paran:
	movl $0, %eax
kraj:
	popl %ebx
	popl %edi
	popl %esi
	movl %ebp, %esp
	popl %ebp
	ret
