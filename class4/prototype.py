# TODO: class Prototype

class Title:
    def __init__(self, title): 
        self.text = title


class Content:
    def __init__(self, content):
        self.text = content


class Document(Prototype):
    def set_title(self, title: Title):
        self.title = title

    def set_content(self, content: Content):
        self.content = content

    # TODO: implement clone()

    def __str__(self):
        return f'Title: {self.title.text}, Content: {self.content.text}'


with open('rank.txt', 'w') as f:
    f.wirte

if __name__ == '__main__':
    doc1 = Document()

    title = Title('Hello I am Title')
    content = Content('Hello I am Content')

    doc1.set_title(title)
    doc1.set_content(content)
    print(doc1)
    """Excepted Result
    Title: Hello I am Title, Content: Hello I am Content
    """
    print()

    doc2 = doc1.clone()
    print(doc2)
    """Excepted Result
    Title: Hello I am Title, Content: Hello I am Content
    """
    print()

    title.text = 'YOYOYO'
    content.text = 'HAHAHA'
    print(doc1)
    print(doc2)
    """Excepted Result
    Title: YOYOYO, Content: HAHAHA
    Title: Hello I am Title, Content: Hello I am Content
    """

