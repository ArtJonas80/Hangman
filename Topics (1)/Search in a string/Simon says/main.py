def what_to_do(ins):
    ss = "Simon says"
    if ins.startswith(ss) or ins.endswith(ss):
        if ins.startswith(ss):
            ins = ins.replace(ss, "")
            ins = "I" + ins
        else:
            ins = ins.replace(ss, "")
            ins = "I " + ins
        return ins
    else:
        return "I won't do it!"
