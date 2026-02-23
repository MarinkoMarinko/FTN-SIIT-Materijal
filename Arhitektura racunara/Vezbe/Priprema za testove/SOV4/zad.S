.macro KRAJ greska
	movl $1, %eax
	movl \greska, %ebx
	int $0x80
.endm
.macro ISPIS str, duzina
	movl $4, %eax
	movl $1, %ebx
	movl \str, %ecx
	movl \duzina, %edx
	int $0x80
.endm
.macro UNOS str, duzina
	movl $3, %eax
	movl $0, %ebx
	movl \str, %ecx
	movl \duzina, %edx
	int $0x80
.endm	
.section .data
	poruka1: .ascii "Unesite jednacinu: \0"
	poruka1_len = .- poruka1
	poruka2: .ascii "Resenje: x = \0"
	poruka2_len = .- poruka2
	greska1: .ascii "Greska pri konverziji!\n\0"
	greska1_len = .- greska1
	greska2: .ascii "Greska! Neispravna operacija!\n\0"
	greska2_len = .- greska2
	max_len = 30
	unos: .fill max_len, 1, '*'
	ispis: .fill max_len, 1, '*'
	ispis_len: .long 0
	prvi: .long 0
	drugi: .long 0
	operator: .fill 1, 1, '*'
	greska: .long 0
	br_space: .long 0
.section .text
.globl main
main:
	ISPIS $poruka1, $poruka1_len
	UNOS $unos, $max_len
	movl $unos, %esi			# pokazivac kroz unos
	movl $0, %eax				# broj
	movl $10, %ebx				# baza
	movl $0, %ecx				# temp
prolaz:
	cmpb $'\n', (%esi)
	je dalje
	cmpb $' ', (%esi)
	jne nije_space
	incl br_space
	jmp sledeci
nije_space:
	cmpl $0, br_space
	je broj
	cmpl $1, br_space
	je znak
	cmpl $2, br_space
	je sledeci
	cmpl $3, br_space
	je sledeci
	cmpl $4, br_space
	je broj
broj:		
	cmpb $'0', (%esi)
	jb greska_konverzija
	cmpb $'9', (%esi)
	ja greska_konverzija	
	movl $0, %ecx			
	movb (%esi), %cl
	subb $'0', %cl
	movl $0, %edx
	mull %ebx			# broj *= 10
	addl %ecx, %eax
	jmp sledeci
znak:
	movl %eax, prvi
	movl $0, %eax
	cmpb $'+', (%esi)
	je plus
	cmpb $'-', (%esi)
	je minus
	jmp greska_operator
plus:
	movb $'+', operator
	jmp sledeci
minus:
	movb $'-', operator
sledeci:
	incl %esi
	jmp prolaz
dalje:
	movl %eax, drugi
	movl prvi, %ebx
	subl %ebx, %eax
	cmpb $'+', operator
	je preskoci
	negl %eax
preskoci:
	movl $ispis, %esi
	movl $10, %ebx
int_u_str:
	cmpl $0, %eax
	je pripremi_za_obrtanje
	movl $0, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl ispis_len
	incl %esi
	jmp int_u_str
pripremi_za_obrtanje:
	movb $'\n', (%esi)
	incl %esi
	movb $0, (%esi)
	addl $2, ispis_len
	subl $2, %esi
	movl $ispis, %edi
obrni:
	cmpl %edi, %esi
	jbe ispisi
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni
ispisi:
	ISPIS $poruka2, $poruka2_len
	ISPIS $ispis, ispis_len
	jmp proveri_greske
greska_konverzija:
	movl $1, greska
	jmp proveri_greske
greska_operator:
	movl $2, greska
proveri_greske:
	cmpl $1, greska
	je prva_greska
	cmpl $2, greska
	je druga_greska
	jmp kraj
prva_greska:
	ISPIS $greska1, $greska1_len
	jmp kraj
druga_greska:
	ISPIS $greska2, $greska2_len
kraj:
	KRAJ greska
