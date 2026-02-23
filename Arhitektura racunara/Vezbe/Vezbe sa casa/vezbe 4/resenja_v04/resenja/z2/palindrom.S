.section .data
poruka: .ascii "Unesite string: \0"
poruka_len = . - poruka
nijep:  .ascii "String nije palindrom.\n\0"
nijep_len = . - nijep
jestep: .ascii "String je palindrom.\n\0"
jestep_len = . - jestep
unos:   .fill 50,1,42
unos_len: .long 0
palindrom: .long 0
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx			
	movl $poruka, %ecx
	movl $poruka_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx
	movl $unos, %ecx
	movl $50, %edx
	int $0x80
	movl %eax, unos_len
	movl $unos, %esi
	movl $unos, %edi
	addl unos_len, %edi
	subl $2, %edi			# poslednji element pre \n
petlja:
	cmpl %esi, %edi
	jbe jeste_palindrom
	movb (%esi), %cl		# %cl je temp vrednost
	cmpb %cl, (%edi) 
	jne nije_palindrom
	incl %esi
	decl %edi
	jmp petlja
nije_palindrom:
	movl $1, palindrom
	movl $4, %eax
	movl $1, %ebx
	movl $nijep, %ecx
	movl $nijep_len, %edx
	int $0x80
	jmp kraj
jeste_palindrom:
	movl $4, %eax
	movl $1, %ebx
	movl $jestep, %ecx
	movl $jestep_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl palindrom, %ebx
	int $0x80
