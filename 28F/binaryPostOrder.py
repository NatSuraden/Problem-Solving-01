def PostorderTrraversal(self,root):
    res = []
    if root:
        res = self.PostorderTrraversal(root.left)
        res = res+self.PostorderTrraversal(root.right)
        res.append(root.data)
    return res