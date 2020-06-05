import wikipedia


def main():
    page_title = input("page title : ")
    while page_title != "":
        try:
            print(wikipedia.search(page_title))
            print(wikipedia.summary(page_title))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        page_title = input("page title : ")

    print("Thank You")


if __name__ == '__main__':
    main()
