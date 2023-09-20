from task_9_checks import Checks
class Input(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
        super().__init__(loc)

search = Input("input#search", 'Found')

# print(search.loc, search.text)
print(search.check_text())


class Button(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
        super().__init__(loc)

search_button = Button("button#search", 'Not Found')

# print(search_button.loc, search_button.text)
print(search_button.check_text())


class Title(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
        super().__init__(loc)

search_title = Title("title#search", 'Found')

# print(search_title.loc, search_title.text)
print(search_title.check_text())


class Link(Checks):

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
        super().__init__(loc)

search_link = Link("link#search", 'Not Found')

# print(search_link.loc, search_link.text)
print(search_link.check_text())