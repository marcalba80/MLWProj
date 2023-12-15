	.file	"polym_win.c"
	.globl	_decoder
	.data
	.align 32
_decoder:
	.ascii "M1\300A\261\0\353\32XH1\311H1\333\212\34\10L9\303t\20D0\313\210\34\10H\377\301\353\355\350\341\377\377\377\0"
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "Syntax: %s binary_file\12\0"
LC1:
	.ascii "File %s not found\0"
LC2:
	.ascii "malloc\0"
LC3:
	.ascii "open\0"
LC4:
	.ascii "read\0"
LC5:
	.ascii "\\x%02x\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB19:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%edi
	andl	$-16, %esp
	subl	$608, %esp
	.cfi_offset 7, -12
	call	___main
	leal	280(%esp), %edx
	movl	$0, %eax
	movl	$64, %ecx
	movl	%edx, %edi
	rep stosl
	leal	24(%esp), %edx
	movl	$0, %eax
	movl	$64, %ecx
	movl	%edx, %edi
	rep stosl
	cmpl	$2, 8(%ebp)
	je	L2
	movl	12(%ebp), %eax
	movl	(%eax), %eax
	movl	%eax, 8(%esp)
	movl	$LC0, 4(%esp)
	movl	__imp___iob, %eax
	addl	$64, %eax
	movl	%eax, (%esp)
	call	_fprintf
	movl	$-1, (%esp)
	call	_exit
L2:
	movl	12(%ebp), %eax
	movl	4(%eax), %eax
	movl	%eax, 596(%esp)
	leal	536(%esp), %eax
	movl	%eax, 4(%esp)
	movl	596(%esp), %eax
	movl	%eax, (%esp)
	call	__stat
	testl	%eax, %eax
	jns	L3
	movl	596(%esp), %eax
	movl	%eax, 8(%esp)
	movl	$LC1, 4(%esp)
	movl	__imp___iob, %eax
	addl	$64, %eax
	movl	%eax, (%esp)
	call	_fprintf
	movl	$-1, (%esp)
	call	_exit
L3:
	movl	556(%esp), %eax
	movl	%eax, 592(%esp)
	movl	592(%esp), %eax
	movl	%eax, (%esp)
	call	_malloc
	movl	%eax, 588(%esp)
	cmpl	$0, 588(%esp)
	jne	L4
	movl	$LC2, (%esp)
	call	_perror
	movl	$-1, (%esp)
	call	_exit
L4:
	movl	$0, 4(%esp)
	movl	596(%esp), %eax
	movl	%eax, (%esp)
	call	_open
	movl	%eax, 584(%esp)
	cmpl	$0, 584(%esp)
	jns	L5
	movl	$LC3, (%esp)
	call	_perror
	movl	$-1, (%esp)
	call	__exit
L5:
	movl	592(%esp), %eax
	movl	%eax, 8(%esp)
	movl	588(%esp), %eax
	movl	%eax, 4(%esp)
	movl	584(%esp), %eax
	movl	%eax, (%esp)
	call	_read
	cmpl	592(%esp), %eax
	je	L6
	movl	$LC4, (%esp)
	call	_perror
	movl	$-1, (%esp)
	call	__exit
L6:
	movl	584(%esp), %eax
	movl	%eax, (%esp)
	call	_close
	movl	$0, 600(%esp)
	jmp	L7
L11:
	movl	$1, 604(%esp)
	jmp	L8
