def format_name(f_name, l_name):
    """
    Takes a first an last name and returns a title
    :param f_name:
    :param l_name:
    :return: titled name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



