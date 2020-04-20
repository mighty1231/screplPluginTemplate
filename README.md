# SC-REPL Plugin Template

plugin template for [screpl](https://github.com/mighty1231/screpl)

Check how it works in this [video](https://youtu.be/6RexCF3SBFU)


## Required

* [euddraft](https://github.com/armoha/euddraft)
* move a folder `repl` of [screpl](https://github.com/mighty1231/screpl) in `lib` folder in euddraft


## How to develop

* copy a folder `mymodule` into `lib` folder of euddraft
* make your own codes, you could add more apps in a single module


## How to test the module in game

* copy a file `prepl.py ` into `plugins` folder in euddraft
* Make your euddraft project file (\*.edd) be follows

```
[main]
input: INPUT.scx
output: OUTPUT.scx

[prepl.py]
superuser: P1
plugins: mymodule
```

Also, you can use more than one modules

```
[main]
input: INPUT.scx
output: OUTPUT.scx

[prepl.py]
superuser: P1
plugins: mymodule module2 module3
```
