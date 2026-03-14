# autor: Imenko Prezimić INDEX ra1234-2023
# int prebrojPalindrome(unsigned long long* niz, int n);
.section .text
.globl prebrojPalindrome
prebrojPalindrome:
	pushl %ebp
	movl %esp, %ebp
	pushl $0				# broj palindroma
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %eax			# pokazivac kroz niz		
	movl $1, %esi				# maska nizih bitova
	movl $0x80000000, %edi			# maska visih bitova
	movl $0, %ebx				# brojac bitova
petlja:
	cmpl $0, 12(%ebp)
	je kraj
palindrom:
	cmpl $31, %ebx
	ja jeste_palindrom
	movl (%eax), %ecx			# nizi deo
	movl 4(%eax), %edx			# visi deo
	testl %edi, %edx
	jz proveri_nizi_nula
	testl %esi, %ecx
	jz sledeci_element
	jmp sledeci_bit
proveri_nizi_nula:
	testl %esi, %ecx
	jnz sledeci_element
sledeci_bit:
	incl %ebx
	shll $1, %esi
	shrl $1, %edi
	jmp palindrom
jeste_palindrom:
	incl -4(%ebp)
sledeci_element:
	addl $8, %eax
	movl $0, %ebx
	decl 12(%ebp)
	movl $1, %esi				
	movl $0x80000000, %edi
	jmp petlja
kraj:
	movl -4(%ebp), %eax
	popl %edi
	popl %esi
	popl %ebx
	addl $4, %esp
	movl %ebp, %esp
	popl %ebp
	ret
