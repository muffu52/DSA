
def stack_check(check):
    open_bracks  = ['(', '{', '[']
    close_bracks = [')', '}', ']']
    S = []
    for i in check:
        if i in open_bracks:
            # open_index = open_bracks.index(i)
            S.append(i)
        elif i in close_bracks:
            if len(S) == 0:
                print('underflow')
                return "not ok"
            close_index = close_bracks.index(i)
            # print(close_index)
            if open_bracks[close_index] == S[-1]: # if it matches the top of the stack S
                S.pop()
            else:
                return "not ok"
    return S


if __name__ == "__main__":
    
    Arr = ["{[[]]{()}}","[{}","}"]

    for i in Arr:
        print("'" +i+"'")
        res = stack_check(i)
        if res == 'not ok':
            print('not ok') 
        elif len(res) > 0:
            print('not ok') 
        else:
            print('ok')
    
    
