# Unos i ispis stringa preko sistemskih poziva
.section .data
	max_len = 40
	poruka: .ascii "Unesite Vase ime i prezime: \0"
	poruka_len = . - poruka
	unos: .fill max_len, 1, '*'
	unos_len: .long 0
.section .text
.globl main
main:
	movl $4, %eax		# Sistemski poziv za ispis stringa
	movl $1, %ebx
	movl $poruka, %ecx
	movl $poruka_len, %edx
	int $0x80
	
	movl $3, %eax		# Sistemski poziv za unos stringa
	movl $0, %ebx			
	movl $unos, %ecx
	movl $max_len, %edx
	int $0x80
	
	movl %eax, unos_len 	# Broj unetih karaktera se cuva u %eax
	
	movl $4, %eax
	movl $1, %ebx
	movl $unos, %ecx
	movl unos_len, %edx
	int $0x80
kraj:
	movl $1, %eax
	movl $0, %ebx
	int $0x80
