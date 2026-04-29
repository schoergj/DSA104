Session 18 contains a separate uv project - for getting the Opentrons package to run without interfering with the other environment (Opentrons package needs quite an old numpy version).

Here are the necessary steps how to set it up:

1) Navigating to the session18 folder by typing in the terminal: `cd .\lectures\session18`
2) Create a new environment here by running (in the session18 folder!) `uv venv`
3) Activate the new environment by running the standard activation command (e.g. for Windows users: ``.\.venv\Script\activate``)
4) A popup may appear asking whether you want to set this environment for the root folder / working directory. I would recommend not doing so.
5) Run `uv sync --active` to install the Opentrons package in your session18 environment.

Afterwards you can use the simulation tool by running:
`opentrons_simulate.exe path\protocol_name.py`.