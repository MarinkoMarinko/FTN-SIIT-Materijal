# autor: Imenko Prezimić INDEX ra1234-2018
# unsigned int setOnes(unsigned int numOnes, unsigned int start)
.section .text
.globl setOnes
setOnes:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %ebx		# broj jedinica
	movl 12(%ebp), %ecx		# start index
	movl $0, %eax			# niz nula
	movl $0x80000000, %esi		# maska sa leva na desno
	movl $1, %edi			# maska sa desna na levo
formiranje_maski:
	cmpl $0, %ecx
	je postavi_jedinice
	shrl $1, %esi			# postavljanje na start index sa obe strane
	shll $1, %edi
	decl %ecx
	jmp formiranje_maski
postavi_jedinice:
	cmpl $0, %ebx
	je kraj
	orl %esi, %eax
	orl %edi, %eax			# postavljanje jedinica i pomeranje maski
	shrl $1, %esi
	shll $1, %edi
	decl %ebx
	jmp postavi_jedinice
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
