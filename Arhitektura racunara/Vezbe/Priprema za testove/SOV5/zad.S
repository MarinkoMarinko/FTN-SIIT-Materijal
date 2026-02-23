# Unesite niz: 0 2 3 1 2	(n >= 0 i samo dekadni)
# Ako je neopadajuci ispisati sumu niza
# Ako nije neopadajuci, ispisati poruku "Niz NIJE neopadajuc!"
# Greske: operand (1) i prekoracenje prilikom unosa i sabiranja (2)
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
	unos_msg: .ascii "Unesite niz: \0"
	unos_msg_len = .- unos_msg
	opadajuc_msg: .ascii "Niz NIJE neopadajuc!\n\0"
	opadajuc_msg_len = .- opadajuc_msg
	suma_msg: .ascii "Suma niza: \0"
	suma_msg_len = .- suma_msg
	greska_operand_msg: .ascii "Pogresan operand!\n\0"
	greska_operand_msg_len = .- greska_operand_msg
	greska_prekoracenje_msg: .ascii "Prekoracenje!\n\0"
	greska_prekoracenje_msg_len = .- greska_prekoracenje_msg
	max_len = 50
	unos: .fill max_len, 1, '*'
	ispis: .fill max_len, 1, '*'
	ispis_len: .long 0
	broj: .long 0
	suma: .long 0
	greska: .long 0
.section .text
.globl main
main:
	ISPIS $unos_msg, $unos_msg_len
	UNOS $unos, $max_len
	movl $0, %eax		# broj
	movl $10, %ebx		# baza
	movl $unos, %esi	# pokazivac kroz unos
prolaz:
	cmpb $'\n', (%esi)
	je sledeci_broj
	cmpb $' ', (%esi)
	je sledeci_broj
	cmpb $'0', (%esi)
	jb greska_operand
	cmpb $'9', (%esi)
	ja greska_operand
	movl $0, %edx
	mull %ebx		# %eax *= 10
	jc greska_prekoracenje
	movl $0, %ecx
	movb (%esi), %cl
	subb $'0', %cl
	addl %ecx, %eax
	jmp sledeci
sledeci_broj:
	cmpl broj, %eax
	jb opadajuc_niz
	movl %eax, broj
	jc greska_prekoracenje
	addl %eax, suma
	jc greska_prekoracenje
	movl $0, %eax
	cmpb $'\n', (%esi)
	je dalje
sledeci:
	incl %esi
	jmp prolaz
dalje:
	movl $ispis, %esi		# pokazivac kroz ispis
	movl suma, %eax			# suma
	movl $10, %ebx			# baza
int_u_str:
	movl $0, %edx
	divl %ebx			# %eax /= 10
	addb $'0', %dl
	movb %dl, (%esi)
	incl %esi
	incl ispis_len
	cmpl $0, %eax
	je pripremi
	jmp int_u_str
pripremi:
	movb $'\n', (%esi)
	incl %esi
	movb $0, (%esi)
	subl $2, %esi
	addl $2, ispis_len
	movl $ispis, %edi
obrni:
	cmpl %esi, %edi
	jae ispisi_sumu
	xorl %ecx, %ecx
	xorl %edx, %edx
	movb (%esi), %cl
	movb (%edi), %dl
	movb %dl, (%esi)
	movb %cl, (%edi)
	incl %edi
	decl %esi
	jmp obrni
ispisi_sumu:
	ISPIS $suma_msg, $suma_msg_len
	ISPIS $ispis, ispis_len
	jmp kraj
opadajuc_niz:
	ISPIS $opadajuc_msg, $opadajuc_msg_len
	jmp kraj
greska_operand:
	movl $1, greska
	ISPIS $greska_operand_msg, $greska_operand_msg_len
	jmp kraj
greska_prekoracenje:
	movl $2, greska
	ISPIS $greska_prekoracenje_msg, $greska_prekoracenje_msg_len
kraj:
	KRAJ_PROGRAMA greska
