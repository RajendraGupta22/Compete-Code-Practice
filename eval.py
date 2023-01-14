
a="11*2?1+3?*7?++879?"
arithmetic = [ "+", "-", "*", "/" ]

def compute_old( txt ):
    _resp = None
    print("txt : ",txt)
    if "?" not in txt:
        return eval(txt)
    _ar = txt.split("?")
    pre = ""
    for x in _ar:
        if not x:
            continue
        _full_operator = ""
        for _op in x:
            if _op in arithmetic:
                _full_operator += _op
        if _full_operator not in arithmetic:
            _resp = "Invalid Operator operation."
            print(_resp)
            break
        pre+=x
        ev = eval(pre)
        _resp = ev
        print(_resp)

def compute( txt ):
    _resp = None
    print("txt : ",txt)
    if "?" not in txt:
        return eval(txt)
    _ar = txt.split("?")
    pre = ""
    for x in _ar:
        if not x:
            continue
        _full_operator = ""
        _opx_index = len(x)-1
        for _e,_op in enumerate(x):
            #  check current and nxt chara are operator or not 
            # print(_e," : ",_op)
            if _e < _opx_index:
                _cur = _op
                _next = x[_e+1]
                if _cur in arithmetic and _next in arithmetic:
                    _full_operator = "++"
                    break
        if _full_operator and _full_operator not in arithmetic:
            _resp = "Invalid Operator operation."
            print(_resp)
            break
        pre+=x
        ev = eval(pre)
        _resp = ev
        print(_resp)



# test 2
a="(2+3)?"
# test 3
a = "11*2?1+3?*(5*2)?"

compute(a)

