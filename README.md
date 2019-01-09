#WHAT IS IT ABOUT ?

Code for simple pokemon name guessing game.

#HOW TO GET IT ?

Download/Clone the repository by clicking onto the " GREEN " button.
              
                               OR

Just run the below given command in your terminal in order to get a copy of the repository on your pc :

git clone https://github.com/tanishqvyas/TEXT-BASED-POKEMON-NAME-GUESSING-GAME.git

#HOW DOES THAT WORK ?

It contains only one file named " guess.py " which you can run in your terminal by simply typing the following command :
(*NOTE : Make sure you have python3 installed on your pc and you current working directory is the one containing the guess.py file)

python3 guess.py

#HOW DO I CHANGE DIRECTORY ?

Just use the cd command in your terminal which stands for change directory.

Example :

cd example_directory

( This changes your current working directory from user to example_directory )

#HOW DO I GET PYTHON3 ?

- FOR WINDOWS :

	Python is not usually included by default on Windows, however we can check if any version exists on the system. Open the command line–a text-only view of your 		computer–via PowerShell which is a built-in program.

	Go to Start Menu and type “PowerShell” to open it.

	Type the following command and hit the Enter/Return key:

#INPUT :	  python --version
#OUTUT :          Python 3.7.0
	If you see output like this, Python is already installed. But most likely it is not. So…let’s install Python.
	
	Installing Python 3
	Go to the downloads section of the official Python website. Download the installer and make sure to click the box on the bottom of the page for the Add Python
	3.7 to PATH option, which will let use use python directly from terminal. Otherwise we’d have to enter our system’s full path and modify our environment
	variables manually. In other words, it’ll be a nightmare. Trust me. Check click the box and you’ll save yourself a world of headache.

	Python Installer

	After Python has installed close PowerShell. Then re-open it and try our command again. You should see the following:

	python --version
	Python 3.7.0

	(*YOUR VERSION MIGHT BE DIFFERENT OR SAME AS THE ONE STATED ABOVE)

- FOR LINUX : 

	To see which version of Python 3 you have installed, open a command prompt and run:

	python3 --version

	If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

	sudo apt-get update
	sudo apt-get install python3.6
	
	If you’re using another version of Ubuntu (e.g. the latest LTS release), we recommend using the deadsnakes PPA to install Python 3.6:
	
	sudo apt-get install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt-get update
	sudo apt-get install python3.6
	
	If you are using other Linux distribution, chances are you already have Python 3 pre-installed as well. If not, use your distribution’s package manager. For 		example on Fedora, you would use dnf:
	
	sudo dnf install python3



#CONTRIBUTING

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


