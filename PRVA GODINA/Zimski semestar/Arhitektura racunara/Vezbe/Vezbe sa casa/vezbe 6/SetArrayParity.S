.section .text
.globl SetArrayParity
SetArrayParity:
	pushl %ebp
	movl %esp, %ebp
	pushl $1
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %esi	# adresa niza
	movl $0, %ebx		# brojac bitova
	movl $0, %ecx		# brojac jedinica
	movl $0, %edx		# index
	movl $0, %edi		# suma pariteta
	movw -4(%ebp), %ax	# maska
petlja:
	cmpl $15, %ebx
	je kraj
unutrasnja_petlja:
	cmpl 12(%ebp), %edx
	je parnost
	testw (%esi, %edx, 2), %ax
	jz sledeci_element
	incl %ecx
sledeci_element:
	incl %edx
	jmp unutrasnja_petlja
parnost:
	testl $1, %ecx
	jz sledeci_bit
	incl %edi
sledeci_bit:
	movl $0, %ecx
	movl $0, %edx
	incl %ebx
	shlw $1, %ax
	jmp petlja
kraj:
	movl %edi, %eax
	popl %edi
	popl %esi
	popl %ebx
	addl $4, %esp
	movl %ebp, %esp
	popl %ebp
	ret
