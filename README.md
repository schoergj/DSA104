# DSA104
Repository for the course DSA104 AI and ML in Chemistry. All course material will be shared here. Additionally, organisational information and lecture slides will be uploaded as well to OLAT, which will also be used for all course-related communication.

## Prerequisites
This course utilises several tools, which have to be installed on your PC (if you have done the DSA103, you are already well set):

1) Git/Github: Make sure you have Git installed and a GitHub account
2) We will use the package manager uv and its virtual environment (https://docs.astral.sh/uv/)
3) IDE: For running code and Jupyter notebooks and for facilitating version control, we will be using an IDE. All demonstration will be done in Visual Studio Code, but other development environments, such as Pycharm, work as well. Whatever IDE you are using, make sure that you keep it and its extensions (e.g. for Jupyter) up to date and that you are familiar with the working environment.

If anything else is going to be required, you will be notified in due course.

## How to work with this repository
The initial steps:
1) Fork the repository using the Fork button on GitHub.
2) Clone your fork.
3) Create a virtual environment, by running ´uv venv´ in the terminal (in the IDE).
4) Activate the virtual environment (e.g. on Windows: ´.venv\Scripts\activate´).
5) Run the command ´uv sync´ to synchronize the environment with the provided lock file. Any missing dependencies will be thereby installed.
6) Select the Python interpreter from the DSA104 environment (in VSC: click in the Search bar, hit Ctrl+P, then type "Python: Select Interpreter" - or use the button in the lower right corner of the window). Likewise you can can set the Interpreter for Jupyter notebooks.

This repository and the environment will be updated many times throughout the course. Make sure to keep both of them up to date by synchronizing the fork via GitHub and running the ´uv sync´ command after starting the environment, respectively.

**Important: In order to avoid merge conflicts, always copy any files you work on (notebooks, scripts, data, etc.) to the user folder provided in each lecture folder, or create a new file under a different name.** This way you can always accept incoming changes, without altering your personal file versions. 

We do recommend to practice the git workflow throughout this course and to commit to your fork after significant changes. **If there are any problems with your IDE, uv, git or your repo, that prevent you from using the environment as intended, please notify us via mail immediately and don't wait until the next Q&A session.** 

## Authors
This repository was created and is maintained by Jasmin Hafner and Johannes Schörgenhumer.

## License
CC BY-NC-SA 4.0 

You are free to share and adapt, as long as attribution to the authors is appropriately given, the material is not used for any commercial purposes and any material built on the content of the DSA104 repository is shared under the same license.

Full license information are found here: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en
