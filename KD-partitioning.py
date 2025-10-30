from binarytree import tree, Node
import math
class KD_Tree:
    def __init__(self,data):
        self.data=data
        self.tree=None
        
    def build(self,points,depth):
        k=len(points.columns)
        _axis=depth % k
        _column=points.columns[_axis]
        
        if len(points)==0:
            return None
        objects_list=points.sort_values(by=[_column],ascending=True)
        
        if len(objects_list)%2==0:
            median_idx=int((len(objects_list)/2))
        else:
            median_idx=math.floor((len(objects_list)/2))
        
        node=Node(round(objects_list.iloc[median_idx][_column],3))
        node.left=self.build(objects_list.iloc[0:median_idx],depth+1)
        node.right=self.build(objects_list.iloc[median_idx:],depth+1)
        
        return node
    def build(self):
        self.tree=self._build(self.data,depth=0)
        
        