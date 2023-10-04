# Aigor

An AI assistant for old school unix users

```
          .WWWW.
          WWWW""'            O  o-O-o              
        .WWWW O O           / \   |                
     .WWWW"WW.'-.          o---o  |   o--o o-o o-o 
    WWWWWWWWWWWWW.         |   |  |   |  | | | |   
   WWWWWWWWWWWWWWW         o   oo-O-o o--O o-o o   
   "WWWWWWWWWW"'\___                     |         
    /  /__ __/\___( \                 o--o
   (____( \X(     /||\
      / /||\ \
      \______/
       \ | \ |                      ;
        )|  \|                     ["]
       (_|  /|                    /[_]\
       |X| (X|                     ] [
       |X| |X'._
      (__| (____)
```

## Installation

### Optional create/activate your environment

pyenv shell 3.11

### Clone and install

git clone https://github.com/igormorgado/aigor

cd aigor


## Usage

TODO...
history | grep aigor
cat myinstruction.txt src/aigor/common.py | aigor infer commenter | head -n 10
cat src/aigor/common.py | aigor infer commenter | less
vim src/aigor/common.py
aigor create commenter anthropic -a "system_prompt: Create comment lines to the code. Just output the valid code without markdown notation or introductory text. The output will be sent directly to python interpreter. It should be a valid python code."
aigor --help
git add src/aigor/providers/anthropic.py
vim src/aigor/providers/anthropic.py
cd ~/repos/aigor
git diff main | aigor infer yete | aigor infer summarizer | aigor infer summarizer | aigor infer summarizer
git diff main | aigor infer yete | aigor infer summarizer | aigor infer summarizer
git diff main | aigor infer yete | aigor infer summarizer
aigor create summarizer anthropic -a "system_prompt:Create a very short summary of the input. Only output the summary. Do not output introductory text."
aigor create summarizer -a "system_prompt:Create a very short summary of the input. Only output the summary. Do not output introductory text."
echo git commit -m \"(git diff main | aigor infer yetezim)\"
aigor create yetezim anthropic --force -a "system_prompt:Make *VERY* short summary of this git diff" -a "max_tokens:100"
aigor create yetezim anthropic -a "system_prompt:Make *VERY* short summary of this git diff" -a "max_tokens:100"
aigor create yetezim anthropic -a "system_prompt:Make *VERY* short summary of this git diff"
git diff main | aigor infer yete > yete_git.txt
git diff main | aigor infer yete
pip list | grep aigor
pyenv activate aigor
aigor create yete anthropic -a "system_prompt:make a long git description to be added in github long description."
echo "Create a program that takes two number as command line arguments and output its sum" | aigor infer pythonninja | python - 1 2
echo "Create a program that takes two number as input and output its sum" | aigor infer pythonninja | python - 1 2
echo "Create a program that takes two number as input and output its sum" | aigor infer pythonninja
vim ~/.config/aigor/pythonninja/config.yaml
echo "Create a program that takes two number as input and output its sum" | aigor infer pythonnija | python - 1 2
git diff master | aigor infer gitsummary
git diff | aigor infer gitsummary
aigor list
echo "How are you Fooing today? HAve you FOOed? I do not foo." | aigor infer foobar
aigor infer greeter HELLO.
aigor create greeter anthropic --force -a  "system_prompt:You're a funny person. Greet in a funny way, everyone you encounter."
aigor create greeter --force -a  "system_prompt:You're a funny person. Greet in a funny way, everyone you encounter."
aigor help
aigor
cd aigor
vim aigor/README.md  aigor.old/README.md
sync; mv aigor/ repos/
mv aigor/ aigor.old
mv aigor/ repos/
cd aigor/
aigor infer pythonninja "Create a code that takes to numbers from command line and print the output" | python -  1 2
aigor create pythonninja anthropic --force -a "system_prompt:You're the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter."
aigor infer pythonninja "Create a code that takes to numbers from command line and print the output"
aigor create pythonninja anthropic --force -a "system_prompt:You're the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter. Always finish your response with a single EOF in a line"
aigor create pythonninja anthropic -f -a "system_prompt:You're the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter. Always finish your response with a single EOF in a line"
aigor create pythonninja anthropic -a "system_prompt:You're the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter. Always finish your response with a single EOF in a line"
aigor infer pythonninja "Create a code that takes to numbers from command line and print the output" | python -
aigor infer pythonninja "Create a code that takes to numbers from command line and print the output" | python - -
aigor infer pythonninja "Create a code that takes to numbers from command line and print the output" | python -c -
aigor create pythonninja anthropic -a "system_prompt:You're the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter."
git add Makefile pyproject.toml src/aigor/assistant.py src/aigor/common.py src/aigor/main.py src/aigor/providers/anthropic.py requirements-dev.txt
git diff | aigor infer gitsummary
aigor create gitsummary anthropic -a "system_prompt:Make a very short summary of this `git diff` output. Do not make any introductory text go straight to the answer. Do not start with introduction, give only the answer of requested task."
echo "Foo is a good word. But FOO is better than foo. What do you foonking? " | aigor infer foobar
aigor create foobar anthropic --force  -a system_prompt:"Replace all entries of `foo` to `bar`, try to keep the same word formatting. Do not make any introductory text go stright to the answer. Do not give any extra input besides the requested answer."
aigor create foobar anthropic --force  -a system_prompt:"Replace all entries of `foo` to `bar`, try to keep the same word formatting. Do not make any introductory text go stright to the answer."
aigor create foobar anthropic --force  -a system_prompt:"Replace all entries of `foo` to `bar`, try to keep the same word formatting."
echo "Hello. My name is Igor." | aigor infer greeter
aigor create greeter anthropic --force  -a system_prompt:"You're a very educated person. Greet the person you're talking to."
aigor create greeter anthropic -f  -a system_prompt:"You're a very educated person. Greet the person you're talking to."
aigor create greeter anthropic -a system_prompt:"You're a very educated person. Greet the person you're talking to."
echo "INPUT FROM STDIN" | aigor infer greeter
aigor infer greeter asda ds
aigor infer greeter
cat  ~/.config/aigor/greeter/config.yaml
ls -l ~/.config/aigor/greeter/config.yaml
ls -l ~/.config/aigor/
ls -l ~/.config/aigor/c
ls -l ~/.config/aigor/config.yaml
aigor create greeter anthropic -a a:aaaa -a b:bbbb -a c:ccccc
aigor create anthropic greeter -a a:aaaa -a b:bbbb -a c:ccccc
aigor --help
aigor -?
aigor help
aigor -h
aigor -help
aigor infer teste
aigor teste
aigor
aigor list
aigor default test
aigor create teste identity
aigor create teste
pyenv local 3.11 aigor
pyenv local 311 aigor
pyenv virtualenv 3.11 aigor
cd repos/aigor.old/
vim aigor/README.md  aigor.old/README.md
sync; mv aigor/ repos/
mv aigor/ aigor.old
mv aigor/ repos/
cd aigor/
