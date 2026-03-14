.section .data
    a:      .quad 0x123
    b:      .quad 0x456
    rez:    .quad 0x0
    greska: .byte 0
.section .text
.globl main
main:
    movl a, %eax
    movl a+4, %edx
    movl b, %ebx
    movl b+4, %ecx

    cmpl %ecx, %edx
    jb a_manje
    ja a_vece
    cmpl %ebx, %eax
    jbe a_manje

a_vece:
    xchgl %eax, %ebx
    xchgl %edx, %ecx

a_manje:
    movl %eax, %esi
    movl %ebx, %edi
    movl %ecx, %ebp
    xorl %eax, %eax
    xorl %edx, %edx
petlja:
    cmpl $0, %esi
    jz kraj_mnozenja
    addl %edi, %eax
    adcl %ebp, %edx
    jc postavi_gresku
    decl %esi
    jmp petlja
kraj_mnozenja:
    movl %eax, rez
    movl %edx, rez+4
    jmp kraj
postavi_gresku:
    incl greska
kraj:
    movl $1, %eax
    movl $0, %ebx
    int $0x80
