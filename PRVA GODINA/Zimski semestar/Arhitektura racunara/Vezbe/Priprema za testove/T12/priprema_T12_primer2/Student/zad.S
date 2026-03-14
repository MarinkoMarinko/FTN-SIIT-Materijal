#autor: Imenko Prezimić INDEX ra1234-2015

.section .data
	ulaz_poruka: .ascii "Unesite string: \0"
	ulaz_len = . - ulaz_poruka
	izlaz_poruka: .ascii "Rezultujuci string: \0"
	izlaz_len = . - izlaz_poruka
	ulaz_max = 50
	unos: .fill ulaz_max, 1, '*'
	unos_len: .long 0
	ispis: .fill ulaz_max, 1, '*'
	ispis_len: .long 0
	delilac: .long 2
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx
	movl $ulaz_poruka, %ecx
	movl $ulaz_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx
	movl $unos, %ecx
	movl $ulaz_max, %edx
	int $0x80
	movl %eax, unos_len
	movl %eax, ispis_len
	movl $unos, %esi		# pokazivac kroz string unos
	movl $ispis, %edi		# pokazivac kroz string ispis
	addl ispis_len, %edi		# postavljanje na kraj stringa ispis
	movb $0, (%edi)
	decl %edi
	movb $'\n', (%edi)
	decl %edi			# poslednji element pre \n
	movl $0, %ebx			# brojac karaktera
obrni:
	cmpb $'\n', (%esi)
	je ispisi
	incl %ebx
	movl %ebx, %eax			# %eax je temp
	xorl %edx, %edx
	divl delilac			# delilac = 2
	cmpl $0, %edx
	je zameni
	movb (%esi), %al
	movb %al, (%edi)
sledeci:
	incl %esi
	decl %edi
	jmp obrni
zameni:
	movb $'?', (%edi)
	jmp sledeci
ispisi:
	movl $4, %eax
	movl $1, %ebx
	movl $izlaz_poruka, %ecx
	movl $izlaz_len, %edx
	int $0x80
	movl $4, %eax
	movl $1, %ebx
	movl $ispis, %ecx
	movl ispis_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80 
