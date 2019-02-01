import graphviz


class DOTFileConverter():
    def __init__(self):
        self.g = graphviz.Digraph('also_likes_Duncan', filename='alsolikesgraph')

    def createDOTFile(self, jointReaders, docId, userId):
        readers = jointReaders[docId][0]
        for reader in readers:
            if(reader == userId):
                self.g.attr('node', style="filled", color = "green", shape="box")
            else:
                self.g.attr('node', style = "",shape="box")
            self.g.node(reader[-4:])
        maxResult = 10
        counter = 0

        for key, val in jointReaders.items():
            print("key: " + key)
            print("docId: " + docId)
            if key == docId:
                self.g.attr('node', style="filled", color = "green", shape="circle")
            else:
                self.g.attr('node', shape="circle", style = "", color="black")
            self.g.node(key[-4:])

            for reader in val[0]:
                self.g.edge(reader[-4:], key[-4:])
            if(counter==maxResult):
                break
            counter += 1

        print(readers)
        self.g.render('alsolikes', view=True)
