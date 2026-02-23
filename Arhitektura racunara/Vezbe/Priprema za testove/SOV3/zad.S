# autor: Mihajlo Milojevic SV57/2023
# fajlovi: zad.S

# Ako vaše rešenje sadrži dodatne fajlove, stavite njihove nazive u liniju fajlovi
# Na primer, ako imate i potprogram u pp.S, iza fajlovi treba da stoji: zad.S pp.S

.macro ISPIS str, len
	movl $4, %eax
	movl $1, %ebx
	movl \str, %ecx
	movl \len, %edx
	int $0x80
.endm
.macro UNOS str, len
	movl $3, %eax
	movl $0, %ebx
	movl \str, %ecx
	movl \len, %edx
	int $0x80
.endm
.macro KRAJ_PROGRAMA greska
	movl $1, %eax
	movl \greska, %ebx
	int $0x80
.endm
.section .data
	poruka_unos: .ascii "Unesite zirafin pritisak: \0"
	poruka_unos_len = . - poruka_unos
	poruka_ispis: .ascii "Potrebna korekcija: \0"
	poruka_ispis_len = . - poruka_ispis
	poruka_greska: .ascii "Doslo je do greske pri konverziji!\n\0"
	poruka_greska_len = . - poruka_greska
	max_len = 30
	unos_str: .fill max_len, 1, '*'
	ispis_str: .fill max_len, 1, '*'
	ispis_str_len: .long 0
	visi_pritisak: .long 0
	nizi_pritisak: .long 0
	negativan_visi: .long 0
	negativan_nizi: .long 0
	greska: .long 0
.section .text
.globl main
main:
	ISPIS $poruka_unos, $poruka_unos_len
	UNOS $unos_str, $max_len
	movl $0, %eax		# broj
	movl $10, %ebx		# baza
	movl $unos_str, %esi	# pokazivac kroz unos
prolaz:
	cmpb $'\n', (%esi)
	je dalje
	cmpb $'/',(%esi)
	je resetuj
	cmpb $'0', (%esi)
	jb postavi_gresku
	cmpb $'9', (%esi)
	ja postavi_gresku
	movl $0, %edx
	mull %ebx		# %eax *= 10
	movl $0, %ecx
	movb (%esi), %cl
	subb $'0', %cl
	addl %ecx, %eax
	jmp sledeci
resetuj:
	movl %eax, visi_pritisak
	movl $0, %eax
sledeci:
	incl %esi
	jmp prolaz
dalje:
	movl %eax, nizi_pritisak
	cmpl $280, visi_pritisak
	ja postavi_negativan_visi
	cmpl $240, visi_pritisak
	jb postavi_pozitivan_visi
	movl $0, visi_pritisak
postavi_nizi_pritisak:
	cmpl $200, nizi_pritisak
	ja postavi_negativan_nizi
	cmpl $160, nizi_pritisak
	jb postavi_pozitivan_nizi
	movl $0, nizi_pritisak
	jmp pripremi_konverziju_viseg
postavi_negativan_visi:
	movl $1, negativan_visi
	subl $280, visi_pritisak
	jmp postavi_nizi_pritisak
postavi_pozitivan_visi:
	movl $0, negativan_visi
	movl $240, %ecx
	subl visi_pritisak, %ecx
	movl %ecx, visi_pritisak
	jmp postavi_nizi_pritisak
postavi_negativan_nizi:
	movl $1, negativan_nizi
	subl $200, nizi_pritisak
	jmp pripremi_konverziju_viseg
postavi_pozitivan_nizi:
	movl $0, negativan_nizi
	movl $160, %ecx
	subl nizi_pritisak, %ecx
	movl %ecx, nizi_pritisak
	jmp pripremi_konverziju_viseg
pripremi_konverziju_viseg:
	movl visi_pritisak, %eax
	movl $10, %ebx
	movl $ispis_str, %esi
	cmpl $0, %eax
	je preskoci_konverziju_viseg
	cmpl $1, negativan_visi
	jne upisi_plus_viseg
	movb $'-', (%esi)
	jmp pomeri
upisi_plus_viseg:
	movb $'+', (%esi)
pomeri:
	incl ispis_str_len
	incl %esi
konverzija_viseg:
	cmpl $0, %eax
	je pripremi_obrtanje_viseg
	movl $0, %edx
	divl %ebx				# %eax /= 10
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	incl ispis_str_len
	jmp konverzija_viseg
pripremi_obrtanje_viseg:
	movl %esi, %eax
	decl %esi
	movl $ispis_str, %edi
	incl %edi
obrni_visi:
	cmpl %esi, %edi
	jae pripremi_konverziju_nizeg
	movl $0, %ecx
	movl $0, %edx
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni_visi
preskoci_konverziju_viseg:
	movb $'0', (%esi)
	incl %esi
	movl %esi, %eax
	incl ispis_str_len
pripremi_konverziju_nizeg:
	movl %eax, %esi
	movb $'/', (%esi)
	incl %esi
	incl ispis_str_len
	movl nizi_pritisak, %eax
	movl $10, %ebx
	cmpl $0, %eax
	je preskoci_konverziju_nizeg
	cmpl $1, negativan_nizi
	jne upisi_plus_nizeg
	movb $'-', (%esi)
	jmp pomeri_nizi
upisi_plus_nizeg:
	movb $'+', (%esi)
pomeri_nizi:
	incl %esi
	movl %esi, %edi
	incl ispis_str_len
konverzija_nizi:
	cmpl $0, %eax
	je pripremi_obrtanje_nizeg
	movl $0, %edx
	divl %ebx			# %eax /= 10
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	incl ispis_str_len
	jmp konverzija_nizi	
pripremi_obrtanje_nizeg:
	movl %esi, %eax
	decl %esi
obrni_nizi:
	cmpl %esi, %edi
	jae postavi_kraj
	movl $0, %ecx
	movl $0, %edx
	movb (%edi), %cl
	movb (%esi), %dl
	movb %cl, (%esi)
	movb %dl, (%edi)
	incl %edi
	decl %esi
	jmp obrni_nizi
preskoci_konverziju_nizeg:
	movb $'0', (%esi)
	incl %esi
	movb $'\n', (%esi)
	incl ispis_str_len
	jmp ispisi
postavi_kraj:
	movl %eax, %esi
	movb $'\n', (%esi)
	incl ispis_str_len
ispisi:
	ISPIS $poruka_ispis, $poruka_ispis_len
	ISPIS $ispis_str, ispis_str_len
	jmp kraj
postavi_gresku:
	ISPIS $poruka_greska, $poruka_greska_len
	incl greska
kraj:
	KRAJ_PROGRAMA greska
