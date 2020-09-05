
# Linux-101-Challenge

## Guidelines
1. You need to submit the solutions in a pdf file. For each solution mention the the command used and screenshots of the execution.

2. Submit us the pdfs on whatsapp (either number): +91 6355344038, +91 6354481596

4. Mention your full name and admission number in the pdf. Name the pdf as: `<admission number>-solution.pdf` example: `u19cs001-solution.pdf`

3. Deadline for submission is Monday, 7th September 2020, 12pm.

4. This competition is only for 2nd year students of SVNIT and IIIT Surat. Rest can solve but their submissions won't be counted.

5. Submitting early won't fetch you extra points. But amongst the people who have the same marks, ranks will be decided according the their submission time on the final leaderboard.

6. People with top submissions will get included in the ACM NIT Surat's github team.

7. For the vim section, the answers will be evaluated on the basis of number of keystrokes used.

8. Number in brackets after each problem statement specify the maximum points for solving that problem.

## CLI: 60 Points
For all the questions, assume that your are starting from the question directory `q-xx`.

1. Copy all the files from `cli/q-01/from` to `cli/q-01/to`. (2)

2. So, `sudo` is used to run commands in super user mode. Figure out a way to use `please` instead of `sudo`. So, if `$ sudo xyz` works, `$ please xyz` should works as well. (5)

3. `cli/q-03` has a lot of files written in UTF-8. Write all the file names which contain the string "acm". (5)

4. `cli/q-04/main.cpp` contains a simple hello world program. Compile it to a binary called `hello-world`. Now to run this from say `cli` directory, I need to specify the whole path: `$ ./q-04/hello-world`. Figure out a way to run it from any location by entering just `$ hello-world` in the command line. (10)

5. `cli/q-05` contains some old blurry images. Add prefix of `old-` to all the image files. You cannot use the `rename` command. (10)

6. `cli/q-06/script.py` contains the script we used to generate random files for question 3. Execute this script without using the `python` command. (5)

7. `cli/q-07` contains `file.c`. Delete all the lines that contains the word "struct". (5)

8. `cli/q-08` contains a lot of c++, java and javascript files. Calculate the number of lines of code of each of the 3 languages. (10)

9. `cli/q-09` contains a linked list implementation written in java. Unfortunately, the code is in the reverse order. Fix it! (8)

## VIM: 40 Points

1. Given the name and number of fruits available. Your task is to sort the file so that the fruit having maximum number is first. (10)

Input file ( go to [vim/fruits.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/fruits.txt) )

		oranges      5
		apples       7
		blueberries  15
		bananas      4
		ananas       6

Output file( go to [vim/fruitsOutput.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/fruitsOutput.txt)) 

		
		blueberries  15
		apples       7
		ananas       6
		oranges      5
		bananas      4

2. Your task is to prepend * in front of the given lines using vim. The answer will be evaluated on the basis of keystrokes used. If less keystrokes are used, you will get better score. (10)

Input File:(go to [vim/prepend.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/prepend.txt))

	This is a
	very short

	file, but it is
	still
	full

	of

	surpises.

Output.txt: ( go to [vim/prependOutput.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/prependOutput.txt))

	*This is a
	*very short

	*file, but it is
	*still
	*full

	*of

	*surpises.

3. Look out for [figlet command](https://linux.die.net/man/6/figlet). Install it on your terminal. Now using figlet, convert Input file to Output file without going out from vim. (10)

Input.txt ( go to [vim/figlet.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/figlet.txt))

	Hello World

Output.txt:( go to [vim/figletOutput.txt](https://github.com/acm-svnit/linux-101-challenge/blob/master/vim/figletOutput.txt))

		 _   _      _ _        __        __         _     _ 
		| | | | ___| | | ___   \ \      / /__  _ __| | __| |
		| |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |
		|  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |
		|_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_|
		

**Bonus Questions:** Solve `q-07` and `q-09` from the cli section using just vim (5 + 5)

## RESOURCES

* Type vimtutor on your terminal and complete the basic vim tutorial.
* [Missing semester vim tutorial](https://missing.csail.mit.edu/2020/editors/)
* [Vim golf](http://www.vimgolf.com/)
* [Vim adventures](https://vim-adventures.com/)(it is free upto level 3).
* [Shell Crash Course](https://dev.to/godcrampy/the-missing-shell-scripting-crash-course-37mk)
