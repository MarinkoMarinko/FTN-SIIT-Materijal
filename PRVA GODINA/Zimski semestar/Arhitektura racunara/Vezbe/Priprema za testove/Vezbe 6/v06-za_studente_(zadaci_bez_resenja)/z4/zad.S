.section .text
.globl SetParityArray

SetParityArray:
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx
    pushl %esi
    pushl %edi

    movl 8(%ebp), %esi     # adresa niza
    movl $0, %edi          # index
    movl $0, %eax          # broj elemenata sa parity=1

petlja_niza:
    cmpl 12(%ebp), %edi
    je kraj

    movw (%esi), %bx       # BX = element
    andw $0x7FFF, %bx      # ukloni MSB
    movl $0, %ecx          # brojac jedinica

unutrasnja_petlja:
    testw %bx, %bx
    je parnost
    testw $1, %bx
    jz sledeci_bit
    incl %ecx
sledeci_bit:
    shrw $1, %bx
    jmp unutrasnja_petlja

parnost:
    testl $1, %ecx
    jz upis
    orw $0x8000, %bx       # POSTAVI PARITY BIT
    incl %eax              # BROJI GA

upis:
    movw %bx, (%esi)       # UPISI NAZAD U NIZ
    addl $2, %esi
    incl %edi
    jmp petlja_niza

kraj:
    popl %edi
    popl %esi
    popl %ebx
    movl %ebp, %esp
    popl %ebp
    ret
