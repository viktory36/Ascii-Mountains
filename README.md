## Ascii-Mountains
Draws mountain ranges on the terminal, implemented in Python 3 using VT100 or xterm control sequences/ANSI escape sequences.

<br />

### About

This should serve as a reference for understanding, enabling, and working with terminal control sequences for a solution in some capacity. To this end, code is paired with comments describing it where applicable.

<br /> 

### Usage 

The input is expected to be in the following format, and is translated into ascii mountains as follows:
1. The first number in the sequence of input represents the number of times an escalating mountainside `/` is to be drawn.
2. The next number represents the number of times a de-escaltion of the mountainside `\` is to be drawn from that point.
3. Go to 1. and continue drawing escalations and de-escalations until end of input.
4. Draw an ascii guy sitting at the peak of the highest mountain.

<br />

### Requirements

A terminal with support for ANSI escape sequences or VT100 control sequences is required to properly run this program.

<br />

### Examples

<img src="/images/pyMountains.png" >

<br />

### References

[https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html](https://tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.html)

[https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences](https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)

[https://stackoverflow.com/a/36760881](https://stackoverflow.com/a/36760881)

[https://docs.microsoft.com/en-us/windows/console/setconsolemode](https://docs.microsoft.com/en-us/windows/console/setconsolemode)

[https://tomayko.com/blog/2004/StupidShellTricks](https://tomayko.com/blog/2004/StupidShellTricks)
