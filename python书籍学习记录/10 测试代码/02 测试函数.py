from name_function import get_formatted_name

print('输入"q"退出程序。')

while True:
    first = input('请输入你的姓氏：')
    if first == 'q':
        break
    last = input('请输入你的名字：')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f'规范格式的名字：{formatted_name}')
    
# 单元测试和测试用例
# 软件的测试方法多种多样。一种最简单的测试是单元测试（unit test），用于核实函数的某个方面没有问题。
# 测试用例（test case）是一组单元测试，这些单元测试一道核实函数在各种情况下的行为都符合要求。
# 良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情况的测试。全覆盖（full coverage）测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
# 对于大型项目，要进行全覆盖测试可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。

# 可通过的测试
# 测试文件的名称很重要，必须以 test_打头。当你让 pytest 运行测试时，它将查找以 test_打头的文件，并运行其中的所有测试。

# 运行测试
# 打开一个终端窗口，并切换到这个测试文件所在的文件夹。如果你使用的是 VS Code，可打开测试文件所在的文件夹，并使用该编辑器内嵌的终端。



