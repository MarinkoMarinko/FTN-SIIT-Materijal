# Program koji sabira ASCII vrednosti najmanje i najvece cifre u stringu

.section .data 
    max_len = 50 
    poruka_unos: .ascii "Unesite string: \0" 
    poruka_unos_len = . - poruka_unos 

    unos: .fill max_len, 1, '*' 
    unos_len: .long 0 

    poruka_ispis: .ascii "Izlazni kod programa: \0" 
    poruka_ispis_len = . - poruka_ispis 

    max: .byte 0
    min: .byte 0

    buf: .fill 4,1,0          # buffer za ASCII broj (max 3 cifre + terminator)

.section .text
.globl main
main:

    # ispis poruke za unos
    movl $4, %eax
    movl $1, %ebx
    movl $poruka_unos, %ecx
    movl $poruka_unos_len, %edx
    int $0x80

    # unos stringa
    movl $3, %eax
    movl $0, %ebx
    movl $unos, %ecx
    movl $max_len, %edx
    int $0x80
    movl %eax, unos_len

    movb max, %al
    movb min, %bl

    movl $unos, %esi

nadji_cifru:
    cmpb $'0', (%esi)
    jb preskoci
    cmpb $'9', (%esi)
    ja preskoci
    movb (%esi), %al
    movb (%esi), %bl
    incl %esi
    jmp petlja

preskoci:
    incl %esi
    jmp nadji_cifru

petlja:
    cmpb $'\n', (%esi)
    je proveri
    cmpb $'0', (%esi)
    jb sledeci
    cmpb $'9', (%esi)
    ja sledeci
    cmpb %bl, (%esi)
    jb dodaj_min
    cmpb %al, (%esi)
    jbe sledeci
    movb (%esi), %al

sledeci:
    incl %esi
    jmp petlja

dodaj_min:
    movb (%esi), %bl
    jmp sledeci

proveri:
    cmpb max, %al
    je nema_max
    movb %al, max

vrati:
    cmpb min, %bl
    je nema_min
    movb %bl, min
    cmpb %bl, %al
    je bez_sabiranja
    jmp velicina

nema_max:
    movb $0, max
    jmp vrati

nema_min:
    movb $0, min
    jmp velicina

velicina:
    addb %bl, %al
bez_sabiranja:
    movb %al, max         # rezultat u max

##################################################
# KONVERZIJA max (BYTE) u DECIMAL ASCII u buf
##################################################

    movzbl max, %eax      # EAX = broj 0–255
    movl $buf+3, %esi     # pocinjemo od kraja
    movb $0, (%esi)       # terminator '\0'

convert:
    xorl %edx, %edx
    movl $10, %ecx
    divl %ecx             # EAX = EAX/10, EDX = ostatak
    addb $'0', %dl
    dec %esi
    movb %dl, (%esi)
    testl %eax, %eax
    jnz convert

##################################################
# ISPIS
##################################################

    # ispis poruke
    movl $4, %eax
    movl $1, %ebx
    movl $poruka_ispis, %ecx
    movl $poruka_ispis_len, %edx
    int $0x80

    # ispis broja
    movl $4, %eax
    movl $1, %ebx
    movl %esi, %ecx            # pocetak ascii broja
    movl $buf+3, %edx
    subl %esi, %edx            # duzina
    int $0x80

kraj:
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80

