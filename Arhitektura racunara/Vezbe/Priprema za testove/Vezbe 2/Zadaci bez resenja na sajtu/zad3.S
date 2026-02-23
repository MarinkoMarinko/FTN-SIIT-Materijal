# Oduzimanje dva neoznacena broja u dvostrukoj preciznosti
.section .data
	a: .quad 0x1122334455667788
	b: .quad 0x0011223344556677
	greska: .byte 0
.section .text
.globl main
main:
	movl a, %eax			# nizi deo broja a
	movl b, %ebx			# nizi deo broja b
	movl a + 4, %ecx		# visi deo broja a
	movl b + 4, %edx		# visi deo broja b
	subl %ebx, %eax
	sbbl %edx, %ecx			# oduzima i b i prenos sa oduzimanja nizih delova
	jnc kraj
	incb greska
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
