class Publication:

    total_publications = 0

    def __init__(self, name):
        Publication.total_publications += 1
        self.name = name

    def print_information(self):
        print(f'name of publication: {self.name}')

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f'author: {self.author}, page count: {self.page_count}')

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f'chief editor: {self.chief_editor}')

pubs = []
pubs.append(Book('Compartment No.6', 'Rosa Liksom', '192'))
pubs.append(Magazine('Donald Duck', 'Aki Hyyppa¨'))

for pub in pubs:
    pub.print_information()