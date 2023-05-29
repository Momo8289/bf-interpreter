# bf-interpreter
An interpreter for the [Brainf*ck](https://en.wikipedia.org/wiki/Brainfuck) programming language, which is an esolang created by Urban Müller. The included program is a simple "Hello World" program, which I got from [the esolangs wiki](https://esolangs.org/wiki/Brainfuck). 

### How to use
The bf program will be read from `program.bf`. Input will be taken either from stdin or from the `input` file, depending on whether you use `main.py` or `file_input.py`. Output will be printed to stdout. 

### Implementation details:
- Any characters that aren't `><+-.,[]` are ignored
- The cell array is implemented as a dictionary, so it can be pretty much as big as your memory allows. 
- Cell values can be from 0 to 255, and will overflow.
