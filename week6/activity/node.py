class Node:
    def __init__(self, animal=None, question=None):
        self._animal = animal
        self._question = question
        self._yes_node = None
        self._no_node = None

    @property
    def animal(self):
        return self._animal

    @animal.setter
    def animal(self, animal):
        self._animal = animal

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, question):
        self._question = question

    @property
    def yes_node(self):
        return self._yes_node

    @yes_node.setter
    def yes_node(self, yes_node):
        self._yes_node = yes_node

    @property
    def no_node(self):
        return self._no_node

    @no_node.setter
    def no_node(self, no_node):
        self._no_node = no_node