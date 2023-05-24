import platform

def info():
    os = platform.system()
    user = platform.node()
    com = platform.machine()
    return(f'''He dieu hanh cua may la: {os}
Ten nguoi dung la: {user}
Ten may la: {com}''')