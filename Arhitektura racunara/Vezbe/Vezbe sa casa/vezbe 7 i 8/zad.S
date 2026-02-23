# Konvertovanje iz stringa u broj, mnozenje sa 2 i konvertovanje nazad u string
.macro kraj_programa greska=$0
	movl $1, %eax
	movl \greska, %ebx
	int $0x80
.endm
.macro ispis_makro str, str_len
	movl $4, %eax
	movl $1, %ebx
	movl \str, %ecx
	movl \str_len, %edx
	int $0x80
.endm
.macro unos_makro str, str_len
	movl $3, %eax
	movl $0, %ebx
	movl \str, %ecx
	movl \str_len, %edx
	int $0x80
.endm
.section .data
	poruka1: .ascii "Unesite broj: \0"
	poruka1_len = .- poruka1
	poruka2: .ascii "Broj pomnozen sa 2 je: \0"
	poruka2_len = .- poruka2
	greska_poruka: .ascii "Doslo je do greske! Pokusajte ponovo!\n\0"
	greska_poruka_len = .- greska_poruka
	max_len = 30
	unos: .fill max_len, 1, '*'
	ispis: .fill max_len, 1, '*'
	ispis_len: .long 0
	greska: .long 0
	negativan: .byte 0
.section .text
.globl main
main:
	ispis_makro $poruka1, $poruka1_len
	unos_makro $unos, $max_len
	movl $unos, %esi	# pokazivac kroz unos
	cmpb $'\n', (%esi)	# ako ima samo '\n', korisnik je kliknuo samo Enter
	je postavi_gresku
	cmpb $'-', (%esi)
	jne preskoci
	incl %esi
	cmpb $'\n', (%esi)	# ako je unet samo "-" bez broja, greska
	je postavi_gresku	
	incb negativan
preskoci:
	movl $0, %eax		# broj
	movl $10, %ebx		# baza
pretvori_u_broj:
	cmpb $'\n', (%esi)
	je dalje
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
	incl %esi
	jmp pretvori_u_broj
dalje:
	movl $2, %ebx
	movl $0, %edx
	mull %ebx		# broj mnozimo sa 2
	movl $ispis, %esi	# ako je br. negativan, dodacemo samo - u string (dole)
	movl $10, %ebx		
pretvori_u_string:
	cmpl $0, %eax
	je postavi_kraj
	movl $0, %edx
	divl %ebx
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	incl ispis_len
	jmp pretvori_u_string
postavi_kraj:
	cmpb $1, negativan
	jne preskoci_minus
	movb $'-', (%esi)
	incl %esi
	incl ispis_len
preskoci_minus:
	movb $'\n', (%esi)
	incl %esi
	movb $0, (%esi)
	addl $2, ispis_len
	subl $2, %esi
	movl $ispis, %edi
obrni:
	cmpl %edi, %esi
	jbe ispisi_rezultat
	movb (%esi), %cl
	movb (%edi), %dl
	movb %cl, (%edi)
	movb %dl, (%esi)
	incl %edi
	decl %esi
	jmp obrni
ispisi_rezultat:
	ispis_makro $poruka2, $poruka2_len
	ispis_makro $ispis, ispis_len
	jmp kraj
postavi_gresku:
	movl $1, greska
	ispis_makro $greska_poruka, $greska_poruka_len
kraj:
	kraj_programa greska
