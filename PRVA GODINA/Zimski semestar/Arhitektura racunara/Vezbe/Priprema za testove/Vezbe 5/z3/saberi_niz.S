.section .text
.globl saberi_niz
saberi_niz:
	pushl %ebp
	movl %esp, %ebp
	pushl %ebx
	pushl %esi
	pushl %edi	
	cmpl $0, 20(%ebp)		# ako je n manje ili jednako nula, greska
	jbe postavi_gresku		
	movl 8(%ebp), %esi		# adresa 1. niza
	movl 12(%ebp), %edi		# adresa 2. niza
	movl 16(%ebp), %ebx		# adresa izlaznog niza
	movl 20(%ebp), %ecx		# n
petlja:
	cmpl $0, %ecx
	je nema_greske
	movl (%esi), %eax		# nizi deo elementa 1. niza
	addl (%edi), %eax		# sabiranje nizih delova
	movl 4(%esi), %edx		# visi deo elementa 1. niza
	adcl 4(%edi), %edx		# sabiranje visih delova
	jo postavi_gresku
	movl %eax, (%ebx)		# prebacivanje zbira nizih delova u niz
	movl %edx, 4(%ebx)		# prebacivanje zbira visih delova u niz
	addl $8, %esi			# sledeci element 1. niza
	addl $8, %edi			# sledeci element 2. niza
	addl $8, %ebx			# sledeci element izlaznog niza
	decl %ecx
	jmp petlja
nema_greske:
	movl $0, %eax	
	jmp kraj
postavi_gresku:
	movl $1, %eax
kraj:
	popl %edi
	popl %esi
	popl %ebx
	movl %ebp, %esp
	popl %ebp
	ret
