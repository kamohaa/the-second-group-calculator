def str_showcenter():
    input_string = input("Введите строку: ")

    terminal_width = 80
    terminal_height = 25

    vertical_center = terminal_height // 2
    
    horizontal_padding = (terminal_width - len(input_string)) // 2
    
    print("\n" * vertical_center)
    
    print(" " * horizontal_padding + input_string)
    
    remaining_lines = terminal_height - vertical_center - 1
    if remaining_lines > 0:
        print("\n" * remaining_lines)

if __name__ == "__main__":
    str_showcenter()