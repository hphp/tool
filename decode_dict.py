#encoding:utf-8
import json

def decode_dict(dic):
    if not dic:
        return None
    if isinstance(dic, unicode):
        return dic.encode('utf-8')
    elif isinstance(dic, dict):
        for key in dic.keys():
            dic[key] = decode_dict(dic[key])
        return dic
    else:
        return dic

def print_type_dict(c_key, dic):
    if not isinstance(dic, dict):
        print c_key, dic, type(dic)
    else:
        for key in dic.keys():
            print_type_dict(key, dic[key])

if __name__ == "__main__":
    dic = {1:2, '1':3, '2':5, '3':{'aa':'1', 'bb':2, 'cc':u'中文'}}
    dic = json.loads(json.dumps(dic))
    new_dic = decode_dict(dic)
    print_type_dict("ori", new_dic)
