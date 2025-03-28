from module_5_4_analyzer import TextAnalyzer  

analyzer = TextAnalyzer(textfile_path=r"c:\Users\Lenovo\Desktop\weibo.txt",stopwords_path=r"C:\Users\Lenovo\Desktop\python\homework\W2\cn_stopwords.txt")
analyzer._pre_process()
analyzer._get_word2vec_model()

expanded_lexicon = analyzer.expand_emotion_lexicon(r"C:\Users\Lenovo\Desktop\emotion_lexicon (1)\emotion_lexicon")
emo_dict = {emotion: set() for emotion in ['anger', 'disgust', 'fear', 'sadness', 'joy']}
for word, label in expanded_lexicon.items():
    emo_dict[label].add(word)

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
def emotion_time_analize(path,emotion,shop_ID,time_type):
    df = pd.read_csv(path)
    shop_data=df[df['shopID']==shop_ID]
    shop_data['cus_comment'] = shop_data['cus_comment'].str.strip()  # 去除前后空格
    shop_data['cus_comment'] = shop_data['cus_comment'].str.replace('\n', ' ')  # 替换换行符
    if time_type == 'hour':
        shop_data['time_type'] = shop_data['hour']  
    else:
        shop_data['time_type'] = shop_data['weekday'] 

    filtered_time=shop_data[shop_data['cus_comment'].apply(lambda x:analyze_comment(x)==emotion)]
    if filtered_time.empty:
        print(f"No data found for emotion '{emotion}' in shop ID '{shop_ID}'.")
        return None
    time_freq = filtered_time['time_type'].value_counts().sort_index()
    freq_table = time_freq.reset_index()
    freq_table.columns = ['time_type', 'frequency']
    
    plt.figure(figsize=(12, 6))
    if(time_type=='hour'):
        plt.bar(freq_table['time_type'], freq_table['frequency'], color='skyblue', edgecolor='black')
        plt.xlabel('hour')
        plt.xticks(range(24), [f"{h:02d}:00" for h in range(24)], rotation=45)
    else:
        plt.bar(freq_table['time_type'], freq_table['frequency'], color='skyblue', edgecolor='black')
        plt.xlabel('weekday')
        plt.xticks(range(7),['0','1','2','3','4','5','6'],rotation=45)
    plt.title(f' {shop_ID} - {emotion} ')
    plt.ylabel('frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    
    print(freq_table)
    return freq_table        


emotion_time_analize('C:\\Users\\Lenovo\\Desktop\\week3.csv','joy',521698,'weekday')
