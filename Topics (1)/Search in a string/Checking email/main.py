def check_email(string):
    if string.count(" ") > 0:
        return False
    elif string.find("@") > 0 and string.find(".", string.find("@")) > string.find("@") + 1:
        return True
    else:
        return False
