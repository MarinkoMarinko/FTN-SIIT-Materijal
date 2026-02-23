# Sortiranje niza u rastucem redosledu
.section .data
	niz: .word 6, 3, 1, 5, 4, -1, 3, 2, 9, 7
	NELEM = 10
.section .text
.globl main
main:
	movl $0, %eax		# brojac i
	movl $1, %ebx		# brojac j
petlja:
	cmpl $NELEM - 1, %eax
	je kraj
unutrasnja_petlja:
	xorl %ecx, %ecx			# cisti registre
	xorl %edx, %edx			# cisti registre	
	movw niz(, %eax, 2), %cx
	movw niz(, %ebx, 2), %dx
	cmpw %dx, %cx
	jg sortiraj
povecaj_index:
	incl %ebx
	cmpl $NELEM, %ebx
	je vrati_brojac
	jmp unutrasnja_petlja
sortiraj:
	xchgw %dx, %cx
	movw %cx, niz(, %eax, 2)			# ??????
	movw %dx, niz(, %ebx, 2)
	jmp povecaj_index
vrati_brojac:
	incl %eax
	movl %eax, %ebx
	incl %ebx
	jmp petlja
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
