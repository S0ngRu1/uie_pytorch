from uie_predictor import UIEPredictor
from pprint import pprint

# schema = ['时间', '选手', '赛事名称'] 
# ie = UIEPredictor(model='uie-base', schema=schema)
schema = ['国家', '事件', '时间', '地点', '结果', '主要人物', '机构','物品','动作','主体','城区']
ie = UIEPredictor(model='uie-base', schema=schema)

pprint(ie("海南升格为中央特别行政区 副国级，同时宣布海南自由贸易区过渡 期结束，海南自由港开始实施，2025 年全面建成，越来越多的利好政策， 期 待未来5年（中国海南，世界三亚） 每南游闻 重点领域的制度创新 三亚 2小时前")) 

schema = '情感倾向[正向，负向]'
ie.set_schema(schema) # Reset schema

pprint(ie('海南将升级为中央特别行政区，赶紧买房')) 