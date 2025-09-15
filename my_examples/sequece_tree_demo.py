import py_trees
import time

class MyBehaviour(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super().__init__(name)
        self.count = 0
    
    def setup(self):
        # 一次性初始化（硬件连接等）
        print(f"Setting up {self.name}")
    
    def initialise(self):
        # 准备执行（重置变量，启动计时器）
        print(f"Initializing {self.name}")
    
    def update(self):
        # 主要逻辑 - 返回SUCCESS、FAILURE或RUNNING
        print(f"Updating {self.name}")
        if self.count < 4:
            self.count += 1
            return py_trees.common.Status.RUNNING
        return py_trees.common.Status.SUCCESS
    
    def terminate(self, new_status):
        # 停止时的清理工作
        print(f"Terminating {self.name} with status {new_status}")
    
# 创建一个根序列（按顺序运行子节点，如果任何失败则停止）
root = py_trees.composites.Sequence("Morning Routine", memory=True)
 
# 创建具有不同结果的行为
wake_up = py_trees.behaviours.StatusQueue(
    name="Wake Up",
    queue=[py_trees.common.Status.RUNNING, py_trees.common.Status.SUCCESS],
    eventually=py_trees.common.Status.SUCCESS
)
 
brush_teeth = py_trees.behaviours.StatusQueue(
    name="Brush Teeth", 
    queue=[py_trees.common.Status.RUNNING, py_trees.common.Status.SUCCESS],
    eventually=py_trees.common.Status.SUCCESS
)

my_behaviour = MyBehaviour("My Behaviour")
 
have_coffee = py_trees.behaviours.Failure(name="Have Coffee")  # 这将失败！
 
# 将行为添加到序列
root.add_children([wake_up, brush_teeth, my_behaviour, have_coffee])
 
# 创建并运行树
behaviour_tree = py_trees.trees.BehaviourTree(root=root)
behaviour_tree.setup(timeout=15)
 
# 运行树几个周期以查看行为
for i in range(1, 10):
    print(f"\n--- Tick {i} ---")
    behaviour_tree.tick()
    print(py_trees.display.unicode_tree(root=root, show_status=True))
    #py_trees.display.render_dot_tree(root=root, name=f"tick_{i}", target_directory=".")
    time.sleep(0.5)
