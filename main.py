


# def notebook():
#
#     todo_list: list[str] = []
#
#     def add_todo(todo: str)-> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#
#     def get_all()->list[str]:
#          nonlocal todo_list
#          return todo_list
#
#
#     return add_todo,get_all
#
#
# add, all_todos = notebook()
#
# add('lnok')
#
# print(all_todos())
def count_decor(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count+=1
        res = func(*args, **kwargs)
        print(f'{count=}')
        return res
    return inner

@count_decor
def expanded_form(num:int)->str:
    st =str(num)
    return '+ ' .join(ch+ '0'*(len(st)-i-1) for i, ch in enumerate(st) if ch!='0')
print(expanded_form(1234))




print(expanded_form(54545))
print(expanded_form(54545))