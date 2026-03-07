from name_function import get_formatted_name

def test_get_formatted_name():
    """ 能够正确地处理像 Janis Joplin 这样的姓名吗？ """
    formatted_name = get_formatted_name('janis', 'joplin')
    # 断言（assertion）
    assert formatted_name == 'Janis Joplin'





