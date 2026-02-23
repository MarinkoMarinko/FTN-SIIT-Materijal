.section .data
a: .quad 0x1122334455667788
b: .quad 0x1122334455667788
.section .text
.globl main
main:
	movl a + 4, %eax			# vecih 4 bajta
	movl b + 4, %ebx			# vecih 4 bajta
	cmpl %ebx, %eax
	ja veci
	jb manji
	movl a, %ecx				# manjih 4 bajta
	movl b, %edx				# manjih 4 bajta
	cmpl %edx, %ecx
	ja veci
	jb manji
	je jednako
veci: 
	movl $1, %eax
	jmp kraj
manji:
	movl $-1, %eax
	jmp kraj
jednako:
	movl $0, %eax
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
