import ipaddress

def cidr_to_list(cidr) -> list:
    return [str(ip) for ip in ipaddress.IPv4Network(cidr)]

def get_black_list():
    with open("proxy/blacklist.txt") as file:
        x = file.readlines()
    x = [x.strip() for x in x]
    ls = [cidr_to_list(cidr) for cidr in x]
    return ls

def get_user_passes():
    with open('accounts.txt') as file:
        x = file.readlines()
    x = [x.strip() for x in x]
    all_ = [x.split(':') for x in x]
    return all_

if __name__ == "__main__":
    # for cidr in 
    print(get_black_list())
    print(get_user_passes())
    # print(cidr_to_list(cidr))

