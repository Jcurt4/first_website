from textnode import TextNode


def main():
    

    text_node = TextNode("This is a test", "p", "http://www.google.com")
    print(text_node.__repr__())


if __name__ == "__main__":
    main()