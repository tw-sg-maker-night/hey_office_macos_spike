# Hey Office (Python)

## Python Setup Quickstart

```
brew install python
pip3 install virtualenv
pip3 install virtualenvwrapper
```

Add to .bash_profile or .zshrc, etc.

```
# Python3
export WORKON_HOME=~/PythonEnvs
export PROJECT_HOME=~/PythonProjects
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7
source /usr/local/bin/virtualenvwrapper.sh
```

### References
http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/
http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/#virtualenvironments-ref


## Snowboy Setup

```
brew install swig portaudio sox
pip install pyaudio
pip install boto3
```

```
import snowboydecoder
def detected_callback():
  print "hotword detected"

detector = snowboydecoder.HotwordDetector("resources/Hey_Office.pmdl", sensitivity=0.45, audio_gain=1)
detector.start(detected_callback)
```
