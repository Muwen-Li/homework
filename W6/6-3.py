class GameConfigManager:
    _instance = None#尚未创建任何实例
    def __init__(self):
        self.difficulty="normal"
        self.soundEnabled=True
        self.maxLevels=10     
    def __new__(cls):
        if not cls._instance:#确保只有一个实例
             cls._instance = super(GameConfigManager,cls).__new__(cls)
        #用super函数创建实例
        return cls._instance
    
    def set_difficulty(self, difficulty):
        self.difficulty=difficulty
    def set_sound_enabled(self, enabled):
        self.soundEnabled=enabled

    def set_max_levels(self, levels):
        self.maxLevels=levels

    def get_difficulty(self):
        return self.difficulty

    def is_sound_enabled(self):
        return self.soundEnabled

    def get_max_levels(self):
        return self.maxLevels

Manager1 = GameConfigManager()
Manager2 = GameConfigManager()
assert Manager1 is Manager2, "单例模式实现失败"

difficulty, enabled, levels = input().split()
    # 更改Manager1的属性
    
Manager1.set_difficulty(difficulty)
Manager1.set_sound_enabled(enabled)
Manager1.set_max_levels(int(levels))

    # 获取配置并验证
print(f"{Manager2.get_difficulty()},{Manager2.is_sound_enabled()},{Manager2.get_max_levels()}")