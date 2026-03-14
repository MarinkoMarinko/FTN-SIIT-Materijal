# Min i max element niza oznacenih brojeva
.section .data
	niz: .long 5, 1, -2, 0, 6, 12, 15, 1, -4, 9
	max: .long 0
	min: .long 0
	NELEM = 10
.section .text
.globl main
main:
	movl $0, %eax			# index
	movl niz(, %eax, 4), %esi
	movl %esi, max
	movl %esi, min
	incl %eax
petlja:
	cmpl $NELEM, %eax
	je kraj
	movl niz(, %eax, 4), %esi
	cmpl max, %esi
	jl proveri_min
	jg dodeli_max
povecaj_index:
	incl %eax
	jmp petlja
proveri_min:
	cmpl min, %esi
	jl dodeli_min
	jmp povecaj_index
dodeli_min:
	movl %esi, min
	jmp povecaj_index
dodeli_max:
	movl %esi, max
	jmp povecaj_index
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
