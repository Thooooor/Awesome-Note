from note import Tag, recent_list


class NoteSystem:
    def __init__(self, tag, root_path):
        self.root_path = root_path
        self.tag = tag
        self.root = Tag(tag, root_path)

    def span_tree(self):
        self.root.span_tree()
        self.recent_list = recent_list
