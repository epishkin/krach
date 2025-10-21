# EJ and NJYHL KRACH Calculators

## Setup
```shell
#install uv
brew install uv

#init a project
uv init

#download dependencies
uv add -r requirements.txt
```

## Download and update EJ ratings
```shell
#download
uv run ej.py download --div="14U Futures Silver 1"

#update
uv run ej.py update --div="14U Futures Silver 1"
```

## Download and update NJYHL ratings
```shell
#download
uv run njyhl.py download --div="14U-AA"

#update
uv run njyhl.py update --div="14U-AA"
```

## Download and update NJYHL 18U-AA ratings
```shell
#download
uv run njyhl.py download --div="18U-AA"

#update
uv run njyhl.py update --div="18U-AA"
```