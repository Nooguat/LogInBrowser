import os


def get(dict_name, key_name, return_default=False):
    file = parameters_exists()
    x = file.readlines()
    default = ""
    x = [i[:-1] for i in x]
    for i in range(len(x)):
        if x[i] == '$BEGIN$':
            while x[i] != "$END":
                i += 1
                if x[i] == dict_name:
                    print("test1")
                    end_dict = "[END " + dict_name[1:]
                    while x[i] != end_dict:
                        res = x[i].split(' > ')
                        if res[0] == key_name:
                            return res[1]
                        if res[0] == "default":
                            default = res[1]
                        i += 1
                if return_default is True:
                    return default
            return -1


def get_all_values(dict_name):
    file = parameters_exists()
    x = file.readlines()
    x = [i[:-1] for i in x]
    rslt = list()
    for i in range(len(x)):
        if x[i] == '$BEGIN$':
            while x[i] != "$END":
                i += 1
                if x[i] == dict_name:
                    end_dict = "[END " + dict_name[1:]
                    while x[i] != end_dict:
                        rslt.append(x[i])
                        i += 1
                    return rslt


def exist(dict_name, key_name):
    file = parameters_exists()
    x = file.readlines()
    x = [i[:-1] for i in x]
    for i in range(len(x)):
        if x[i] == '$BEGIN$':
            while x[i] != "$END":
                i += 1
                if x[i] == dict_name:
                    end_dict = "[END " + dict_name[1:]
                    while x[i] != end_dict:
                        res = x[i].split(' > ')
                        if res[0] == key_name:
                            return True
                        i += 1
            return False


def set_new(dict_name, key_name, value, modif=False):
    file = parameters_exists()
    y = file.readlines()
    x = [i[:-1] for i in y]
    for i in range(len(x)):
        if x[i] == '$BEGIN$':
            while x[i] != "$END":
                i += 1
                if x[i] == dict_name:
                    if modif is False:
                        new_line = key_name + " > " + value
                        y.insert(i + 1, new_line + "\n")
                        file = parameters_exists('w')
                        file.writelines(y)
                        file.close()
                        return
                    end_dict = "[END " + dict_name[1:]
                    while x[i] != end_dict:
                        res = x[i].split(' > ')
                        if res[0] == key_name:
                            new_value = res[0] + " > " + value + "\n"
                            y[i] = new_value
                            file = parameters_exists('w')
                            file.writelines(y)
                            file.close()
                            return
                        i += 1


def remove(dict_name, key_name):
    file = parameters_exists()
    y = file.readlines()
    x = [i[:-1] for i in y]
    for i in range(len(x)):
        if x[i] == '$BEGIN$':
            while x[i] != "$END":
                i += 1
                if x[i] == dict_name:
                    end_dict = "[END " + dict_name[1:]
                    while x[i] != end_dict:
                        res = x[i].split(' > ')
                        if res[0] == key_name:
                            del y[i]
                            file = parameters_exists('w')
                            file.writelines(y)
                            file.close()
                            return
                        i += 1


def parameters_exists(mode='r'):
    path = os.path.dirname(os.path.realpath(__file__))
    path = path + "/SE_parameters"
    try:
        file = open(path, mode)
        return file
    except FileExistsError:
        file = open('SE_parameters', 'w')
        text = '#This file is automaticly modified by the handle file, so you should\'nt modify by yourself\n\n$BEGIN$\n[SEARCH ENGINE]\ndefault > www.google.fr/search?q=a\n[END SEARCH ENGINE]\n[FILE LINKS]\n[END FILE LINKS]\n[FILE EXT LINKS]\n[END FILE EXT LINKS]\n$END$'
        file.write(text)
        file.close()
        return file
