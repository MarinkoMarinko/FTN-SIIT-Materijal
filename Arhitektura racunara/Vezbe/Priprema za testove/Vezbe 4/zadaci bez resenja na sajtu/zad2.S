# Konkatenacija stringova
.section .data
	max_len = 50
	max_ispis = 2 * max_len
	poruka1: .ascii "Unesite prvi string: \0"
	poruka1_len = . - poruka1
	poruka2: .ascii "Unesite drugi string: \0"
	poruka2_len = . - poruka2
	poruka3: .ascii "Spojeno: \0"
	poruka3_len = . - poruka3
	str1: .fill max_len, 1, '*'
	str2: .fill max_len, 1, '*'
	str3: .fill max_ispis, 1, '*'
	str1_len: .long 0
	str2_len: .long 0
	str3_len: .long 0
.section .text
.globl main
main:
	movl $4, %eax
	movl $1, %ebx
	movl $poruka1, %ecx
	movl $poruka1_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx
	movl $str1, %ecx
	movl $50, %edx
	int $0x80
	movl %eax, str1_len
	movl $4, %eax
	movl $1, %ebx
	movl $poruka2, %ecx
	movl $poruka2_len, %edx
	int $0x80
	movl $3, %eax
	movl $0, %ebx
	movl $str2, %ecx
	movl $max_len, %edx
	int $0x80
	movl %eax, str2_len
	movl $str1, %esi
	movl $str2, %edi
	movl $str3, %ecx	
prebaci_prvi:
	cmpb $'\n', (%esi)
	je prebaci_drugi
	movb (%esi), %al
	movb %al, (%ecx)
	incl %esi
	incl %ecx
	jmp prebaci_prvi
prebaci_drugi:
	cmpb $'\n', (%edi)
	je ispis
	movb (%edi), %al
	movb %al, (%ecx)
	incl %edi
	incl %ecx
	jmp prebaci_drugi
ispis:
	movb $0, (%ecx)
	movl str1_len, %eax
	movl str2_len, %ebx	
	addl %ebx, %eax
	subl $2, %eax		# jer u oba stringa ima po \n, sto se ne racuna
	movl %eax, str3_len
	movl $4, %eax
	movl $1, %ebx
	movl $poruka3, %ecx
	movl $poruka3_len, %edx
	int $0x80
	movl $4, %eax
	movl $1, %ebx
	movl $str3, %ecx
	movl str3_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
