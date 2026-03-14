# Aritmeticka sredina niza
.section .data
	NELEM = 10
	niz: .long 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
	suma: .long 0
	ar_sredina: .long 0
	ostatak: .long 0

.section .text
.globl main
main:
	movl $0, %eax        # index
saberi:
	cmpl $NELEM, %eax
	je aritmeticka_sredina
	movl niz(,%eax,4), %esi
	addl %esi, suma      
	incl %eax
	jmp saberi

aritmeticka_sredina:
	movl suma, %eax       
	xorl %edx, %edx       
	movl $NELEM, %ebx
	divl %ebx             
	movl %eax, ar_sredina
	movl %edx, ostatak

kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80

