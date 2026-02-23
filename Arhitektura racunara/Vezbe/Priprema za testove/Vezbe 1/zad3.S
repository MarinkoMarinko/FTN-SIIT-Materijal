# N-ti clan Fibonacijevog niza
.section .data
.section .text
.globl main
main:
	movl $4, %eax	# n
	movl $1, %ebx	# prvi broj
	movl $1, %ecx	# drugi broj
	movl $0, %edx	# temp
	subl $2, %eax	# n = n - 2 (jer su prve dve jedinice)
fibo:
	cmpl $0, %eax
	je kraj
	movl %ecx, %edx
	addl %ebx, %ecx
	movl %edx, %ebx
	decl %eax
	jmp fibo
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
