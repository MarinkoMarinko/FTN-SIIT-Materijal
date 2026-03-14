# Program koji pretvara mala slova u velika i obrnuto
.section .data
	poruka1: .ascii "Unesite string: \0"
	poruka1_len = . - poruka1
	max_len = 50
	unos: .fill max_len, 1, '*'
	unos_len: .long 0
	poruka2: .ascii "Novi string: \0"
	poruka2_len = . - poruka2
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka1, %ecx
	movl $poruka1_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx
	movl $unos, %ecx
	movl $max_len, %edx
	int $0x80
	movl %eax, unos_len
	movl $unos, %esi		# pokazivac kroz string unos
petlja:
	cmpb $0, (%esi)
	je ispis
	cmpb $'A', (%esi)
	jb sledeci
	cmpb $'z', (%esi)
	ja sledeci			# ako nisu ispunjeni uslovi, nije slovo
	cmpb $'Z', (%esi)
	jbe veliko
	cmpb $'a', (%esi)
	jb sledeci
	subb $32, (%esi)		# pretvara malo slovo u veliko
	jmp sledeci
veliko:
	addb $32, (%esi)		# pretvara veliko slovo u malo
sledeci:
	incl %esi
	jmp petlja
ispis:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka2, %ecx
	movl $poruka2_len, %edx
	int $0x80
	movl $4, %eax
	movl $1, %ebx
	movl $unos, %ecx
	movl unos_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
