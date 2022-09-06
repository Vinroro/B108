class Tag:
    def __init__(self):
        self.tag = "tag"

    def get_html(self):
        return f"<{self.tag}></{self.tag}>"


class Image(Tag):
    def __init__(self):
        self.tag = "img"


class Input(Tag):
    def __init__(self):
        self.tag = "input"


class Text(Tag):
    def __init__(self):
        self.tag = "p"


class Link(Tag):
    def __init__(self):
        self.tag = "a"


class TagFactory:
    def create_tag(self, type):
        if type == "image":
            return Image()
        elif type == "input":
            return Input()
        elif type == "p":
            return Text()
        elif type == "a":
            return Link()
        else:
            return Tag()


factory = TagFactory()
elements = ["image", "input", "p", "a", ""]
for el in elements:
    print(factory.create_tag(el).get_html())
