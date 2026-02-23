# Program koji racuna n-ti stepen broja u dvostrukoj preciznosti
.section .data
	b: .quad 0x1122334455667788
	rezultat: .quad 0x0
	n: .long 3
	greska: .byte 0
.section .text
.globl main
main:
	movl $0, %eax		# zbir viseg dela broja b
	movl $0, %ebx		# zbir nizeg dela broja b
	movl $0, %ecx		# brojac
petlja:
	cmpl n, %ecx
	je prebaci
	addl b, %ebx
	adcl b + 4, %eax
	jc dodaj_gresku		# za oznacene jo
	incl %ecx
	jmp petlja
prebaci:
	movl %eax, rezultat + 4
	movl %ebx, rezultat
	jmp kraj
dodaj_gresku:
	incb greska
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
