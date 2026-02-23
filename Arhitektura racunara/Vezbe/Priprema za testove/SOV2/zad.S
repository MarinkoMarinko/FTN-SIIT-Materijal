# autor: Imenko Prezimić INDEX sv1234-2023

.macro ISPIS unos, len
	movl $4, %eax
	movl $1, %ebx
	movl \unos, %ecx
	movl \len, %edx
	int $0x80
.endm
.macro UNOS unos, len
	movl $3, %eax
	movl $0, %ebx
	movl \unos, %ecx
	movl \len, %edx
	int $0x80
.endm
.section .data
	unos_poruka: .ascii "Unesite niz: \0"
	unos_poruka_len = .- unos_poruka
	greska_poruka: .ascii "Rezultat greske je: \0"
	greska_poruka_len = .- greska_poruka
	istap: .ascii "Iste su aritmeticke sredine pozitivnih i negativnih brojeva!\n\0"
	istap_len = .- istap
	veca_negativna_poruka: .ascii "Veca je aritmeticka sredina negativnih brojeva!\n\0"
	veca_negativna_poruka_len = .- veca_negativna_poruka
	veca_pozitivna_poruka: .ascii "Veca je aritmeticka sredina pozitivnih brojeva!\n\0"
	veca_pozitivna_poruka_len = .- veca_pozitivna_poruka
	max_len = 50
	greska_prekoracenje: .ascii "Prekoracenje!\n\0"
	greska_prekoracenje_len = .- greska_prekoracenje
	greska_operand: .ascii "Neodgovarajuci operand!\n\0"
	greska_operand_len = .- greska_operand
	unos_str: .fill max_len, 1, '*'
	ispis_str: .fill max_len, 1, '*'
	zbir_pozitivnih: .long 0
	zbir_negativnih: .long 0
	br_pozitivnih: .long 0
	br_negativnih: .long 0
	as_pozitivnih: .long 0
	as_negativnih: .long 0
	negativan: .long 0
	greska: .long 0
.section .text
.globl main
main:
	ISPIS $unos_poruka, $unos_poruka_len
	UNOS $unos_str, $max_len
	movl $0, %eax				# broj
	movl $10, %ebx				# baza
	movl $unos_str, %esi			# pokazivac kroz unos
prolaz:
	cmpb $'\n', (%esi)
	je sledeci_broj
	cmpb $' ', (%esi)
	je sledeci_broj
	cmpb $'+', (%esi)
	je sledeci
	cmpb $'-', (%esi)
	je negativan_broj
	cmpb $'0', (%esi)
	jb operand
	cmpb $'9', (%esi)
	ja operand
str_u_int:
	movl $0, %edx
	mull %ebx			# %eax *= 10
	jc prekoracenje
	movl $0, %ecx
	movb (%esi), %cl
	subb $'0', %cl
	addl %ecx, %eax
	jc prekoracenje
	jmp sledeci
negativan_broj:
	incl negativan
	jmp sledeci
sledeci_broj:
	cmpl $1, negativan
	jne preskoci_negativne
	incl br_negativnih
	addl %eax, zbir_negativnih
	jmp resetuj
preskoci_negativne:
	incl br_pozitivnih
	addl %eax, zbir_pozitivnih
resetuj:
	movl $0, %eax
	movl $0, negativan
sledeci:
	cmpb $'\n', (%esi)
	je dalje
	incl %esi
	jmp prolaz
dalje:
	movl zbir_pozitivnih, %eax
	movl $0, %edx
	divl br_pozitivnih
	movl %eax, as_pozitivnih
	movl zbir_negativnih, %eax
	movl $0, %edx
	divl br_negativnih
	movl %eax, as_negativnih
	cmpl as_pozitivnih, %eax	# %eax je as_negativnih
	je isti
	ja veci_neg
	ISPIS $veca_pozitivna_poruka, $veca_pozitivna_poruka_len
	jmp konvertuj_gresku
isti:
	ISPIS $istap, $istap_len
	jmp konvertuj_gresku
veci_neg:
	ISPIS $veca_negativna_poruka, $veca_negativna_poruka_len
	jmp konvertuj_gresku
prekoracenje:
	movl $1, greska
	ISPIS $greska_prekoracenje, $greska_prekoracenje_len
	jmp konvertuj_gresku
operand:
	movl $2, greska
	ISPIS $greska_operand, $greska_operand_len
konvertuj_gresku:
	movl $ispis_str, %esi
	movl greska, %eax
	movl $10, %ebx
	movl $0, %edx
	divl %ebx		# %eax /= 10
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	movb $'\n', (%esi)
	incl %esi
	movb $0, (%esi)
	ISPIS $greska_poruka, $greska_poruka_len
	ISPIS $ispis_str, $1
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
