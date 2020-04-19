# SC-REPL Plugin Template

plugin template for [screpl](https://github.com/mighty1231/screpl)


## Required

* [euddraft](https://github.com/armoha/euddraft)
* move a folder `repl` of [screpl](https://github.com/mighty1231/screpl) in `lib` folder in euddraft


## How to develop

* copy a folder `mymodule` into `lib` folder of euddraft
* modify files, you could add more apps in a single module


## How to test in game

Make your euddraft project file (\*.edd) be follows

```
[repl]
plugins: mymodule
```

or
```
[repl]
command: openMine
```
