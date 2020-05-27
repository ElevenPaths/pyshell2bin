# pyshell2bin

If you work with exploits and shellcode, you already know what shellcode is and how to deal with it. Sometimes it comes with exploits in C, Perl, Python… It usually looks like:

```python
payload = (b"xbfxabxd0x9ax5bxdaxc7xd9x74x24xf4x5ax2bxc9" + "xb1x45x83xc2x04x31x7ax11x03x7ax11xe2x5ex2c" + "x72xd2xa0xcdx83x85x29x28xb2x97x4dx38xe7x27" + ...
```


But sometimes you need a binary file representation of this shellcode, so you can inject it into some file, debug it or for whatever reason. There are all kinds of scripts out there to deal with shellcode and accomplish different tasks. Binary to shellcode, shellcode to binary (only for bash)… But I was not able to find a simple script to get it under Windows. Even finding “xxd” command (make a hexdump) ported to Windows is possible but not easy (it seems to come bundled with Vim for Windows, but it used to be available with unixtools…).
 
Anyhow, here is a simple script in Python that works for Windows and will do the job. It will tolerate dirty shellcode (spaces, returns, concatenation commands…) and will only keep hex characters. Then it uses “write” with “wb” so you get a binary file. Quick and dirty.
