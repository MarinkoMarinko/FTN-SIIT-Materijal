# Poredjenje dva oznacena broja u dvostrukoj preciznosti
.section .data
	a: .quad 0x0000000200000001
	b: .quad 0x0000000100000002
.section .text
.globl main
main:
	movl a + 4, %eax		# visi deo broja a
	movl b + 4, %ebx		# visi deo broja b
	cmpl %ebx, %eax
	jg veci
	jl manji
	movl a, %ecx			# nizi deo broja a
	movl b, %edx			# nizi deo broja b
	cmpl %edx, %ecx
	jg veci
	jl manji
	movl $0, %eax
	jmp kraj
veci:
	movl $1, %eax
	jmp kraj
manji:
	movl $-1, %eax
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
