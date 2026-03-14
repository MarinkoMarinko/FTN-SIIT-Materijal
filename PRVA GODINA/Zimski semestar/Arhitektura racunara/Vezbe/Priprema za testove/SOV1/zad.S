# autor: Imenko Prezimić INDEX ra1234-2016
# fajlovi: zad.S
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
.macro KRAJ_PROGRAMA greska
	movl $1, %eax
	movl \greska, %ebx
	int $0x80
.endm
.section .data
	punos: 	.ascii "Unesite string: \0"
	punos_len = .- punos
	pgreska: .ascii "Doslo je do greske u izvrsavanju programa!\n\0"
	pgreska_len = .- pgreska
	psuma: 	.ascii "Suma elemenata niza je: \0"
	psuma_len = .- psuma
	pbroj_oktalnih: .ascii "\nBroj oktalnih elemenata u nizu: \0"
	pbroj_oktalnih_len = .- pbroj_oktalnih
	pbroj_decimalnih: .ascii "\nBroj decimalnih elemenata u nizu: \0"
	pbroj_decimalnih_len = .- pbroj_decimalnih
	max_len = 30
	unos: .fill max_len, 1, '*'
	ispis: .fill max_len, 1, '*'
	ispis_len: .long 0
	greska: .long 0
	zbir: .long 0
	br_dekadnih: .long 0
	br_oktalnih: .long 0
.section .text
.globl main
main:
	ISPIS $punos, $punos_len
	UNOS $unos, $max_len
	movl $unos, %esi
	movl $0, %eax
	movl $10, %ebx
prolaz:
	cmpb $'\n', (%esi)
	je zavrsen_prolaz
	cmpb $'0', (%esi)
	je proveri_broj
	jmp dekadni
proveri_broj:
	movl %esi, %edi
	incl %edi
	cmpb $' ', (%edi)
	je dekadni
	incl br_oktalnih
	movl $8, %ebx
	jmp str_u_broj
dekadni:
	incl br_dekadnih
	movl $10, %ebx
str_u_broj:
	cmpb $' ', (%esi)
	je sledeci_broj
	cmpb $'\n', (%esi)
	je sledeci_broj
	cmpb $'0', (%esi)
	jb greska_karakter
	cmpb $'9', (%esi)
	ja greska_karakter
	movl $0, %edx
	mull %ebx
	jc greska_konverzija
	movl $0, %ecx
	movb (%esi), %cl
	subb $'0', %cl
	addl %ecx, %eax
	incl %esi
	jmp str_u_broj
sledeci_broj:
	addl %eax, zbir
	jc greska_zbir
	movl $0, %eax
	cmpb $'\n', (%esi)
	je zavrsen_prolaz
	incl %esi
	jmp prolaz
zavrsen_prolaz:
	movl zbir, %eax
	movl $10, %ebx
	movl $ispis, %esi
	movl $0, ispis_len
suma_u_str:
	cmpl $0, %eax
	jne suma_loop

	movb $'0', (%esi)
	movb $0, 1(%esi)
	movl $1, ispis_len
	jmp pripremi_konverziju_oktalnog
suma_loop:
	incl ispis_len
	movl $0, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	cmpl $0, %eax
	jne suma_loop
	jmp pripremi_obrtanje_sume

pripremi_obrtanje_sume:
	movb $0, (%esi)
	decl %esi
	movl $ispis, %edi
obrni_sumu:
	cmpl %edi, %esi
	jbe pripremi_konverziju_oktalnog
	movl $0, %ecx
	movl $0, %edx
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni_sumu
pripremi_konverziju_oktalnog:
	ISPIS $psuma, $psuma_len
	ISPIS $ispis, ispis_len

	movb $0, ispis
	movl $0, ispis_len
	movl br_oktalnih, %eax
	movl $10, %ebx
	movl $ispis, %esi
oktalni_u_str:
	cmpl $0, %eax
	jne okt_loop

	movb $'0', (%esi)
	movb $0, 1(%esi)
	movl $1, ispis_len
	jmp pripremi_konverziju_dekadnog
okt_loop:
	incl ispis_len
	movl $0, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	cmpl $0, %eax
	jne okt_loop
	jmp pripremi_obrtanje_oktalnog
pripremi_obrtanje_oktalnog:
	movb $0, (%esi)
	decl %esi
	movl $ispis, %edi
obrni_oktalni:
	cmpl %edi, %esi
	jbe pripremi_konverziju_dekadnog
	movl $0, %ecx
	movl $0, %edx
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni_oktalni
pripremi_konverziju_dekadnog:
	ISPIS $pbroj_oktalnih, $pbroj_oktalnih_len
	ISPIS $ispis, ispis_len
	movb $0, ispis
	movl $0, ispis_len
	movl br_dekadnih, %eax
	movl $10, %ebx
	movl $ispis, %esi
dekadni_u_str:
	cmpl $0, %eax
	jne dek_loop

	movb $'0', (%esi)
	movb $0, 1(%esi)
	movl $1, ispis_len
	jmp ispisi_dekadni
dek_loop:
	incl ispis_len
	movl $0, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	cmpl $0, %eax
	jne dek_loop
	jmp pripremi_obrtanje_dekadnog
pripremi_obrtanje_dekadnog:
	movb $0, (%esi)
	decl %esi
	movl $ispis, %edi
obrni_dekadni:
	cmpl %edi, %esi
	jbe ispisi_dekadni
	movl $0, %ecx
	movl $0, %edx
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni_dekadni
ispisi_dekadni:
	ISPIS $pbroj_decimalnih, $pbroj_decimalnih_len
	ISPIS $ispis, ispis_len
	jmp kraj
greska_karakter:
	movl $1, greska
	ISPIS $pgreska, $pgreska_len
	jmp kraj
greska_konverzija:
	movl $2, greska
	ISPIS $pgreska, $pgreska_len
	jmp kraj
greska_zbir:
	movl $3, greska
	ISPIS $pgreska, $pgreska_len
kraj:
	KRAJ_PROGRAMA greska
