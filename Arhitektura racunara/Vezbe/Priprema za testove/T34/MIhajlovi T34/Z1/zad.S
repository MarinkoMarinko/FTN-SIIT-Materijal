# autor: Imenko Prezimic RA 13/2025
# int InvertBits(unsigned int* indeksi, int n);
.section .text
.globl InvertBits
InvertBits:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %esi		# niz indeksa
	movl $1, %edi			# maska
	movl $0, %eax			# niz nula (izlaz)
	movl $0, %ebx			# brojac indeksa u izlazu
petlja:
	cmpl $31, %ebx
	ja kraj
	movl $0, %ecx			# brojac indeksa u nizu
	movl 8(%ebp), %esi
niz_petlja:
	cmpl 12(%ebp), %ecx
	je sledeci
	cmpl (%esi), %ebx
	je invertuj
	incl %ecx
	addl $4, %esi
	jmp niz_petlja
invertuj:
	orl %edi, %eax
sledeci:
	incl %ebx
	shll $1, %edi
	jmp petlja
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
