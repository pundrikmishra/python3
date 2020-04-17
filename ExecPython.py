exec("print('So this works like eval')")

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [5,6,2,1,1]")
print(list_str2)

exec("def test(): print('pundrik mishra is a good person but..........')")
test()

exec("""
def test2():
    print('kajal pundrik makati was good friend')
""")
test2()