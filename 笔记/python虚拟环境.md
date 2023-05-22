# Python虚拟环境

##### 在新的Windows电脑上运行Python程序并自动下载所需的库，可以使用Python虚拟环境和pip工具。虚拟环境可以将Python程序和其依赖项隔离到单独的环境中，而pip工具可以自动下载和安装所需的Python库。

###### 以下操作都在命令行操作，且都依以Windows为例

## venv

1. 使用以下命令创建虚拟环境,其中“venv”是您要创建的虚拟环境的名称：
    ``` 
    python -m venv venv 
    ```

  
2. 激活并进入虚拟环境
    ``` 
    myenv\Scripts\activate.bat 
    ```
    - 将激活虚拟环境并将其添加到命令提示符中

3. 现在，可以使用pip安装所需的Python包，例如：
    ``` 
    pip install numpy 
    ```
    - 这将安装名为“numpy”的包及其所有依赖项。


## virtualenv

- virtualenv是一个第三方的工具，用来创建和管理虚拟环境  。它可以让你创建和使用不同的虚拟环境，并提供了更多的选项和参数，比如指定Python版本、指定环境目录、指定包源等  。
- 使用virtualenv的方法有以下几种：
    - 第一种方法，使用`virtualenv`命令。这个命令会在指定的目录生成一个虚拟环境^ [2]^：

```
virtualenv <ENV_DIR>
```

- 这个命令会在<ENV_DIR>目录下创建一个虚拟环境，如果<ENV_DIR>不存在，它会自动创建^ [2]^。然后，你可以使用以下命令来激活这个虚拟环境^ [2]^：

```
<ENV_DIR>\Scripts\activate
```

- 这个命令会让你进入到这个虚拟环境中，你可以在这里安装和使用Python包^ [2]^。
    - 第二种方法，使用`virtualenv --python`命令。这个命令会在指定的目录生成一个指定Python版本的虚拟环境^ [2]^：

```
virtualenv --python <PYTHON_EXE> <ENV_DIR>
```

- 这个命令会在<ENV_DIR>目录下创建一个虚拟环境，如果<ENV_DIR>不存在，它会自动创建^ [2]^。它也会使用<PYTHON_EXE>作为虚拟环境的Python解释器^ [2]^。然后，你可以使用以下命令来激活这个虚拟环境^ [2]^：

```
<ENV_DIR>\Scripts\activate
```

- 这个命令会让你进入到这个虚拟环境中，你可以在这里安装和使用Python包^ [2]^。
    - 第三种方法，使用`virtualenv --no-site-packages`命令。这个命令会在指定的目录生成一个不包含系统已安装包的虚拟环境^ [2]^：

```
virtualenv --no-site-packages <ENV_DIR>
```

- 这个命令会在<ENV_DIR>目录下创建一个虚拟环境，如果<ENV_DIR>不存在，它会自动创建^ [2]^。它也会让这个虚拟环境不继承系统已安装的任何Python包^ [2]^。然后，你可以使用以下命令来激活这个虚拟环境^ [2]^：

```
<ENV_DIR>\Scripts\activate
```

- 这个命令会让你进入到这个虚拟环境中，你可以在这里安装和使用Python包^ [2]^。



=============  
- 如果您需要将所有已安装的包及其版本号写入到一个名为“requirements.txt”的文件中，请使用以下命令：
    ``` 
    pip freeze > requirements.txt 
    ```
    - 这将在当前目录中创建一个名为“requirements.txt”的文件，并将所有已安装的包及其版本号写入该文件中。

- 使用以下命令安装“requirements.txt”文件中列出的所有Python包：
     ```
     pip install -r requirements.txt
     ```
    - 这将自动下载和安装所有在“requirements.txt”文件中列出的Python包及其所有依赖项

- 在虚拟环境中卸载“requirements.txt”文件中列出的所有库，可以使用以下命令：
     ```
     pip uninstall -r requirements.txt -y
     ```
    - 其中，“-y”选项将自动确认卸载所有库，而无需手动确认每个库的卸载。