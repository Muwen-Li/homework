emotions=['anger','disgust','fear','sadness','joy']
emo_dict={}
for emotion in emotions:
    path=f'{"C:\\Users\\Lenovo\\Desktop\\emotion_lexicon (1)\\emotion_lexicon"}/{emotion}.txt'
    with open(path,'r',encoding='utf-8') as f:
        emo_dict[emotion]=set(f.read().splitlines())

import pandas as pd
import matplotlib.pyplot as plt

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
        return str(dominant_emotion[0])
    return analyze
analyze_comment=one_emotion_ana(emo_dict)

def emotion_scores_consistency(path,shop_ID):
    df = pd.read_csv(path)
    data=df[df['shopID']==shop_ID]
    selected_data=[]
    for index,row in data.iterrows():
        comment=row['cus_comment']
        rating=row['stars']
        emotion=analyze_comment(comment)
        selected_data.append({'emotion':emotion,'rating':rating,'comment':comment})
    
    selected_data=pd.DataFrame(selected_data)

    status={'positive-high rating':len(selected_data[(selected_data['emotion']=='joy')&(selected_data['rating']>=4)]),'positive-low rating':len(selected_data[(selected_data['emotion']=='joy')&(selected_data['rating']<=4)]),'negative-high rating':len(selected_data[(selected_data['emotion']!='joy')&(selected_data['rating']>=4)]),'negative-low rating':len(selected_data[(selected_data['emotion']!='joy')&(selected_data['rating']<=4)])}

    plt.figure(figsize=(10,6))
    bar_width=0.35
    x_position=[0,1,3,4]
    colors = ['#1f77b4','#ff7f0e', '#1f77b4','#ff7f0e']
    bars = plt.bar(x_position,[status['positive-high rating'], status['negative-high rating'], status['negative-low rating'], status['positive-low rating']],width=bar_width,color=colors)
    plt.title(f'{shop_ID}-Consistency between Emotions and Ratings')
    plt.xticks(ticks=[0.5, 3.5], labels=['high ratings', 'low ratings'],rotation=0)
    plt.ylabel('Number of Comments')
    legend_elements = [plt.Rectangle((0,0),1,1, fc='#1f77b4', label='Consistent (Positive High / Negative Low)'),plt.Rectangle((0,0),1,1, fc='#ff7f0e', label='Inconsistent (Positive Low / Negative High)')]
    plt.legend(handles=legend_elements, title="Emotion-Rating Match")
    total_high = status['positive-high rating'] + status['negative-high rating']
    total_low = status['positive-low rating'] + status['negative-low rating']
    for bar, x in zip(bars, x_position):
        height = bar.get_height()
        if x == 0: 
            percentage = (status['positive-high rating'] / total_high * 100) if total_high > 0 else 0
        elif x == 1:  
            percentage = (status['negative-high rating'] / total_high * 100) if total_high > 0 else 0
        elif x == 3:  
            percentage = (status['negative-low rating'] / total_low * 100) if total_low > 0 else 0
        elif x == 4: 
            percentage = (status['positive-low rating'] / total_low * 100) if total_low > 0 else 0
        plt.text(x, height + 1, f'{height}\n({percentage:.1f}%)',ha='center',va='bottom',fontsize=9)
    plt.tight_layout()
    plt.show()
    
    inconsistent_low = selected_data[((selected_data['emotion'] == 'joy') & (selected_data['rating'] < 4)) ]
    print("\n低分不一致评论（最多10条）：")
    print("====================================")
    for idx, row in inconsistent_low.head(10).iterrows():
        print(f"评分：{row['rating']} | 情绪：{row['emotion']}")
        print(f"评论：{row['comment']}")
        print("-------------------------------------")


emotion_scores_consistency('C:\\Users\\Lenovo\\Desktop\\week3.csv',521698)
