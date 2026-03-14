.section .data
poruka1: .ascii "Unesite ime i prezime: \0"
poruka1_len = .- poruka1
poruka2: .ascii "Vi ste: \0"
poruka2_len = .- poruka2
imeprez: .fill 50,1,42
imeprez_len: .long 0
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx			# "Unesite ime i prezime: " 
	movl $poruka1, %ecx
	movl $poruka1_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx			# unos imena i prezimena
	movl $imeprez, %ecx
	movl $50, %edx
	int $0x80
	movl %eax, imeprez_len
	movl $4, %eax
	movl $1, %ebx			# "Vi ste: "
	movl $poruka2, %ecx
	movl $poruka2_len, %edx
	int $0x80
	movl $imeprez, %esi		# pokazivac kroz unos
petlja:
	cmpb $0, (%esi)
	je ispis
	cmpb $'a', (%esi)		# ako je pre a, onda sigurno nije malo slovo
	jb sledeci
	cmpb $'z', (%esi)		# ako je posle z, onda sigurno nije malo slovo
	ja sledeci
	subl $32, (%esi)		# svako veliko slovo je za 32 manje od svog malog 	
					# slova npr. a(97) i A(65)
sledeci:
	incl %esi
	jmp petlja
ispis:
	movl $4, %eax
	movl $1, %ebx			# ispis imena i prezimena
	movl $imeprez, %ecx
	movl imeprez_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
