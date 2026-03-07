# 虽然 Python 通过标准库提供了大量的功能，但 Python 开发人员还是需要频繁用到第三方包。
# 第三方包（third-party package）指的是独立于 Python 核心的库。有些深受欢迎的第三方包最终会被纳入标准库，并从此随 Python 一起被安装。

# 更新 pip
# Python 提供了一款名为 pip 的工具，可用来安装第三方包。因为 pip 帮我们安装来自外部的包，所以更新频繁，以消除潜在的安全问题。有鉴于此，我们先来更新 pip。
#终端执行：python -m pip install --upgrade pip

# 可使用下面的命令更新系统中安装的任何包：python -m pip install --upgrade package_name

# 安装 pytest  python -m pip install --user pytest