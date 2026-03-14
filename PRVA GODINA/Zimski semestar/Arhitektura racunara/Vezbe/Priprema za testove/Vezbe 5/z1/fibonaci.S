# N-ti broj fibonacijevog niza (1, 1, 2, 3, 5, 8, 13...) preko potprograma
.section .text
.globl fibonaci
fibonaci:
	pushl %ebp
	movl %esp, %ebp
	pushl $1			# x
	pushl $1			# y
	pushl %ebx
	pushl %esi
	pushl %edi
	movl $0, %eax
	cmpl $3, 8(%ebp)		# ako je n < 3, greska
	jb prebaci_gresku
	movl -4(%ebp), %eax		# x = 1
	movl -8(%ebp), %ebx		# y = 1
	movl $0, %ecx			# brojac
	subl $2, 8(%ebp)		# n = n - 2
petlja:
	cmpl %ecx, 8(%ebp)		# brojac == n
	je prebaci_broj
	xchgl %ebx, %eax		# x i y menjaju vrednosti
	addl %eax, %ebx
	jc prebaci_gresku
	incl %ecx
	jmp petlja
prebaci_broj:
	movl 12(%ebp), %esi
	movl %ebx, (%esi)		# prebacivanje broja na adresu prom. f_broj
	movl $0, %eax			# nema greske
	jmp kraj
prebaci_gresku:
	movl $1, %eax
kraj:
	popl %edi
	popl %esi
	popl %ebx
	addl $8, %esp			# brisanje lokalnih promenjivih sa steka
	movl %ebp, %esp
	popl %ebp
	ret
