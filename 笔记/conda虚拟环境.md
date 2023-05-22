- conda是一种用来管理Python包和环境的工具¹²³。它可以让你创建和使用不同的虚拟环境，每个虚拟环境都有自己的Python安装和包依赖，可以避免不同项目之间的冲突和污染¹²³。
- 创建conda虚拟环境的命令是 `conda create`¹²³。你可以使用 `-n` 参数来指定虚拟环境的名称，使用 `-p` 参数来指定虚拟环境的路径，使用 `python` 参数来指定Python的版本，使用 `anaconda` 参数来安装Anaconda发行版中的所有包，或者使用其他包的名称来安装指定的包¹²³。
- 例如，如果你想创建一个名为 `test_env` 的虚拟环境，使用Python 3.6.3 版本，并安装BioPython包，你可以输入以下命令¹²³：

```
conda create -n test_env python=3.6.3 biopython
```

- conda会检查并安装BioPython所需要的其他包（\"依赖\"），并询问你是否继续。如果你同意，输入 `y` 并回车¹²³。
- 创建好conda虚拟环境后，你需要激活它，才能使用它。激活的命令是 `conda activate`，后面跟上虚拟环境的名称或路径。例如，如果你想激活刚刚创建的 `test_env` 虚拟环境，你可以输入以下命令：

```
conda activate test_env
```

- 激活后，你会看到命令行提示符前面有虚拟环境的名称，表示你已经进入了虚拟环境。
- 激活虚拟环境后，你就可以在里面安装和使用Python包了。你可以使用 `pip` 命令或者 `conda install` 命令来安装或升级包。例如，如果你想在 `test_env` 虚拟环境中安装NumPy包，你可以输入以下命令：

```
pip install numpy
```

或者

```
conda install numpy
```

- 当你不需要使用虚拟环境时，你可以退出它。退出的命令是 `conda deactivate`。退出后，你会回到原来的Python环境，不再受到虚拟环境的影响。
- 如果你想删除一个虚拟环境，你可以使用 `conda remove` 命令，并加上 `-n` 或 `-p` 参数来指定虚拟环境的名称或路径，以及 `--all` 参数来删除所有相关文件。例如，如果你想删除刚刚创建的 `test_env` 虚拟环境，你可以输入以下命令：

```
conda remove -n test_env --all
```
