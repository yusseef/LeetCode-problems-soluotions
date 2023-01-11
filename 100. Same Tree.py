def isSameTree(self, p, q):
    if not p and not q: 
        return True

    if not p or not q or q.val != p.val:
        return False

    return (self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right))
