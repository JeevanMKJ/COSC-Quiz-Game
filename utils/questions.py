initial_questions = [
    {
        'question': 'A(n) __________ is a set of instructions that a computer follows to perform a task.',
        'options': ['a. compiler', 'b. program', 'c. interpreter', 'd. programming language'],
        'answer': 'b',
        'answer_name': 'program',
        'module': 1,
        'explanation': 'A program is defined as a set of instructions that a computer follows to perform a specific task. While compilers and interpreters are tools that translate code, and programming languages are used to write code, the actual set of instructions itself is called a program.'
    },
    {
        'question': 'The physical devices that a computer is made of are referred to as __________.',
        'options': ['a. hardware', 'b. software', 'c. the operating system', 'd. tools'],
        'answer': 'a',
        'answer_name': 'hardware',
        'module': 1,
        'explanation': 'Hardware refers to the physical components of a computer system. This includes devices like the motherboard, CPU, RAM, hard drives, and other tangible parts that make up the computer.'
    },
    {
        'question': 'The part of a computer that runs programs is called __________.',
        'options': ['a. RAM', 'b. secondary storage', 'c. main memory', 'd. the CPU'],
        'answer': 'd',
        'answer_name': 'the CPU',
        'module': 1,
        'explanation': 'The Central Processing Unit (CPU) is the brain of the computer that processes and executes instructions from programs. It performs calculations, makes decisions, and controls the operation of other hardware components.'
    },
    {
        'question': 'Today, CPUs are small chips known as __________.',
        'options': ['a. ENIACs', 'b. microprocessors', 'c. memory chips', 'd. operating systems'],
        'answer': 'b',
        'answer_name': 'microprocessors',
        'module': 1,
        'explanation': 'Modern CPUs are built as microprocessors, which are integrated circuits that contain the entire processing unit on a single chip. This technology allows for smaller, more efficient computers compared to early computing machines like ENIAC.'
    },
    {
        'question': 'The computer stores a program while the program is running, as well as the data that the program is working with, in __________.',
        'options': ['a. secondary storage', 'b. the CPU', 'c. main memory', 'd. the microprocessor'],
        'answer': 'c',
        'answer_name': 'main memory',
        'module': 1,
        'explanation': 'Main memory (which includes RAM) is where programs and their data are stored while actively running. This allows the CPU to quickly access the instructions and data it needs to process, as accessing main memory is much faster than accessing secondary storage.'
    },
    {
        'question': 'This is a volatile type of memory that is used only for temporary storage while a program is running.',
        'options': ['a. RAM', 'b. secondary storage', 'c. the disk drive', 'd. the USB drive'],
        'answer': 'a',
        'answer_name': 'RAM',
        'module': 1,
        'explanation': 'Random Access Memory (RAM) is volatile, meaning it loses its contents when power is turned off. It provides temporary storage for programs and data while the computer is running, allowing for quick access by the CPU.'
    },
    {
        'question': 'A type of memory that can hold data for long periods of time, even when there is no power to the computer, is called __________.',
        'options': ['a. RAM', 'b. main memory', 'c. secondary storage', 'd. CPU storage'],
        'answer': 'c',
        'answer_name': 'secondary storage',
        'module': 1,
        'explanation': 'Secondary storage, such as hard drives and SSDs, is non-volatile memory that retains data even when the computer is powered off. It provides long-term storage for programs, files, and other data that needs to be preserved between uses of the computer.'
    },
    {
        'question': 'A component that collects data from people or other devices and sends it to the computer is called __________.',
        'options': ['a. an output device', 'b. an input device', 'c. a secondary storage device', 'd. main memory'],
        'answer': 'b',
        'answer_name': 'an input device',
        'module': 1,
        'explanation': 'Input devices are hardware components that allow users or other systems to send data to a computer. Examples include keyboards, mice, scanners, microphones, and various sensors that collect information from the external environment.'
    },
    {
        'question': 'A video display is a(n) __________ device.',
        'options': ['a. output', 'b. input', 'c. secondary storage', 'd. main memory'],
        'answer': 'a',
        'answer_name': 'output',
        'module': 1,
        'explanation': 'A video display (monitor or screen) is an output device because it presents information from the computer to the user. It displays the results of processing, showing text, images, videos, and other visual data generated by the computer.'
    },
    {
        'question': 'A __________ is enough memory to store a letter of the alphabet or a small number.',
        'options': ['a. byte', 'b. bit', 'c. switch', 'd. transistor'],
        'answer': 'a',
        'answer_name': 'byte',
        'module': 1,
        'explanation': 'A byte is a unit of digital information that typically consists of 8 bits. It can represent a single character, such as a letter, number, or symbol in most encoding schemes like ASCII, making it the basic unit for representing text in computers.'
    },
    {
        'question': 'A byte is made up of eight __________.',
        'options': ['a. CPUs', 'b. instructions', 'c. variables', 'd. bits'],
        'answer': 'd',
        'answer_name': 'bits',
        'module': 1,
        'explanation': 'A byte consists of 8 bits. A bit (binary digit) is the smallest unit of data in computing and can have a value of either 0 or 1. Eight bits grouped together form a byte, which can represent 256 different values (2^8).'
    },
    {
        'question': 'In the __________ numbering system, all numeric values are written as sequences of 0s and 1s.',
        'options': ['a. hexadecimal', 'b. binary', 'c. octal', 'd. decimal'],
        'answer': 'b',
        'answer_name': 'binary',
        'module': 1,
        'module': 1,
        'explanation': 'The binary numbering system uses only two digits: 0 and 1. It is the fundamental language of computers, as electronic components can represent these two states (on/off, high/low voltage). All data in computers is ultimately stored and processed as binary values.'
    },
    {
        'question': 'A bit that is turned off represents the following value: __________.',
        'options': ['a. 1', 'b. −1', 'c. 0', 'd. “no”'],
        'answer': 'c',
        'answer_name': '0',
        'module': 1,
        'explanation': 'In binary representation, a bit that is turned off (or in the "off" state) represents the value 0. Conversely, a bit that is turned on represents the value 1. These two states form the basis of all binary data in computing.'
    },
    {
        'question': 'A set of 128 numeric codes that represent the English letters, various punctuation marks, and other characters is __________.',
        'options': ['a. binary numbering', 'b. ASCII', 'c. Unicode', 'd. ENIAC'],
        'answer': 'b',
        'answer_name': 'ASCII',
        'module': 1,
        'explanation': 'ASCII (American Standard Code for Information Interchange) is a character encoding standard that uses 7 bits to represent 128 different characters, including uppercase and lowercase English letters, numbers, punctuation marks, and control characters. It was one of the first standardized ways to represent text in computers.'
    },
    {
        'question': 'An extensive encoding scheme that can represent characters for many languages in the world is __________.',
        'options': ['a. binary numbering', 'b. ASCII', 'c. Unicode', 'd. ENIAC'],
        'answer': 'c',
        'answer_name': 'Unicode',
        'module': 1,
        'explanation': 'Unicode is an extensive character encoding standard designed to support text in all of the world’s writing systems. Unlike ASCII which only supports 128 characters primarily for English, Unicode can represent characters from virtually all languages worldwide. It uses a codespace of over a million code points to accommodate this vast array of characters, making it the standard for international text representation in modern computing.'
    },
    {
        'question': 'Negative numbers are encoded using the __________ technique.',
        'options': ['a. two’s complement', 'b. floating point', 'c. ASCII', 'd. Unicode'],
        'answer': 'a',
        'answer_name': 'two’s complement',
        'module': 1,
        'explanation': 'Two’s complement is the most common method for representing signed integers (positive, negative, and zero) in computers. This technique works by using the most significant bit as a sign bit, with the remaining bits representing the magnitude. It has the advantage that addition and subtraction work the same way for both positive and negative numbers, simplifying computer arithmetic operations.'
    },
    {
        'question': 'Real numbers are encoded using the __________ technique.',
        'options': ['a. two’s complement', 'b. floating point', 'c. ASCII', 'd. Unicode'],
        'answer': 'b',
        'answer_name': 'floating point',
        'module': 1,
        'explanation': 'Floating point is a technique used to represent real numbers (numbers with decimal points) in computers. It works similarly to scientific notation, with a significand (mantissa) that represents the digits and an exponent that determines the position of the decimal point. This allows computers to represent a wide range of values, from very small to very large numbers, with a fixed number of bits.'
    },
    {
        'question': 'The tiny dots of color that digital images are composed of are called __________.',
        'options': ['a. bits', 'b. bytes', 'c. color packets', 'd. pixels'],
        'answer': 'd',
        'answer_name': 'pixels',
        'module': 1,
        'explanation': 'Pixels (short for "picture elements") are the smallest addressable elements in a digital image or display. Each pixel represents a single point in the image and contains information about its color and brightness. Digital images are composed of grids of these pixels, and the resolution of an image is determined by the number of pixels it contains. Higher pixel counts generally result in more detailed images.'
    },
    {
        'question': 'If you were to look at a machine language program, you would see __________.',
        'options': ['a. Python code', 'b. a stream of binary numbers', 'c. English words', 'd. circuits'],
        'answer': 'b',
        'answer_name': 'a stream of binary numbers',
        'module': 1,
        'explanation': 'Machine language, also known as machine code or native code, is the lowest-level programming language that a computer can directly execute. It consists of binary code - sequences of 0s and 1s that represent specific instructions for the CPU. Unlike high-level languages like Python that use English-like syntax, machine language is not human-readable without specialized tools to interpret it.'
    },
    {
        'question': 'In the __________ part of the fetch-decode-execute cycle, the CPU determines which operation it should perform.',
        'options': ['a. fetch', 'b. decode', 'c. execute', 'd. deconstruct'],
        'answer': 'b',
        'answer_name': 'decode',
        'module': 1,
        'explanation': 'In the fetch-decode-execute cycle (the fundamental operation cycle of a CPU), the decode phase occurs after the CPU fetches an instruction from memory. During decoding, the CPU determines what the instruction means and what components will be required for execution. It interprets the binary instruction code to identify the specific operation to be performed, preparing the system for the execution phase that follows.'
    },
    {
        'question': 'Computers can only execute programs that are written in __________.',
        'options': ['a. Java', 'b. assembly language', 'c. machine language', 'd. Python'],
        'answer': 'c',
        'answer_name': 'machine language',
        'module': 1,
        'explanation': 'Computers can only directly execute programs written in machine language, which consists of binary code (0s and 1s) that the CPU can process. All other programming languages, including Java, Python, and assembly language, must be translated (compiled or interpreted) into machine language before the computer can execute them. This is why compilers, interpreters, and assemblers are essential tools in programming.'
    },
    {
        'question': 'The __________ translates an assembly language program to a machine language program.',
        'options': ['a. assembler', 'b. compiler', 'c. translator', 'd. interpreter'],
        'answer': 'a',
        'answer_name': 'assembler',
        'module': 1,
        'explanation': 'An assembler is a program that translates assembly language code into machine code. Assembly language uses human-readable mnemonics to represent machine instructions, making it easier for programmers to write low-level code. The assembler converts these mnemonics into the binary instructions that the CPU can directly execute, creating a one-to-one correspondence between assembly instructions and machine code operations.'
    },
    {
        'question': 'The words that make up a high-level programming language are called __________.',
        'options': ['a. binary instructions', 'b. mnemonics', 'c. commands', 'd. keywords'],
        'answer': 'd',
        'answer_name': 'keywords',
        'module': 1,
        'explanation': 'Keywords are reserved words that have predefined meanings in a programming language. They form the basic vocabulary of the language and cannot be used as variable names or identifiers. Examples include "if", "while", "for", "class", and "return". These words have specific syntactic purposes and are used to construct the statements and control structures that make up a program.'
    },
    {
        'question': 'The rules that must be followed when writing a program are called __________.',
        'options': ['a. syntax', 'b. punctuation', 'c. keywords', 'd. operators'],
        'answer': 'a',
        'answer_name': 'syntax',
        'module': 1,
        'explanation': 'Syntax refers to the set of rules that define how programs written in a programming language must be structured. These rules specify how keywords, operators, variables, and other elements must be arranged to create valid program statements. If syntax rules are violated, the program will not compile or run correctly. Each programming language has its own specific syntax that programmers must follow.'
    },
    {
        'question': 'A(n) __________ program translates a high-level language program into a separate machine language program.',
        'options': ['a. assembler', 'b. compiler', 'c. translator', 'd. utility'],
        'answer': 'b',
        'answer_name': 'compiler',
        'module': 1,
        'explanation': 'A compiler is a program that translates source code written in a high-level programming language (like C++, Java, or Python) into machine language that a computer can directly execute. Unlike interpreters that translate and execute code line by line, compilers translate the entire program at once, creating a standalone executable file. This process allows compiled programs to run efficiently without requiring the original source code or the compiler itself.'
    },
    {
        'question': 'A __________ error does not prevent the program from running, but causes it to produce incorrect results.',
        'options': ['a. syntax', 'b. hardware', 'c. logic', 'd. fatal'],
        'answer': 'c',
        'answer_name': 'logic',
        'module': 1,
        'explanation': 'A logic error occurs when a program contains a mistake in its algorithm or reasoning, but not in its syntax. Unlike syntax errors that prevent compilation, logic errors allow the program to run but cause it to produce incorrect results. These errors can be difficult to detect because they don’t generate error messages - the program appears to run normally but produces unintended outcomes due to flawed logic in the code.'
    },
    {
        'question': 'A __________ is a single function that the program must perform in order to satisfy the customer.',
        'options': ['a. task', 'b. software requirement', 'c. prerequisite', 'd. predicate'],
        'answer': 'b',
        'answer_name': 'software requirement',
        'module': 1,
        'explanation': 'A software requirement is a specific function or capability that a program must perform to meet customer needs. It defines what the software should do rather than how it should do it. Software requirements form the foundation of software development projects, serving as a contract between developers and customers about what the final product will accomplish.'
    },
    {
        'question': 'A(n) __________ is a set of well-defined logical steps that must be taken to perform a task.',
        'options': ['a. logarithm', 'b. plan of action', 'c. logic schedule', 'd. algorithm'],
        'answer': 'd',
        'answer_name': 'algorithm',
        'module': 1,
        'explanation': 'An algorithm is a precise, step-by-step procedure for solving a problem or accomplishing a task. It consists of a finite sequence of well-defined instructions that, when followed, will produce a specific outcome. Algorithms are fundamental to computer programming as they provide the logical framework that programs implement to process data and produce results.'
    },
    {
        'question': 'An informal language that has no syntax rules and is not meant to be compiled or executed is called __________.',
        'options': ['a. faux code', 'b. pseudocode', 'c. Python', 'd. a flowchart'],
        'answer': 'b',
        'answer_name': 'pseudocode',
        'module': 1,
        'explanation': 'Pseudocode is an informal, human-readable description of a program’s algorithm that uses natural language and simple conventions to outline the logic without adhering to strict syntax rules of any specific programming language. It serves as a planning tool that helps programmers design algorithms before implementing them in actual code, making it easier to focus on the logic rather than syntax details.'
    },
    {
        'question': 'A __________ is a diagram that graphically depicts the steps that take place in a program.',
        'options': ['a. flowchart', 'b. step chart', 'c. code graph', 'd. program graph'],
        'answer': 'a',
        'answer_name': 'flowchart',
        'module': 1,
        'explanation': 'A flowchart is a visual representation of an algorithm or process that uses different shapes connected by arrows to show the sequence of steps. Each shape represents a specific type of action or decision point in the program. Flowcharts help programmers visualize the flow of control in a program and are especially useful for understanding complex logic and decision paths.'
    },
    {
        'question': 'A __________ is a sequence of characters.',
        'options': ['a. char sequence', 'b. character collection', 'c. string', 'd. text block'],
        'answer': 'c',
        'answer_name': 'string',
        'module': 1,
        'explanation': 'A string is a sequence of characters treated as a single unit of data in programming. Strings can contain letters, numbers, symbols, and spaces, and are typically used to store and manipulate text. In most programming languages, including Python, strings are enclosed in quotation marks and can be manipulated using various string-specific operations and methods.'
    },
    {
        'question': 'A __________ is a name that references a value in the computer’s memory.',
        'options': ['a. variable', 'b. register', 'c. RAM slot', 'd. byte'],
        'answer': 'a',
        'answer_name': 'variable',
        'module': 1,
        'explanation': 'A variable is a named storage location in a computer’s memory that holds a value which can be modified during program execution. Variables allow programmers to store, retrieve, and manipulate data by referring to a meaningful name rather than a memory address. They are fundamental to programming as they enable the creation of dynamic, flexible code that can work with different data values.'
    },
    {
        'question': 'A __________ is any hypothetical person using a program and providing input for it.',
        'options': ['a. designer', 'b. user', 'c. guinea pig', 'd. test subject'],
        'answer': 'b',
        'answer_name': 'user',
        'module': 1,
        'explanation': 'A user is any person who interacts with a computer program, providing input and receiving output. In programming contexts, the term often refers to a hypothetical person who will use the software being developed. Understanding user needs, behaviors, and expectations is crucial for creating effective, user-friendly programs that accomplish their intended purposes.'
    },
    {
        'question': 'A string literal in Python must be enclosed in __________.',
        'options': ['a. parentheses', 'b. single-quotes', 'c. double-quotes', 'd. either single-quotes or double-quotes'],
        'answer': 'd',
        'answer_name': 'either single-quotes or double-quotes',
        'module': 1,
        'explanation': 'In Python, string literals can be enclosed in either single quotes ’ or double quotes ’’. This flexibility allows programmers to include quote characters within strings by using the alternative quote style as delimiters. For example, if a string contains single quotes, it can be enclosed in double quotes, and vice versa. Both styles are functionally equivalent, and the choice between them is typically a matter of style preference or practical necessity.'
    },
    {
        'question': 'Short notes placed in different parts of a program explaining how those parts of the program work are called __________.',
        'options': ['a. comments', 'b. reference manuals', 'c. tutorials', 'd. external documentation'],
        'answer': 'a',
        'answer_name': 'comments',
        'module': 1,
        'explanation': 'Comments are explanatory notes added to source code that are ignored by the compiler or interpreter. They serve as documentation within the code itself, helping programmers understand the purpose and functionality of different code sections. Comments are essential for code maintainability, especially when multiple developers work on the same project or when revisiting code after a long period.'
    },
    {
        'question': 'A(n) __________ makes a variable reference a value in the computer’s memory.',
        'options': ['a. variable declaration', 'b. assignment statement', 'c. math expression', 'd. string literal'],
        'answer': 'b',
        'answer_name': 'assignment statement',
        'module': 1,
        'explanation': 'An assignment statement is a programming instruction that stores a value in a variable, creating a reference from the variable name to that value in memory. In Python, assignment uses the equals sign (=) operator, with the variable name on the left and the value to be assigned on the right. This fundamental operation allows programs to store and later retrieve data during execution.'
    },
    {
        'question': 'This symbol marks the beginning of a comment in Python.',
        'options': ['a. &', 'b. *', 'c. **', 'd. #'],
        'answer': 'd',
        'answer_name': '#',
        'module': 1,
        'explanation': 'In Python, the hash symbol (#) marks the beginning of a comment. When the Python interpreter encounters this symbol, it ignores everything from that point to the end of the line. Comments are not executed as part of the program but serve as notes for human readers to understand the code’s purpose, functionality, or implementation details.'
    },
    {
        'question': 'Which of the following statements will cause an error?',
        'options': ['a. x = 17', 'b. 17 = x', 'c. x = 99999', 'd. x = \'17\''],
        'answer': 'b',
        'answer_name': '17 = x',
        'module': 1,
        'explanation': 'The statement "17 = x" will cause a syntax error because in Python, the left side of an assignment statement must be a valid target for assignment (like a variable name), not a literal value. This is because assignment stores a value in a named memory location, and literals like 17 don’t represent memory locations. The other options are all valid Python statements that assign different types of values to the variable x.'
    },
    {
        'question': 'In the expression 12 + 7, the values on the right and left of the + symbol are called __________.',
        'options': ['a. operands', 'b. operators', 'c. arguments', 'd. math expressions'],
        'answer': 'a',
        'answer_name': 'operands',
        'module': 1,
        'explanation': 'In an expression like 12 + 7, the values 12 and 7 are called operands. Operands are the data values that operators act upon. The + symbol is the operator that specifies what action to perform on the operands (in this case, addition). Understanding the relationship between operators and operands is fundamental to constructing and evaluating expressions in programming.'
    },
    {
        'question': 'This operator performs integer division.',
        'options': ['a. //', 'b. %', 'c. **', 'd. /'],
        'answer': 'a',
        'answer_name': '//',
        'module': 1,
        'explanation': 'The // operator in Python performs integer division (also called floor division), which divides the first operand by the second and rounds the result down to the nearest integer. For example, 7 // 2 equals 3, not 3.5. This differs from the regular division operator (/) which returns a floating-point result. Integer division is useful when you need a whole number result and want to discard any fractional part.'
    },
    {
        'question': 'This is an operator that raises a number to a power.',
        'options': ['a. %', 'b. *', 'c. **', 'd. /'],
        'answer': 'c',
        'answer_name': '**',
        'module': 1,
        'explanation': 'The ** operator in Python is the exponentiation operator, which raises a number to a power. For example, 2 ** 3 calculates 2 raised to the power of 3, resulting in 8. This operator provides a concise way to perform power calculations that would otherwise require multiple multiplication operations or the use of specialized math functions.'
    },
    {
        'question': 'This operator performs division, but instead of returning the quotient it returns the remainder.',
        'options': ['a. %', 'b. *', 'c. **', 'd. /'],
        'answer': 'a',
        'answer_name': '%',
        'module': 1,
        'explanation': 'The % operator in Python is the modulo operator, which returns the remainder when the first operand is divided by the second. For example, 7 % 3 equals 1 because when 7 is divided by 3, the quotient is 2 with a remainder of 1. The modulo operator is particularly useful for determining if a number is divisible by another (remainder of 0) and for creating cyclic patterns in programs.'
    },
    {
        'question': 'Suppose the following statement is in a program: price = 99.0. After this statement executes, the price variable will reference a value of which data type?',
        'options': ['a. int', 'b. float', 'c. currency', 'd. str'],
        'answer': 'b',
        'answer_name': 'float',
        'module': 1,
        'explanation': 'After the statement "price = 99.0" executes, the price variable will reference a value of the float data type. In Python, numbers with decimal points are automatically treated as floating-point numbers. The decimal point in 99.0 explicitly indicates that this is a floating-point value, not an integer, even though the fractional part is zero.'
    },
    {
        'question': 'Which built-in function can be used to read input that has been typed on the keyboard?',
        'options': ['a. input()', 'b. get_input()', 'c. read_input()', 'd. keyboard()'],
        'answer': 'a',
        'answer_name': 'input()',
        'module': 1,
        'explanation': 'The input() function in Python is a built-in function that pauses program execution, allows the user to type text at the keyboard, and returns that text as a string when the user presses Enter. This function is essential for creating interactive programs that can receive and process user input during runtime. The other options listed are not standard Python functions for keyboard input.'
    },
    {
        'question': 'Which built-in function can be used to convert an int value to a float?',
        'options': ['a. int_to_float()', 'b. float()', 'c. convert()', 'd. int()'],
        'answer': 'b',
        'answer_name': 'float()',
        'module': 1,
        'explanation': 'The float() function in Python is a built-in function that converts a value (typically an integer or a string representing a number) to a floating-point number. For example, float(42) converts the integer 42 to the floating-point number 42.0. This type conversion function is part of Python’s set of built-in functions for converting between different data types.'
    },
    {
        'question': 'A magic number is ________________.',
        'options': ['a. a number that is mathematically undefined', 'b. an unexplained value that appears in a program’s code', 'c. a number that cannot be divided by 1', 'd. a number that causes computers to crash'],
        'answer': 'b',
        'answer_name': 'an unexplained value that appears in a program’s code',
        'module': 1,
        'explanation': 'A magic number in programming refers to an unexplained numeric value that appears directly in code without context or explanation. For example, using 3.14159 in calculations without clarifying that it represents π. Using magic numbers is considered poor programming practice because they make code harder to understand and maintain. Best practice is to replace magic numbers with named constants that clearly indicate their purpose and meaning.'
    },
    {
        'question': 'A __________ is a name that represents a value that does not change during the program’s execution.',
        'options': ['a. named literal', 'b. named constant', 'c. variable signature', 'd. key term'],
        'answer': 'b',
        'answer_name': 'named constant',
        'module': 1,
        'explanation': 'A named constant is an identifier that represents a fixed value that should not change throughout the program’s execution. Unlike variables that can be reassigned different values, constants maintain the same value from their initialization to the end of the program. Using named constants instead of literal values (like magic numbers) makes code more readable and maintainable, as it gives meaning to values and centralizes them for easier modification.'
    },
    {
        'question': 'A ________ structure can execute a set of statements only under certain circumstances.',
        'options': ['a. sequence', 'b. circumstantial', 'c. decision', 'd. Boolean'],
        'answer': 'c',
        'answer_name': 'decision',
        'module': 1,
        'explanation': 'A decision structure allows a program to execute certain statements conditionally, based on whether a specific condition evaluates to true or false. Unlike sequence structures that execute statements in order without any conditions, decision structures (like if statements) provide branching paths in the program flow, allowing different code to run depending on the evaluation of Boolean expressions.'
    },
    {
        'question': 'A ________ structure provides one alternative path of execution.',
        'options': ['a. sequence', 'b. single alternative decision', 'c. one path alternative', 'd. single execution decision'],
        'answer': 'b',
        'answer_name': 'single alternative decision',
        'module': 1,
        'explanation': 'A single alternative decision structure (implemented with a simple if statement without an else clause) provides just one alternative path of execution. If the condition is true, the program executes a specific block of code; if the condition is false, the program simply skips that block and continues with the next statement after the decision structure. This differs from dual alternative decisions that provide two distinct paths.'
    },
    {
        'question': 'A(n) ________ expression has a value of either True or False.',
        'options': ['a. binary', 'b. decision', 'c. unconditional', 'd. Boolean'],
        'answer': 'd',
        'answer_name': 'Boolean',
        'module': 1,
        'explanation': 'A Boolean expression is an expression that evaluates to either True or False. Named after mathematician George Boole, Boolean expressions are fundamental to programming logic, particularly in decision structures and loops. They can be created using relational operators (like ==, >, <), logical operators (and, or, not), or can be Boolean variables or constants themselves.'
    },
    {
        'question': 'The symbols >, <, and == are all operators.',
        'options': ['a. relational', 'b. logical', 'c. conditional', 'd. ternary'],
        'answer': 'a',
        'answer_name': 'relational',
        'module': 1,
        'explanation': 'The symbols >, <, and == are relational operators that compare two values and produce a Boolean result. They establish relationships between operands: greater than (>), less than (<), and equal to (==). Relational operators are distinct from logical operators (and, or, not) which combine Boolean values, and are essential for creating conditions in decision structures and loops.'
    },
    {
        'question': 'A(n) ________ structure tests a condition and then takes one path if the condition is true, or another path if the condition is false.',
        'options': ['a. if statement', 'b. single alternative decision', 'c. dual alternative decision', 'd. sequence'],
        'answer': 'c',
        'answer_name': 'dual alternative decision',
        'module': 1,
        'explanation': 'A dual alternative decision structure (implemented with an if-else statement) provides exactly two possible execution paths. If the condition evaluates to true, one block of code executes; if the condition is false, a different block executes. This ensures that exactly one of the two code blocks will run, making it useful when a program needs to choose between two mutually exclusive actions.'
    },
    {
        'question': 'You use a(n) ________ statement to write a single alternative decision structure.',
        'options': ['a. test-jump', 'b. if', 'c. if-else', 'd. if-call'],
        'answer': 'b',
        'answer_name': 'if',
        'module': 1,
        'explanation': 'The if statement (without an else clause) is used to implement a single alternative decision structure in programming. It evaluates a condition and executes a block of code only if that condition is true. If the condition is false, the program simply skips the code block and continues with the next statement after the if structure. This is the simplest form of conditional execution in most programming languages.'
    },
    {
        'question': 'You use a(n) ________ statement to write a dual alternative decision structure.',
        'options': ['a. test-jump', 'b. if', 'c. if-else', 'd. if-call'],
        'answer': 'c',
        'answer_name': 'if-else',
        'module': 1,
        'explanation': 'The if-else statement implements a dual alternative decision structure in programming. It evaluates a condition and executes one block of code if the condition is true, or a different block if the condition is false. This ensures that exactly one of the two code blocks will execute, making it appropriate when a program must choose between two mutually exclusive actions based on a condition.'
    },
    {
        'question': 'and, or, and not are ________ operators.',
        'options': ['a. relational', 'b. logical', 'c. conditional', 'd. ternary'],
        'answer': 'b',
        'answer_name': 'logical',
        'module': 1,
        'explanation': 'The keywords and, or, and not are logical operators that combine or modify Boolean expressions. They operate on Boolean values: "and" returns True only if both operands are True; "or" returns True if at least one operand is True; and "not" negates a Boolean value, turning True to False and vice versa. These operators are essential for creating complex conditions in decision structures and loops.'
    },
    {
        'question': 'A compound Boolean expression created with the ________ operator is true only if both of its subexpressions are true.',
        'options': ['a. and', 'b. or', 'c. not', 'd. both'],
        'answer': 'a',
        'answer_name': 'and',
        'module': 1,
        'explanation': 'The "and" logical operator creates a compound Boolean expression that evaluates to True only if both of its subexpressions are True. If either subexpression is False, or both are False, the entire expression evaluates to False. This operator is used when a program needs to verify that multiple conditions are simultaneously satisfied before executing certain code.'
    },
    {
        'question': 'The ________ operator takes a Boolean expression as its operand and reverses its logical value.',
        'options': ['a. and', 'b. or', 'c. not', 'd. either'],
        'answer': 'c',
        'answer_name': 'not',
        'module': 1,
        'explanation': 'The "not" logical operator is a unary operator that takes a single Boolean expression as its operand and reverses its logical value. It transforms True to False and False to True. This operator is useful when a program needs to check for the absence of a condition or when the logic needs to be inverted for clarity or to simplify complex Boolean expressions.'
    },
    {
        'question': 'A ________ is a Boolean variable that signals when some condition exists in the program.',
        'options': ['a. flag', 'b. signal', 'c. sentinel', 'd. siren'],
        'answer': 'a',
        'answer_name': 'flag',
        'module': 1,
        'explanation': 'A flag is a Boolean variable used to indicate whether a specific condition has occurred or exists in a program. Flags are typically initialized to one value (often False) and then set to the opposite value when a particular event happens. They serve as markers or signals that can be checked later in the program to determine if certain actions should be taken, making them valuable for tracking states across different parts of code.'
    },
    {
        'question': 'A __________ -controlled loop uses a true/false condition to control the number of times that it repeats.',
        'options': ['a. Boolean', 'b. condition', 'c. decision', 'd. count'],
        'answer': 'a',
        'answer_name': 'Boolean',
        'module': 1,
        'explanation': 'A Boolean-controlled loop (like a while loop) uses a Boolean expression that evaluates to either True or False to determine whether the loop should continue executing. The loop repeats as long as the condition remains True and terminates when it becomes False. This type of loop is useful when the number of iterations isn’t known in advance and depends on conditions that may change during execution.'
    },
    {
        'question': 'A __________ -controlled loop repeats a specific number of times.',
        'options': ['a. Boolean', 'b. condition', 'c. decision', 'd. count'],
        'answer': 'd',
        'answer_name': 'count',
        'module': 1,
        'explanation': 'A count-controlled loop (like a for loop in many languages) repeats a specific, predetermined number of times. It typically uses a counter variable that is initialized, tested, and updated with each iteration. Count-controlled loops are appropriate when the exact number of iterations is known before the loop begins, such as when processing arrays or lists of known size or performing an action a specific number of times.'
    },
    {
        'question': 'Each repetition of a loop is known as a(n) __________ .',
        'options': ['a. cycle', 'b. revolution', 'c. orbit', 'd. iteration'],
        'answer': 'd',
        'answer_name': 'iteration',
        'module': 1,
        'explanation': 'An iteration refers to a single execution of the statements within a loop. During each iteration, the loop body is executed once before the condition is reevaluated to determine if another iteration should occur. The term comes from the Latin "iterare" meaning "to repeat," and is standard terminology in programming and mathematics for describing repeated processes.'
    },
    {
        'question': 'The while loop is a __________ type of loop.',
        'options': ['a. pretest', 'b. no-test', 'c. prequalified', 'd. post-iterative'],
        'answer': 'a',
        'answer_name': 'pretest',
        'module': 1,
        'explanation': 'The while loop is a pretest loop, meaning it evaluates its condition before executing the loop body. If the condition is initially false, the loop body may never execute. This contrasts with post-test loops (like do-while in many languages) that execute the loop body at least once before testing the condition. Pretest loops are useful when you want to avoid execution entirely under certain conditions.'
    },
    {
        'question': 'A(n) __________ loop has no way of ending and repeats until the program is inter- rupted.',
        'options': ['a. indeterminate', 'b. interminable', 'c. infinite', 'd. timeless'],
        'answer': 'c',
        'answer_name': 'infinite',
        'module': 1,
        'explanation': 'An infinite loop is a loop that has no termination condition or has a condition that never becomes false, causing it to execute indefinitely. Without external intervention (like program termination by the user or system), an infinite loop will continue running forever. While usually a programming error, infinite loops are sometimes intentionally used in systems that must run continuously until explicitly stopped.'
    },
    {
        'question': 'The -= operator is an example of a(n) __________ operator.',
        'options': ['a. relational', 'b. augmented assignment', 'c. complex assignment', 'd. reverse assignment'],
        'answer': 'b',
        'answer_name': 'augmented assignment',
        'module': 1,
        'explanation': 'The -= operator is an augmented assignment operator that combines subtraction with assignment. It subtracts the right operand from the left operand and assigns the result back to the left operand. For example, x -= 5 is equivalent to x = x - 5. Augmented assignment operators (which also include +=, *=, /=, etc.) provide a more concise syntax for updating variables with operations on their current values.'
    },
    {
        'question': 'A(n) __________ variable keeps a running total.',
        'options': ['a. sentinel', 'b. sum', 'c. total', 'd. accumulator'],
        'answer': 'd',
        'answer_name': 'accumulator',
        'module': 1,
        'explanation': 'An accumulator variable is used to keep a running total or sum as a program executes. It is typically initialized to a starting value (often zero) and then updated by adding or combining new values as they are processed. Accumulators are commonly used in loops to calculate sums, averages, or other aggregate values across multiple iterations or data items.'
    },
    {
        'question': 'A(n) __________ is a special value that signals when there are no more items from a list of items to be processed. This value cannot be mistaken as an item from the list.',
        'options': ['a. sentinel', 'b. flag', 'c. signal', 'd. accumulator'],
        'answer': 'a',
        'answer_name': 'sentinel',
        'module': 1,
        'explanation': 'A sentinel is a special value used to signal the end of a data set or to terminate a loop. It must be a value that cannot be confused with legitimate data values. For example, using -1 as a sentinel when processing positive integers, or using an empty string when processing non-empty text. Sentinels are particularly useful in input validation loops and when processing data of unknown length.'
    },
    {
        'question': 'GIGO stands for __________ .',
        'options': ['a. great input, great output', 'b. garbage in, garbage out', 'c. GIGahertz Output',
                    'd. GIGabyte Operation'],
        'answer': 'b',
        'answer_name': 'garbage in, garbage out',
        'module': 1,
        'explanation': 'GIGO stands for "Garbage In, Garbage Out," a concept in computer science emphasizing that the quality of a program’s output depends on the quality of its input. If invalid or nonsensical data is provided to a program, the results will also be invalid or nonsensical, regardless of how well the program is designed. This principle highlights the importance of input validation and data quality in computing.'
    },
    {
        'question': "The integrity of a program's output is only as good as the integrity of the program's ____________ .",
        'options': ['a. compiler', 'b. programming language', 'c. input', 'd. debugger'],
        'answer': 'c',
        'answer_name': 'input',
        'module': 1,
        'explanation': 'The integrity of a program’s output is only as good as the integrity of its input, which is the essence of the GIGO principle. Even the most well-designed and error-free program will produce incorrect results if given invalid or inappropriate input data. This underscores the critical importance of input validation and data quality checks in software development to ensure reliable and accurate program output.'
    },
    {
        'question': 'The input operation that appears just before a validation loop is known as the __________ .',
        'options': ['a. prevalidation read', 'b. primordial read', 'c. initialization read', 'd. priming read'],
        'answer': 'd',
        'answer_name': 'priming read',
        'module': 1,
        'explanation': 'A priming read is the initial input operation that occurs before entering a validation loop. It gets the first value to be tested by the loop’s condition. This pattern is common when validating user input: first, the program reads a value (the priming read), then it enters a loop that validates the input and, if invalid, prompts for and reads new values until valid input is received. The priming read is essential for the loop’s first condition test.'
    },
    {
        'question': 'Validation loops are also known as __________ .',
        'options': ['a. error traps', 'b. doomsday loops', 'c. error avoidance loops', 'd. defensive loops'],
        'answer': 'a',
        'answer_name': 'error traps',
        'module': 1,
        'explanation': 'Validation loops are also known as error traps or error handlers. These loops are designed to verify that user input meets specific criteria before the program proceeds with processing that input. If invalid data is detected, the loop continues to prompt the user until valid input is received, effectively "trapping" errors before they can cause problems in the program.'
    },
    {
        'question': 'A group of statements that exist within a program for the purpose of performing a specific task is a(n) _______ .',
        'options': ['a. block', 'b. parameter', 'c. function', 'd. expression'],
        'answer': 'c',
        'answer_name': 'function',
        'module': 2,
        'explanation': 'A function is a group of statements that exists within a program for the purpose of performing a specific task. Functions allow programmers to organize code into logical, reusable units that can be called whenever their specific functionality is needed. This modular approach makes programs easier to understand, maintain, and debug.'
    },
    {
        'question': 'A design technique that helps to reduce the duplication of code within a program and is a benefit of using functions is ________ .',
        'options': ['a. code reuse', 'b. divide and conquer', 'c. debugging', 'd. facilitation of teamwork'],
        'answer': 'a',
        'answer_name': 'code reuse',
        'module': 2,
        'explanation': 'Code reuse is a design technique that helps reduce duplication by allowing programmers to write a piece of code once and use it multiple times throughout a program. This is a major benefit of using functions, as they enable developers to encapsulate functionality that can be called whenever needed rather than rewriting the same code in multiple places, which saves time, reduces errors, and makes maintenance easier.'
    },
    {
        'question': 'The first line of a function definition is known as the   .',
        'options': ['a. body', 'b. introduction', 'c. initialization', 'd. header'],
        'answer': 'd',
        'answer_name': 'header',
        'module': 2,
        'explanation': 'The first line of a function definition is known as the header. In Python, the function header begins with the keyword "def", followed by the function name, parentheses containing any parameters, and ends with a colon. The header establishes the function’s name, specifies what data it will receive through parameters, and marks the beginning of the function definition.'
    },
    {
        'question': 'You ________ a function to execute it.',
        'options': ['a. define', 'b. call', 'c. import', 'd. export'],
        'answer': 'b',
        'answer_name': 'call',
        'module': 2,
        'explanation': 'You call a function to execute it. Calling a function means invoking or executing the code contained within that function. In Python, this is done by writing the function name followed by parentheses containing any arguments that need to be passed to the function. When a function is called, program execution jumps to the function, executes its statements, and then returns to the point immediately after the function call.'
    },
    {
        'question': 'A design technique that programmers use to break down an algorithm into functions is known as ________ .',
        'options': ['a. top-down design', 'b. code simplification', 'c. code refactoring', 'd. hierarchical subtasking'],
        'answer': 'a',
        'answer_name': 'top-down design',
        'module': 2,
        'explanation': 'Top-down design (also known as stepwise refinement or divide and conquer) is a design technique where programmers start with a high-level view of a problem and progressively break it down into smaller, more manageable functions or modules. This approach allows complex problems to be solved by dividing them into simpler subtasks, making the overall solution easier to understand, implement, and maintain.'
    },
    {
        'question': 'A ________ is a diagram that gives a visual representation of the relationships between functions in a program.',
        'options': ['a. flowchart', 'b. function relationship chart', 'c. symbol chart', 'd. hierarchy chart'],
        'answer': 'd',
        'answer_name': 'hierarchy chart',
        'module': 2,
        'explanation': 'A hierarchy chart (also known as a structured chart) provides a visual representation of the relationships between functions in a program. Unlike flowcharts that show the sequence of operations, hierarchy charts display the organizational structure of functions, showing which functions call other functions. This helps programmers understand the program’s overall structure and the dependencies between different modules.'
    },
    {
        'question': 'The ________ keyword is ignored by the Python interpreter and can be used as a placeholder for code that will be written later.',
        'options': ['a. placeholder', 'b. pass', 'c. pause', 'd. skip'],
        'answer': 'b',
        'answer_name': 'pass',
        'module': 2,
        'explanation': 'The pass keyword in Python is a null operation that is ignored by the interpreter. It serves as a placeholder in situations where syntax requires a statement but no action is needed. This is particularly useful during development when you want to define a function or class structure but haven’t yet implemented the details, allowing the code to run without errors while you work on other parts.'
    },
    {
        'question': 'A ________ is a variable that is created inside a function.',
        'options': ['a. global variable', 'b. local variable', 'c. hidden variable', 'd. none of the above; you cannot create a variable inside a function'],
        'answer': 'b',
        'answer_name': 'local variable',
        'module': 2,
        'explanation': 'A local variable is a variable that is created inside a function and can only be accessed within that function. Local variables are not visible to code outside the function, including other functions. They exist only during the function’s execution and are destroyed when the function completes, making them useful for temporary storage without affecting the rest of the program.'
    },
    {
        'question': 'A(n) ________ is the part of a program in which a variable may be accessed.',
        'options': ['a. declaration space', 'b. area of visibility', 'c. scope', 'd. mode'],
        'answer': 'c',
        'answer_name': 'scope',
        'module': 2,
        'explanation': 'Scope refers to the part of a program in which a variable may be accessed. The scope of a variable determines its visibility and lifetime within a program. Local variables have function scope and are only accessible within the function where they are defined, while global variables have file scope and can be accessed throughout the entire program file.'
    },
    {
        'question': 'A(n) ________ is a piece of data that is sent into a function.',
        'options': ['a. argument', 'b. parameter', 'c. header', 'd. packet'],
        'answer': 'a',
        'answer_name': 'argument',
        'module': 2,
        'explanation': 'An argument is a piece of data that is sent into a function when the function is called. Arguments provide the function with the specific values it needs to perform its task. When a function is called, the arguments are placed inside the parentheses following the function name, and these values are then passed to the corresponding parameters defined in the function header.'
    },
    {
        'question': 'A(n) ________ is a special variable that receives a piece of data when a function is called.',
        'options': ['a. argument', 'b. parameter', 'c. header', 'd. packet'],
        'answer': 'b',
        'answer_name': 'parameter',
        'module': 2,
        'explanation': 'A parameter is a special variable listed in a function’s definition that receives data when the function is called. Parameters act as placeholders for the arguments that will be passed to the function. When the function executes, each parameter is assigned the value of its corresponding argument, allowing the function to work with the data provided by the caller.'
    },
    {
        'question': 'A variable that is visible to every function in a program file is a ________ .',
        'options': ['a. local variable', 'b. universal variable', 'c. program-wide variable', 'd. global variable'],
        'answer': 'd',
        'answer_name': 'global variable',
        'module': 2,
        'explanation': 'A global variable is a variable that is visible to every function in a program file. Global variables are defined outside of any function and can be accessed and modified by any function in the same file. This provides a way for different functions to share data, though excessive use of global variables is generally discouraged as it can make programs harder to understand and maintain.'
    },
    {
        'question': 'When possible, you should avoid using ________ variables in a program.',
        'options': ['a. local', 'b. global', 'c. reference', 'd. parameter'],
        'answer': 'b',
        'answer_name': 'global',
        'module': 2,
        'explanation': 'When possible, you should avoid using global variables in a program. While global variables provide a way to share data between functions, they can make programs harder to debug and maintain because any function can modify them, potentially leading to unexpected behavior. Instead, it’s generally better to pass data between functions using parameters and return values, which makes the data flow more explicit and controlled.'
    },
    {
        'question': 'This is a prewritten function that is built into a programming language.',
        'options': ['a. standard function', 'b. library function', 'c. custom function', 'd. cafeteria function'],
        'answer': 'b',
        'answer_name': 'library function',
        'module': 2,
        'explanation': 'A library function is a prewritten function that is built into a programming language or provided through its standard libraries. These functions are ready to use without requiring the programmer to write them from scratch, saving time and effort. Examples in Python include functions like print(), len(), and those in modules like math, random, and datetime, which provide commonly needed functionality.'
    },
    {
        'question': 'This standard library function returns a random integer within a specified range of values.',
        'options': ['a. random', 'b. randint', 'c. random_integer', 'd. uniform'],
        'answer': 'b',
        'answer_name': 'randint',
        'module': 2,
        'explanation': 'The randint() function from Python’s random module returns a random integer within a specified range of values. It takes two parameters representing the lower and upper bounds of the range (inclusive) and returns a randomly selected integer from that range. For example, random.randint(1, 10) would return a random integer between 1 and 10, including both 1 and 10.'
    },
    {
        'question': 'This standard library function returns a random floating-point number in the range of 0.0 up to 1.0 (but not including 1.0).',
        'options': ['a. random', 'b. randint', 'c. random_integer', 'd. uniform'],
        'answer': 'a',
        'answer_name': 'random',
        'module': 2,
        'explanation': 'The random() function from Python’s random module returns a random floating-point number in the range of 0.0 up to but not including 1.0. This function takes no parameters and generates a pseudo-random value that can be used for various purposes, such as simulations, games, or generating random test data. The result is always greater than or equal to 0.0 and less than 1.0.'
    },
    {
        'question': 'This standard library function returns a random floating-point number within a specified range of values.',
        'options': ['a. random', 'b. randint', 'c. random_integer', 'd. uniform'],
        'answer': 'd',
        'answer_name': 'uniform',
        'module': 2,
        'explanation': 'The uniform() function from Python’s random module returns a random floating-point number within a specified range of values. It takes two parameters representing the lower and upper bounds of the range and returns a randomly selected floating-point number from that range. Unlike random(), which only generates values between 0.0 and 1.0, uniform() allows you to specify any range of floating-point values.'
    },
    {
        'question': 'This statement causes a function to end and sends a value back to the part of the program that called the function.',
        'options': ['a. end', 'b. send', 'c. exit', 'd. return'],
        'answer': 'd',
        'answer_name': 'return',
        'module': 2,
        'explanation': 'The return statement causes a function to end its execution and sends a value back to the part of the program that called the function. When a return statement is encountered, the function immediately stops executing, and control is passed back to the caller along with any value specified after the return keyword. If no value is specified, the function returns None by default.'
    },
    {
        'question': 'This is a design tool that describes the input, processing, and output of a function.',
        'options': ['a. hierarchy chart', 'b. IPO chart', 'c. datagram chart', 'd. data processing chart'],
        'answer': 'b',
        'answer_name': 'IPO chart',
        'module': 2,
        'explanation': 'An IPO (Input-Processing-Output) chart is a design tool that describes the input, processing, and output of a function. This chart helps programmers plan and document what data a function will receive, what operations it will perform on that data, and what results it will produce. IPO charts are useful during the design phase of programming as they provide a clear overview of a function’s purpose and behavior.'
    },
    {
        'question': 'This type of function returns either True or False.',
        'options': ['a. Binary', 'b. true_false', 'c. Boolean', 'd. logical'],
        'answer': 'c',
        'answer_name': 'Boolean',
        'module': 2,
        'explanation': 'A Boolean function is a type of function that returns either True or False. These functions are commonly used to test conditions or verify if certain criteria are met. Boolean functions are particularly useful in decision structures (if statements) and loops, where the program needs to determine whether to execute certain code based on a condition. They help make code more readable by encapsulating complex conditions into descriptively named functions.'
    },
    {
        'question': 'This is a math module function.',
        'options': ['a. derivative', 'b. factor', 'c. sqrt', 'd. differentiate'],
        'answer': 'c',
        'answer_name': 'sqrt',
        'module': 2,
        'explanation': 'The sqrt() function is part of Python’s math module and is used to calculate the square root of a number. It takes a single numeric argument and returns the square root of that number as a floating-point value. To use this function, you must first import the math module with "import math" and then call the function as math.sqrt(x), where x is the number for which you want to find the square root.'
    },
    {
        'question': 'A file that data is written to is known as a(n) ________ .',
        'options': ['a. input file', 'b. output file', 'c. sequential access file', 'd. binary file'],
        'answer': 'b',
        'answer_name': 'output file',
        'module': 2,
        'explanation': 'An output file is a file that a program writes data to. When a program needs to save information for later use or to be accessed by other programs, it writes this data to an output file. In programming, output files are typically opened in write mode ("w") or append mode ("a"), allowing the program to create new content or add to existing content in the file.'
    },
    {
        'question': 'A file that data is read from is known as a(n) ________ .',
        'options': ['a. input file', 'b. output file', 'c. sequential access file', 'd. binary file'],
        'answer': 'a',
        'answer_name': 'input file',
        'module': 2,
        'explanation': 'An input file is a file from which a program reads data. When a program needs to process existing information stored in a file, it opens the file as an input file. In programming, input files are typically opened in read mode ("r"), which allows the program to access the file’s contents but prevents any modifications to the file.'
    },
    {
        'question': 'Before a file can be used by a program, it must be ________ .',
        'options': ['a. formatted', 'b. encrypted', 'c. closed', 'd. opened'],
        'answer': 'd',
        'answer_name': 'opened',
        'module': 2,
        'explanation': 'Before a file can be used by a program, it must be opened. Opening a file establishes a connection between the program and the file, creating a file object that the program can use to read from or write to the file. This process includes specifying the file name and the mode (read, write, or append) in which the file will be accessed.'
    },
    {
        'question': 'When a program is finished using a file, it should do this.',
        'options': ['a. erase the file', 'b. open the file', 'c. close the file', 'd. encrypt the file'],
        'answer': 'c',
        'answer_name': 'close the file',
        'module': 2,
        'explanation': 'When a program is finished using a file, it should close the file. Closing a file releases the resources associated with it, ensures that any buffered data is written to the file, and breaks the connection between the program and the file. Properly closing files is important for data integrity and efficient resource management in the operating system.'
    },
        {
        'question': 'The contents of this type of file can be viewed in an editor such as Notepad.',
        'options': ['a. text file', 'b. binary file', 'c. English file', 'd. human-readable file'],
        'answer': 'a',
        'answer_name': 'text file',
        'module': 2,
        'explanation': 'A text file contains data that has been encoded as text, typically using ASCII or Unicode character sets. The contents of text files can be viewed and edited in simple text editors like Notepad because they contain human-readable characters. Text files are commonly used for storing configuration information, source code, logs, and other data that needs to be easily read or modified by humans.'
    },
    {
        'question': 'This type of file contains data that has not been converted to text.',
        'options': ['a. text file', 'b. binary file', 'c. Unicode file', 'd. symbolic file'],
        'answer': 'b',
        'answer_name': 'binary file',
        'module': 2,
        'explanation': 'A binary file contains data that has not been converted to text format. Instead, binary files store information in the same format that the computer uses internally to represent the data, which is often more compact and efficient. Examples include executable programs, images, videos, and database files. Unlike text files, binary files cannot be meaningfully viewed or edited with standard text editors.'
    },
    {
        'question': 'When working with this type of file, you access its data from the beginning of the file to the end of the file.',
        'options': ['a. ordered access', 'b. binary access', 'c. direct access', 'd. sequential access'],
        'answer': 'd',
        'answer_name': 'sequential access',
        'module': 2,
        'explanation': 'Sequential access is a file access method where data is read or written in order, from the beginning of the file to the end. To access a particular piece of data, all preceding data must be read first. This is similar to how a cassette tape works - you must fast-forward through earlier content to reach later content. Sequential access is simple to implement and is efficient for operations that process all data in a file.'
    },
    {
        'question': 'When working with this type of file, you can jump directly to any piece of data in the file without reading the data that comes before it.',
        'options': ['a. ordered access', 'b. binary access', 'c. direct access', 'd. sequential access'],
        'answer': 'c',
        'answer_name': 'direct access',
        'module': 2,
        'explanation': 'Direct access (also known as random access) allows a program to jump directly to any location in a file without reading through all preceding data. This is similar to how you can skip directly to any track on a CD or any chapter in a digital video. Direct access is particularly useful for database applications and other programs that need to quickly retrieve specific pieces of information from large files.'
    },
    {
        'question': 'This is a small "holding section" in memory that many systems write data to before writing the data to a file.',
        'options': ['a. buffer', 'b. variable', 'c. virtual file', 'd. temporary file'],
        'answer': 'a',
        'answer_name': 'buffer',
        'module': 2,
        'explanation': 'A buffer is a temporary storage area in memory that holds data before it is processed or transferred. When writing to files, data is often first collected in a buffer and then written to the file in larger chunks, which is more efficient than writing each small piece of data individually. Buffers help optimize performance by reducing the number of actual I/O operations needed to work with files.'
    },
    {
        'question': 'This marks the location of the next item that will be read from a file.',
        'options': ['a. input position', 'b. delimiter', 'c. pointer', 'd. read position'],
        'answer': 'd',
        'answer_name': 'read position',
        'module': 2,
        'explanation': 'The read position (also called the file position or file pointer) marks the location in a file where the next read operation will occur. As data is read from a file, this position automatically advances. Programs can also manually change the read position using operations like seek() to jump to specific locations in the file, which is particularly useful in direct access file operations.'
    },
    {
        'question': 'When a file is opened in this mode, data will be written at the end of the file\'s existing contents.',
        'options': ['a. output mode', 'b. append mode', 'c. backup mode', 'd. read-only mode'],
        'answer': 'b',
        'answer_name': 'append mode',
        'module': 2,
        'explanation': 'Append mode is a file access mode that positions the file pointer at the end of the file before each write operation. This ensures that new data is added to the end of the file’s existing contents rather than overwriting them. In Python, append mode is specified with the "a" mode character when opening a file. This mode is useful for adding information to logs, transaction records, or any file that needs to accumulate data over time.'
    },
    {
        'question': 'This is a single piece of data within a record.',
        'options': ['a. field', 'b. variable', 'c. delimiter', 'd. subrecord'],
        'answer': 'a',
        'answer_name': 'field',
        'module': 2,
        'explanation': 'A field is a single piece of data within a record. In structured data storage, records typically contain multiple related fields that together represent a complete unit of information. For example, in a customer record, fields might include name, address, phone number, and email address. Fields are fundamental to database design and are also important when working with CSV files, fixed-width files, and other structured data formats.'
    },
    {
        'question': 'When an exception is generated, it is said to have been ________ .',
        'options': ['a. built', 'b. raised', 'c. caught', 'd. killed'],
        'answer': 'b',
        'answer_name': 'raised',
        'module': 2,
        'explanation': 'When an exception is generated in a program, it is said to have been "raised." This terminology reflects how the exception interrupts the normal flow of program execution and "raises" the issue to a higher level of attention. In Python, exceptions can be raised automatically by the interpreter when it encounters errors, or explicitly by the programmer using the "raise" statement to signal exceptional conditions.'
    },
    {
        'question': 'This is a section of code that gracefully responds to exceptions.',
        'options': ['a. exception generator', 'b. exception manipulator', 'c. exception handler', 'd. exception monitor'],
        'answer': 'c',
        'answer_name': 'exception handler',
        'module': 2,
        'explanation': 'An exception handler is a section of code specifically designed to respond to exceptions in a controlled manner. Instead of allowing exceptions to crash a program, handlers catch them and execute alternative code paths. Exception handlers allow programs to gracefully manage error conditions, provide meaningful feedback to users, perform cleanup operations, and potentially recover from errors to continue execution.'
    },
    {
        'question': 'You write this statement to respond to exceptions.',
        'options': ['a. run/handle', 'b. try/except', 'c. try/handle', 'd. attempt/except'],
        'answer': 'b',
        'answer_name': 'try/except',
        'module': 2,
        'explanation': 'The try/except statement is used in Python to handle exceptions. Code that might raise an exception is placed in the "try" block, and the code that handles potential exceptions is placed in the "except" block. If an exception occurs in the try block, program execution immediately jumps to the corresponding except block, allowing the program to respond appropriately rather than crashing. This structure is fundamental to robust error handling in Python programs.'
    }
]