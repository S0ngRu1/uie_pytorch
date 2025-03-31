from uie_predictor import UIEPredictor
from pprint import pprint
import json

def read_json(path: str):
    with open(path, 'r') as f:
        data = json.loads(f.read())
    return data


def contains_chinese(text):
    for char in text:
        if '\u4e00' <= char <= '\u9fff' or \
           '\u3400' <= char <= '\u4dbf' or \
           '\u20000' <= char <= '\u2a6df' or \
           '\u2a700' <= char <= '\u2b73f' or \
           '\u2b740' <= char <= '\u2b81f' or \
           '\u2b820' <= char <= '\u2ceaf' or \
           '\u2ceb0' <= char <= '\u2ebef' or \
           '\u30000' <= char <= '\u3134f':
            return True
    return False


# schema = ['时间', '选手', '赛事名称'] 
# ie = UIEPredictor(model='uie-base', schema=schema)
schema = ['国家', '事件', '时间', '地点', '结果', '主要人物', '机构','物品','动作','主体','城区']

ocr_datas = read_json("/home/caisongrui/Workspace/DeepLearning/data/CFND_dataset/ocr_data_val.json")
results = []
for index, ocr_data in enumerate(ocr_datas):
    try:
        print(f"正在处理index: {index}")  
        ie = UIEPredictor(model='uie-base', schema=schema)
        result = ie(ocr_data['title'])
        title_ner = [item['text'] for key in result[0] for item in result[0][key]]
        plain_text_ner = []
        if contains_chinese(ocr_data['plain_text']):
            result = ie(ocr_data['plain_text'])
            plain_text_ner =  [item['text'] for key in result[0] for item in result[0][key]]
        
        results.append({
                "index": index,
                "title_ner": title_ner,
                "plain_text_ner": plain_text_ner
            })
    except Exception as e:
        print(f"Error: {e}")
        continue

# 将所有结果保存为 JSON 文件
with open('/home/caisongrui/Workspace/DeepLearning/data/CFND_dataset/ner_data_val_uie.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

