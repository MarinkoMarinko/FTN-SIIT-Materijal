# Trimovanje stringa (uklanjanje razmaka sa pocetka i kraja stringa)
.section .data
	max_len = 50
	poruka: .ascii "Unesite neki tekst: \0"
	poruka_len = .- poruka
	str_unos: .fill max_len, 1, '*'
	unos_len: .long 0
	str_ispis: .fill max_len, 1, '*'
	ispis_len: .long 0
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
	movl $str_unos, %ecx
	movl $max_len, %edx
	int $0x80
	movl %eax, unos_len
	movl $str_unos, %esi
poslednji:
	cmpb $'\n', (%esi)
	je brojac
	incl %esi
	jmp poslednji
brojac:
	movl $0, %ebx		# brojac za space-ove
	decl %esi		# poslednji karakter u unosu
trim_desno:
	cmpb $' ', (%esi)
	jne dalje
	decl %esi
	incl %ebx
	jmp trim_desno
dalje:
	movl $str_unos, %esi
	movl $str_ispis, %edi
prvi:				# pomera %esi do prvog karaktera koji nije blanko u unosu
	cmpb $' ', (%esi)
	jne trim_levo
	incl %esi
	incl %ebx
	jmp prvi
trim_levo:
	cmpb $0, (%esi)
	je ispis
	movb (%esi), %al 	# prebacuje str unos u str ispis i tako brise space-ove 
				# sa pocetka
	movb %al, (%edi)
	incl %esi
	incl %edi
	jmp trim_levo
ispis:
	movl unos_len, %eax
	subl %ebx, %eax
	decl %eax		# zbog \n iz unosa
	movb $0, (%edi)
	movl %eax, ispis_len	# duzina ispisa = duzina unosa - br. space-ova
	movl $4, %eax
	movl $1, %ebx
	movl $str_ispis, %ecx
	movl ispis_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
