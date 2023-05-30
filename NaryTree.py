class NaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.children =[]
class NaryTree:
    def __init__(self):
        self.root = None
    def add_node(self, data, parent=None):
        new_node = NaryTreeNode(data)
        if parent is None:
            self.root = new_node
        else:
            for node in self._find_node(parent, self.root):
                node.children.append(new_node)
    def _find_node(self, data, current_node):
        nodes =[]
        if current_node.data ==data:
            nodes.append(current_node)
        for child in current_node.children:
            nodes += self._find_node(data, child)
        return nodes
        
    def find_node(self, data):
        nodes = self._find_node(data, self.root)
        if nodes:
            return nodes[0]
        return None

    def remove_node(self, data):
        node_to_remove = self.find_node(data)  # Encuentra el nodo a eliminar
        if node_to_remove:
            parent = self._find_parent(data, self.root)  # Encuentra el padre del nodo a eliminar
            if parent:
                parent.children.remove(node_to_remove)  # Elimina el nodo de la lista de hijos del padre
            else:
                self.root = None  # Si no hay padre, el nodo a eliminar es la raíz del árbol

    def _find_parent(self, data, current_node):
        if current_node.children:
            for child in current_node.children: # Si tiene una lista de hijos la recorre en busca del nodo
                if child.data == data:
                    return current_node # Si encuentra el nodo, retorna current_node que es el padre actual
                else:
                    parent = self._find_parent(data, child) # Sino, se llama recursivamente para seguir buscando en los children el nodo
                    if parent:
                        return parent
        return None
    def rename_node(self, data, new_data):
        node_to_rename = self.find_node(data) # Busca el nodo a renombrar
        try:
           node_to_rename.data=new_data # renombra el nodo
        except:
            print("nodo no encontrado")