L10:
	movl	600(%esp), %edx
	movl	588(%esp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %eax
	movzbl	%al, %eax
	cmpl	604(%esp), %eax
	jne	L9
	movl	604(%esp), %eax
	movl	%eax, %ecx
	leal	280(%esp), %edx
	movl	604(%esp), %eax
	addl	%edx, %eax
	movb	%cl, (%eax)
L9:
	addl	$1, 604(%esp)
L8:
	cmpl	$255, 604(%esp)
	jle	L10
	addl	$1, 600(%esp)
L7:
	movl	600(%esp), %eax
	cmpl	592(%esp), %eax
	jl	L11
	movl	$1, 604(%esp)
	movl	$0, 600(%esp)
	jmp	L12
L14:
	leal	280(%esp), %edx
	movl	604(%esp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %eax
	testb	%al, %al
	jne	L13
	movl	600(%esp), %eax
	leal	1(%eax), %edx
	movl	%edx, 600(%esp)
	movl	604(%esp), %edx
	movb	%dl, 24(%esp,%eax)
L13:
	addl	$1, 604(%esp)
L12:
	cmpl	$255, 604(%esp)
	jle	L14
	movl	$0, (%esp)
	call	_time
	movl	%eax, (%esp)
	call	_srand
	call	_rand
	cltd
	idivl	600(%esp)
	movl	%edx, %eax
	movzbl	24(%esp,%eax), %eax
	movzbl	%al, %eax
	movl	%eax, 580(%esp)
	cmpl	$0, 580(%esp)
	je	L15
	movl	580(%esp), %eax
	movb	%al, _decoder+5
	movl	$_decoder, (%esp)
	call	_strlen
	movl	%eax, 576(%esp)
	movl	576(%esp), %edx
	movl	592(%esp), %eax
	addl	%edx, %eax
	addl	$1, %eax
	movl	%eax, (%esp)
	call	_malloc
	movl	%eax, 572(%esp)
	cmpl	$0, 572(%esp)
	jne	L16
	movl	$LC2, (%esp)
	call	_perror
	movl	$-1, (%esp)
	call	__exit
L16:
	movl	$4, 8(%esp)
	movl	$0, 4(%esp)
	movl	572(%esp), %eax
	movl	%eax, (%esp)
	call	_memset
	movl	$0, 604(%esp)
	jmp	L17
L18:
	movl	604(%esp), %edx
	movl	572(%esp), %eax
	addl	%eax, %edx
	movl	604(%esp), %eax
	addl	$_decoder, %eax
	movzbl	(%eax), %eax
	movb	%al, (%edx)
	addl	$1, 604(%esp)
L17:
	movl	604(%esp), %eax
	cmpl	576(%esp), %eax
	jl	L18
	movl	$0, 604(%esp)
	jmp	L19
L20:
	movl	604(%esp), %edx
	movl	576(%esp), %eax
	addl	%edx, %eax
	movl	%eax, %edx
	movl	572(%esp), %eax
	addl	%edx, %eax
	movl	604(%esp), %ecx
	movl	588(%esp), %edx
	addl	%ecx, %edx
	movzbl	(%edx), %edx
	movl	%edx, %ecx
	movl	580(%esp), %edx
	xorl	%ecx, %edx
	movb	%dl, (%eax)
	addl	$1, 604(%esp)
L19:
	movl	604(%esp), %eax
	cmpl	592(%esp), %eax
	jl	L20
	movl	$0, 604(%esp)
	jmp	L21
L22:
	movl	604(%esp), %edx
	movl	572(%esp), %eax
	addl	%edx, %eax
	movzbl	(%eax), %eax
	movzbl	%al, %eax
	movl	%eax, 4(%esp)
	movl	$LC5, (%esp)
	call	_printf
	addl	$1, 604(%esp)
L21:
	movl	572(%esp), %eax
	movl	%eax, (%esp)
	call	_strlen
	movl	%eax, %edx
	movl	604(%esp), %eax
	cmpl	%eax, %edx
	ja	L22
	movl	$0, %eax
	jmp	L24
L15:
	movl	$78, (%esp)
	call	_putchar
	movl	$-1, (%esp)
	call	__exit
L24:
	movl	-4(%ebp), %edi
	leave
	.cfi_restore 5
	.cfi_restore 7
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE19:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_fprintf;	.scl	2;	.type	32;	.endef
	.def	_exit;	.scl	2;	.type	32;	.endef
	.def	__stat;	.scl	2;	.type	32;	.endef
	.def	_malloc;	.scl	2;	.type	32;	.endef
	.def	_perror;	.scl	2;	.type	32;	.endef
	.def	_open;	.scl	2;	.type	32;	.endef
	.def	__exit;	.scl	2;	.type	32;	.endef
	.def	_read;	.scl	2;	.type	32;	.endef
	.def	_close;	.scl	2;	.type	32;	.endef
	.def	_time;	.scl	2;	.type	32;	.endef
	.def	_srand;	.scl	2;	.type	32;	.endef
	.def	_rand;	.scl	2;	.type	32;	.endef
	.def	_strlen;	.scl	2;	.type	32;	.endef
	.def	_memset;	.scl	2;	.type	32;	.endef
	.def	_printf;	.scl	2;	.type	32;	.endef
	.def	_putchar;	.scl	2;	.type	32;	.endef
