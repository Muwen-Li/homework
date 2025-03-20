import pandas as pd
from datetime import datetime
import jieba
def document_shopID_time(df,shopID,time_unit='day'):
    documents={}
    if shopID in df['shopID'].values:
        group=df[df['shopID']==shopID]
        shop_documents={}#键是shopID,值是以时间组合为键，评论为值的字典。
        
        if time_unit=='day':
            for(year,month,day),day_group in group.groupby(['year','month','weekday']):#按照（特定的索引）分组
                combined_comment=' '.join(day_group['cus_comment'].dropna().astype(str))#拼接同意索引组合下的字符串
                shop_documents[(year,month,day)]=combined_comment#形成字典。
        elif time_unit=='month':
            for(year,month),month_group in group.groupby(['year','month']):
                combined_comment=' '.join(month_group['cus_comment'].dropna().astype(str))
                shop_documents[(year,month,day)]=combined_comment
        elif time_unit=='year':
            for year,year_group in group.groupby('year'):
                combined_comment=' '.join(year_group['cus_comment'].dropna().astype(str))
                shop_documents[year]=combined_comment
        
        documents[shopID]=shop_documents

    return documents

