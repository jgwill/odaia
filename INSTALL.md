# Installation




----
Original Forked INSTALL (wont apply to this project)
----

## Compiled versions (Linux, Windows 10 and 11)

You can download compiled versions for `Linux` and `Windows` (10/11). 

Download the `.msi` or `tar.gz` for the appropriate OS from the download page at https://pygpt.net and then extract files from the archive and run the application.

## Snap Store

You can install **PyGPT** directly from Snap Store:

```commandline
sudo snap install pygpt
```

To manage future updates just use:

```commandline
sudo snap refresh pygpt
```

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/pygpt)

**Using camera:** to use camera in Snap version you must connect the camera with:

```commandline
sudo snap connect pygpt:camera
```

**Using microphone:** to use microphone in Snap version you must connect the microphone with:

```commandline
sudo snap connect pygpt:audio-record :audio-record
```

## PyPi (pip)

The application can also be installed from `PyPI` using `pip install`:

1. Create virtual environment:

```commandline
python3 -m venv venv
source venv/bin/activate
```

2. Install from PyPi:

``` commandline
pip install pygpt-net
```

3. Once installed run the command to start the application:

``` commandline
pygpt
```

## Source Code

An alternative method is to download the source code from `GitHub` and execute the application using 
the Python interpreter (version `3.10` or higher). 

### Running from GitHub source code

1. Clone git repository or download .zip file:

```commandline
git clone https://github.com/szczyglis-dev/py-gpt.git
cd py-gpt
```

2. Create virtual environment:

```commandline
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements:

```commandline
pip install -r requirements.txt
```

4. Run the application:

```commandline
python3 run.py
```

**Install with Poetry**

1. Clone git repository or download .zip file:

```commandline
git clone https://github.com/szczyglis-dev/py-gpt.git
cd py-gpt
```

2. Install Poetry (if not installed):

```commandline
pip install poetry
```

3. Create a new virtual environment that uses Python 3.10:

```commandline
poetry env use python3.10
poetry shell
```

4. Install requirements:

```commandline
poetry install
```

5. Run the application:

```commandline
poetry run python3 run.py
```

**Tip**: you can use `PyInstaller` to create a compiled version of
the application for your system (required version >= `6.0.0`).

### Troubleshooting

If you have a problems with `xcb` plugin with newer versions of PySide on Linux, e.g. like this:

```commandline
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. 
Reinstalling the application may fix this problem.
```

...then install `libxcb`:

```commandline
sudo apt install libxcb-cursor0
```

If you have a problems with audio on Linux, then try to install `portaudio19-dev` and/or `libasound2`:

```commandline
sudo apt install portaudio19-dev
```

```commandline
sudo apt install libasound2
sudo apt install libasound2-data 
sudo apt install libasound2-plugins
```

**Camera access in Snap version:**

To use camera in Vision mode in Snap version you must connect the camera with:

```commandline
sudo snap connect pygpt:camera
```

**Windows and VC++ Redistributable**

On Windows, the proper functioning requires the installation of the `VC++ Redistributable`, which can be found on the Microsoft website:

https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist

The libraries from this environment are used by `PySide6` - one of the base packages used by PyGPT. 
The absence of the installed libraries may cause display errors or completely prevent the application from running.

It may also be necessary to add the path `C:\path\to\venv\Lib\python3.x\site-packages\PySide6` to the `PATH` variable.

**WebEngine/Chromium renderer and OpenGL problems**

If you have a problems with `WebEngine / Chromium` renderer you can force the legacy mode by launching the app with command line arguments:

``` ini
python3 run.py --legacy=1
```

and to force disable OpenGL:

``` ini
python3 run.py --disable-gpu=1
```

You can also manualy enable legacy mode by editing config file - open the `%WORKDIR%/config.json` config file in editor and set the following options:

``` json
"render.engine": "legacy",
"render.open_gl": false,
```

## Other requirements

For operation, an internet connection is needed (for API connectivity), a registered OpenAI account, 
and an active API key that must be input into the program.

The API key can be obtained by registering on the OpenAI website:

<https://platform.openai.com>

Your API keys will be available here:

<https://platform.openai.com/account/api-keys>