import py_trees
 
# 创建根节点 - 一个按顺序尝试每个选项的选择器
root = py_trees.composites.Selector("Character Decisions", memory=False)
 
# 创建行为
attack = py_trees.behaviours.Success(name="Attack")
defend = py_trees.behaviours.Success(name="Defend")
rest = py_trees.behaviours.Success(name="Rest")
 
# 将行为添加到选择器
root.add_children([attack, defend, rest])
 
# 创建并设置行为树
behaviour_tree = py_trees.trees.BehaviourTree(root=root)
behaviour_tree.setup(timeout=15)
 
# 显示树结构
print(py_trees.display.unicode_tree(root=root))

print(py_trees.display.ascii_tree(root=root))

print(py_trees.display.render_dot_tree(root=root))
