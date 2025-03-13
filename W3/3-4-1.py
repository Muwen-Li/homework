emotions=['anger','disgust','fear','sadness','joy']
emo_dict={}
for emotion in emotions:
    path=f'{"C:\\Users\\Lenovo\\Desktop\\emotion_lexicon (1)\\emotion_lexicon"}/{emotion}.txt'
    with open(path,'r',encoding='utf-8') as f:
        emo_dict[emotion]=set(f.read().splitlines())

def mix_emotion_ana(emo_dict):
    def analyze(comment):
        total=0
        counts={emotion:0 for emotion in emo_dict.keys()}
        for word in comment.split():
            for emotion in emo_dict.keys():
                if word in emo_dict[emotion]:
                    counts[emotion]+=1
                    total+=1
        if total==0:
            return{emotion:0 for emotion in emo_dict.keys()}
        ratios={emotion:counts[emotion]/total for emotion in emo_dict.keys()}
        return ratios
    
    return analyze

def one_emotion_ana(emo_dict):
    def analyze(comment):
        total=0
        counts={emotion:0 for emotion in emo_dict.keys()}
        for word in comment.split():
            for emotion in emo_dict.keys():
                if word in emo_dict[emotion]:
                    counts[emotion]+=1
                    total+=1
        if total==0:
            return{emotion:0 for emotion in emo_dict.keys()}
        max_emotion=max(counts.values())
        dominant_emotion=[emotion for emotion in emo_dict.keys() if counts[emotion]==max_emotion]
        return dominant_emotion
    
    return analyze

analyze_comment=mix_emotion_ana(emo_dict)
analyze_comment1=one_emotion_ana(emo_dict)
print(analyze_comment("心 念念 地 跑过来 上下 九 这边 就 为了 南信 啊 环境 在 老字号 里 南信 环境 算是 不错 啦 可惜 人太多 整个 店 都 好 拥挤 服务态度 还 不错 一 二楼 都 可以 点餐 二楼 支持 手机 支付 菜品 就 想 吃 个 椰汁 香芋 西米露 但 好像 不是 椰汁 是 牛奶 耶奶味 灰常重 香芋 不粉 总体 感觉 一般 而且 有点 贵 一小 碗 居然 要 块钱"))
print(analyze_comment1("补发 点评 目前为止 吃 过 的 最 好吃 的 双皮奶 没有 之一 去 广州 一定 要 尝试 他家 的 双皮奶 不然 是 人生 一大 憾事 杨枝 甘露 也 不错 比较 解腻 适合 饭后 吃 还 点 过 两道 主食 鲜虾 云吞面 尚可 菌菇 叉烧 肠粉 不 推荐 因为 他家 一直 人 很多 想着 难得 来 一次 多 尝试 一些 口味 匆忙 间 随机 点 了 个 椰汁 香芋 西米露 不错 香芋 又 糯 又 大块 但 不是 我 的 菜 仔细 研究 菜单 后 发现 好 想 吃 雪 牛奶 雪耳炖 木瓜 下次 有 机会 再 来 广州 玩 一定 要 再 来 吃"))