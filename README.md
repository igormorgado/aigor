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

```
pyenv install 3.11
pyenv shell 3.11
```

### Install

```
pip install aigor
```


### Or install from sources

```
git clone https://github.com/igormorgado/aigor
cd aigor
pip install .
```


## Usage


### Get help

aigor --help


### Create someone to greet

aigor create JohnCleese anthropic -a  "system_prompt:You're a funny person like Jonh Cleese. Greet in a funny way, everyone you encounter."

aigor call JohnCleese "Hello."

### Create a not so useful (or not) sed replacer...

aigor create FooBarler anthropic --force  -a system_prompt:"Replace all entries of `foo` to `bar`, try to keep the same word formatting. Do not make any introductory text go stright to the answer. Do not give any extra input besides the requested answer."

echo "Foo is a good word. But FOO is better than foo. What do you foonking? " | aigor call FooBarler


### Create a sys admin

aigor create Moss anthropic -a "You're the most experient linux system administrator. Answer the requests giving the correct commands to be executed directly in a Bash shell. Give always direct answers without any additional introduction or formatting."


### Create a python coder

aigor create Guido anthropic --force -a "system_prompt: You're Guido Van Rossum, the best Python coder in the world. You talk only in Python code. Write the best possible program requested. Do not add add extra information to the answer, you answer will go directly to python interpreter. Do not output markdown, just python code."

aigor call Guido "Create a code that takes to numbers from command line and print the output" | python -  1 2

echo "Create a python code using pywikipedia, that reads the name of a wikipedia
page from command line argument and output the it's text content" | aigor call Guido > wikitext.py

aigor call Moss "What is the command to install pywikipedia python package?"


### Creater a text summarizer 

cat > summarizer_sys_prompt.txt << EOF
Create a very short summary of the input. Only output the summary. Do not output introductory text.
EOF

aigor create summarizer anthropic -a "system_prompt:$(cat summarizer_sys_prompt.txt)"


### Code explainer

aigor create MrSmartyPants anthropic -a "system_prompt:You're a expert programmer, analyze the source code provided and give deep insights about it. Follow all additional instructions."


### Create a code commenter

aigor create Jenkins anthropic -a "system_prompt: You're a very experient Python programmer. Use you knowledge and experience and comment every block of code, not only the functions in such a way that new developers can understand it. Do not change anything else, keep all original comments and docstrings. Just output the valid code without introductory text."


### Create a tool for git commits.

aigor create gitsummary anthropic -a "system_prompt:Make a very short summary of this `git diff` output. Do not make any introductory text go straight to the answer. Do not start with introduction, give only the answer of requested task."

git diff main | aigor call gitsummary
git diff main | aigor call gitsummary | aigor call summarizer 
git diff main | aigor call gitsummary | aigor call summarizer | aigor call summarizer 


### Adding multiple files to Jenkins commenter

echo "Before anything say HOWDY HO!" > firstinstructions.txt
cat firstinstructions.txt src/aigor/common.py | aigor call Jenkins | head -n 10


## Creating providers

TODO...



git diff main | aigor call yete | aigor call summarizer
aigor create summarizer -a "system_prompt:Create a very short summary of the input. Only output the summary. Do not output introductory text."
echo git commit -m \"(git diff main | aigor call yetezim)\"
aigor create yetezim anthropic -a "system_prompt:Make *VERY* short summary of this git diff" -a "max_tokens:100"
aigor create yetezim anthropic -a "system_prompt:Make *VERY* short summary of this git diff"
git diff main | aigor call yete > yete_git.txt
git diff main | aigor call yete
pip list | grep aigor
pyenv activate aigor
aigor create yete anthropic -a "system_prompt:make a long git description to be added in github long description."
echo "Create a program that takes two number as command line arguments and output its sum" | aigor call pythonninja | python - 1 2
echo "Create a program that takes two number as input and output its sum" | aigor call pythonninja | python - 1 2
echo "Create a program that takes two number as input and output its sum" | aigor call pythonninja
echo "Create a program that takes two number as input and output its sum" | aigor call pythonnija | python - 1 2
git diff master | aigor call gitsummary
git diff | aigor call gitsummary
aigor list
git diff | aigor call gitsummary
