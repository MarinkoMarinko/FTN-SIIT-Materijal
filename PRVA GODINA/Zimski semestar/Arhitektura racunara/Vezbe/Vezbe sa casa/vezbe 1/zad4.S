# Poredjenje b i c i upisivanje u a
.section .data
.section .text
.globl main
main:
	movl $2, %ebx
	movl $5, %ecx
	cmpl %ecx, %ebx
	je jednako
	ja vece
	jb manje
jednako:
	movl $0, %eax
	jmp kraj
vece:
	movl $1, %eax
	jmp kraj
manje:
	movl $2, %eax
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
