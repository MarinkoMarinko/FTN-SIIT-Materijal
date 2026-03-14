# Imenko Prezimic RA 12/2025
# void spoji_stringove(char* str, char* drugi, char* rez, int n);
.section .text
.globl spoji_stringove
spoji_stringove:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %esi		# string koji se modifikuje
	movl 12(%ebp), %edi		# string koji se ubacuje
	movl 16(%ebp),  %eax		# rezultujuci
	movl $0, %ebx			# brojac slova
petlja:
	cmpl 20(%ebp), %ebx
	je ubaci
	cmpb $0, (%esi)
	je kraj
	movb (%esi), %cl
	movb %cl, (%eax)
sledeci:
	incl %esi
	incl %eax
	incl %ebx
	jmp petlja
ubaci:
	movl $0, %ebx
ubaci_petlja:
	cmpl 20(%ebp), %ebx
	je vrati
	movb (%edi), %cl
	movb %cl, (%eax)
	incl %edi
	incl %eax
	incl %ebx
	jmp ubaci_petlja
vrati:
	movl $0, %ebx
	movl 12(%ebp), %edi
	jmp petlja
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
