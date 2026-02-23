# autor: Imenko Prezimić INDEX ra1234-2023
# int prebrojNajviseUzastopnih(unsigned long long* vrednost)
.section .text
.globl prebrojNajviseUzastopnih
prebrojNajviseUzastopnih:
	pushl %ebp
	movl %esp, %ebp
	pushl $1		# brojac bitova
	pushl %ebx
	pushl %esi
	pushl %edi
	movl 8(%ebp), %eax
	movl (%eax), %ecx	# nizi deo
	movl 4(%eax), %edx	# visi deo
	xorl %eax, %eax		# movl $0, %eax
	movl $0, %esi		# broj trenutnih nula
	movl $0, %edi		# max broj nula
petlja:
	cmpl $64, -4(%ebp)
	ja gotovo		# ako su sve nule, mora se bar 1 put izvrsiti provera
	cmpl $33, -4(%ebp)
	je zameni
uporedi:
	testl $1, %ecx
	jnz resetuj_brojac
	incl %esi
	jmp sledeci_bit
zameni:
	movl %edx, %ecx
	jmp uporedi
resetuj_brojac:
	movl %esi, %eax
	movl $0, %esi
	cmpl %edi, %eax
	jbe sledeci_bit
	movl %eax, %edi
sledeci_bit:
	incl -4(%ebp)
	shrl $1, %ecx
	jmp petlja
gotovo:
	cmpl %edi, %esi
	jbe kraj
	movl %esi, %edi
kraj:
	movl %edi, %eax
	popl %edi
	popl %esi
	popl %ebx
	addl $4, %esp
	movl %ebp, %esp
	popl %ebp
	ret
