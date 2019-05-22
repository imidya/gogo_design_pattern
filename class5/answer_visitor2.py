import abc

class Element(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor):
        raise NotImplementedError()


class Root(Element):

    node_type = 'Root'
    children = []

    def accept(self, visitor):
        visitor.visit_root(self)


class Node(Element):

    node_type = 'Node'

    def accept(self, visitor):
        visitor.visit_node(self)


class Visitor(abc.ABC):

    @abc.abstractmethod
    def visit_root(self, root):
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_node(self, node):
        raise NotImplementedError()


class JSONVisitor(Visitor):
    
    def visit_root(self, root):
        print('JSON format: Root')

    def visit_node(self, node):
        print('JSON format: Node')


class XMLVisitor(Visitor):
    
    def visit_root(self, root):
        print('XML format: Root')

    def visit_node(self, node):
        print('XML format: Node')


if __name__ == '__main__':
    root = Root()
    node = Node()
    json_visitor = JSONVisitor()
    xml_visitor = XMLVisitor()

    root.accept(json_visitor)
    root.accept(xml_visitor)

    node.accept(json_visitor)
    node.accept(xml_visitor)
