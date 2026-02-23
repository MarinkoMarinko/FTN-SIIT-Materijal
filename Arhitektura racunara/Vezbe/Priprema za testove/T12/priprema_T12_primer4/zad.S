.section .data
	poruka_ulaz: .ascii "Unesite string: \0"
	poruka_ulaz_len = . - poruka_ulaz
	poruka_izlaz: .ascii "Rezultujuci string: \0"
	poruka_izlaz_len = . - poruka_izlaz
	max_len = 50
	unos: .fill max_len, 1, '*'
	unos_len: .long 0
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_ulaz, %ecx			# ispis ulazne poruke
	movl $poruka_ulaz_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx				# unos stringa
	movl $unos, %ecx
	movl $max_len, %edx
	int $0x80
	movl %eax, unos_len
	movl $unos, %esi			# pokazivac kroz string
petlja:
	cmpb $'\n', (%esi)
	je ispisi
	cmpb $'.', (%esi)
	jne sledeci
	movl %esi, %edi				# %edi ce traziti malo slovo
	incl %edi				# sledeci el. posle '.'
nadji:
	cmpb $'\n', (%edi)
	je sledeci
	cmpb $'a', (%edi)
	jb preskoci
	cmpb $'z', (%edi)
	ja preskoci
	subb $32, (%edi)			# povecanje slova
	jmp sledeci
preskoci:
	incl %edi
	jmp nadji
sledeci:
	incl %esi
	jmp petlja
ispisi:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka_izlaz, %ecx		# ispis izlazne poruke
	movl $poruka_izlaz_len, %edx
	int $0x80
	movl $4, %eax
	movl $1, %ebx
	movl $unos, %ecx			# ispis rezultujuceg stringa
	movl unos_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
