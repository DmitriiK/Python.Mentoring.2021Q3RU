d_phones = {}


def merge_user():
    """
    merge user data (insert new phone entry or update users's phone
    :return: str
    :rtype:
    """
    user_name = input('Enter user name insert our update data >>')
    phone = input('Enter phone >>')
    phones = d_phones.setdefault(user_name, [])
    if phone not in phones:
        phones.append(phone)


def get_user():
    """
    output user info by user_name
    :return: None
    :rtype:
    """
    user_name = input('Enter user name you want to find >>')
    user_phones = d_phones.get(user_name)
    if user_phones is None or len(user_phones) == 0:
        print(f"No user '{user_name}' here")
    else:
        for phone in user_phones:
            print(f'{user_name:20} {phone:10}')


def del_user():
    """
    delete user
    :return: None
    :rtype:
    """
    user_name = input('Enter user name you want to delete from dictionary >>')
    if user_name not in d_phones.keys():
        print(f'no {user_name =} in dictionary')
    else:
        del d_phones[user_name]


d_command_mapper = {'add': merge_user, 'get': get_user,
                    'del': del_user, 'exit': lambda: exit()}


def main():
    """    main function - kind of user interface     """
    while True:
        command = input("Enter command you want to execute. "
                        "Options: '"
                        f"{','.join(list(d_command_mapper.keys()))}' >>")
        if command not in d_command_mapper.keys():
            print(f"Command '{command}' is not valid")
            continue
        d_command_mapper[command]()


if __name__ == '__main__':
    main()
