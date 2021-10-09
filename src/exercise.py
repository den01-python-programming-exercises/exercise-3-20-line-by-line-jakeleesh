def main():
    #write your code below this line
    while True:
        user_string = input()
        if (user_string != ""):
            split_string = user_string.split(" ")
            for word in split_string:
                print(word)
        else:
            break


if __name__ == '__main__':
    main()
