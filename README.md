[![Test Multiple Python Versions](https://github.com/h-swathi-shenoy/python-devops/actions/workflows/makefile.yml/badge.svg)](https://github.com/h-swathi-shenoy/python-devops/actions/workflows/makefile.yml)
# python-devops
Understand devops for projects. Includes github actions,ci/cd, conatainerization
## Gen Project Scaffold
### Create Dev Environment that is cloud-based
  -  Notebooks, Github Codespaces,AWSCloud9,AWS CloudShell
## Python - Build Project Scaffold
  - [Makefile]: Cookboook for thing for reproducibility(https://github.com/h-swathi-shenoy/python-devops/blob/b35e085d08633458222dc1c79cc3b9b26818d073/Makefile)
  - [requirements.txt] - libs req(https://github.com/h-swathi-shenoy/python-devops/blob/b35e085d08633458222dc1c79cc3b9b26818d073/requirements.txt)
  - [tests_lib.py] :(https://github.com/h-swathi-shenoy/python-devops/blob/b35e085d08633458222dc1c79cc3b9b26818d073/test_devopslib.py)
  - [python_library] :(https://github.com/h-swathi-shenoy/python-devops/tree/b35e085d08633458222dc1c79cc3b9b26818d073/devopslib)
  - Dockerfile
  - Command Line Tool
  - Microservice

1. Create virtual environment - virtualenv ~/.env (Invisible dir, good practise, as we dont need to remember virtual env names, its always .env file)
2. Edit by '~.bashrc'(called while invocation of interpreter) - Add the line in the end(ctrl+g) 'source ~/.env/bin/activate'
(using vim ~/.bashrc)
3. Check for the libs installed : pip freeze | wc -l (needs to be 0 init)
4. Makefile run cmd: make install
## Command Line tools
- Function consists of - input/unitofwork/output
- Use lambda fuctions: Create lambda from scratch (input-trigger, function,output-destn)
- Step functions: Co-ordinate state operations.
- Fire lib to convert any function to a command line
  ![image](https://github.com/h-swathi-shenoy/python-devops/assets/47154548/022ec0f7-438a-49c9-ab60-f043bfd27da7)

## Microservices
## Containerization
