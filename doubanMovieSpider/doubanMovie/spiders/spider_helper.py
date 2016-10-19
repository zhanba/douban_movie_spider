# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from doubanMovie.items import DoubanMovieItem


def parse_movie_item(self, response):
    sel = Selector(response)
    item = DoubanMovieItem()
    item['subject_id'] = response.url.split("/")[-2]
    item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
    item['year'] = sel.xpath(
        '//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
    item['cover_url'] = sel.xpath('//*[@id="mainpic"]/a/img/@src').extract()
    item['directors'] = sel.xpath(
        '//*[@id="info"]/span[1]/span[2]').xpath('string(.)').extract()
    item['writers'] = sel.xpath(
        '//*[@id="info"]/span[2]/span[2]').xpath('string(.)').extract()
    item['actors'] = sel.xpath(
        '//*[@id="info"]/span[3]/span[2]').xpath('string(.)').extract()
    genre_list = sel.xpath(
        '//*[@id="info"]/*[@property="v:genre"]/text()').extract()
    item['genres'] = '/'.join(genre_list)
    item['countries'] = sel.xpath(
        u'//*[@id="info"]/*[text()="制片国家/地区:"]/following-sibling::text()[1]').extract()
    item['languages'] = sel.xpath(
        u'//*[@id="info"]/*[text()="语言:"]/following-sibling::text()[1]').extract()
    item['release_date'] = sel.xpath(
        '//*[@id="info"]/*[@property="v:initialReleaseDate"]/@content').extract()
    item['running_time'] = sel.xpath(
        '//*[@id="info"]/*[@property="v:runtime"]/@content').extract()
    item['alias'] = sel.xpath(
        u'//*[@id="info"]/*[text()="又名:"]/following-sibling::text()[1]').extract()
    item['imdb_link'] = sel.xpath(
        u'//*[@id="info"]/*[text()="IMDb链接:"]/following-sibling::a[1]/text()').extract()
    item['rating'] = sel.xpath(
        '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
    item['rating_num'] = sel.xpath(
        '//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()
    item['summary'] = sel.xpath(
        '//*[@id="link-report"]/span[1]').xpath('string(.)').extract()
    item['tags'] = sel.xpath(
        '//*[@class="tags-body"]/*[text()]/text()').extract()
    return item

types = ["爱情", "喜剧", "动画", "剧情", "科幻", "动作", "经典", "悬疑",
         "青春", "犯罪", "惊悚", "文艺", "搞笑", "纪录片", "励志", "恐怖",
         "战争", "短片", "魔幻", "黑色幽默", "传记", "情色", "感人", "暴力",
         "动画短片", "家庭", "音乐", "童年", "浪漫", "黑帮", "女性", "同志",
         "史诗", "童话", "烂片", "cult"]

countries = [
    "安道尔",
    "阿联酋",
    "阿富汗",
    "安提瓜和巴布达",
    "安圭拉",
    "阿尔巴尼亚",
    "亚美尼亚",
    "安哥拉",
    "南极洲",
    "阿根廷",
    "美属萨摩亚",
    "奥地利",
    "澳大利亚",
    "阿鲁巴",
    "奥兰",
    "阿塞拜疆",
    "波斯尼亚和黑塞哥维那",
    "巴巴多斯",
    "孟加拉国",
    "比利时",
    "布基纳法索",
    "保加利亚",
    "巴林",
    "布隆迪",
    "贝宁",
    "圣巴泰勒米",
    "百慕大",
    "文莱",
    "玻利维亚",
    "加勒比荷兰",
    "巴西",
    "巴哈马",
    "不丹",
    "布韦岛",
    "博茨瓦纳",
    "白俄罗斯",
    "伯利兹",
    "加拿大",
    "科科斯（基林）群岛",
    "刚果（金）",
    "中非",
    "刚果（布）",
    "瑞士",
    "科特迪瓦",
    "库克群岛",
    "智利",
    "喀麦隆",
    "中国",
    "哥伦比亚",
    "哥斯达黎加",
    "古巴",
    "佛得角",
    "库拉索",
    "圣诞岛",
    "塞浦路斯",
    "捷克",
    "德国",
    "吉布提",
    "丹麦",
    "多米尼克",
    "多米尼加",
    "阿尔及利亚",
    "厄瓜多尔",
    "爱沙尼亚",
    "埃及",
    "阿拉伯撒哈拉民主共和国",
    "厄立特里亚",
    "西班牙",
    "埃塞俄比亚",
    "芬兰",
    "斐济",
    "福克兰群岛",
    "密克罗尼西亚联邦",
    "法罗群岛",
    "法国",
    "加蓬",
    "英国",
    "格林纳达",
    "格鲁吉亚",
    "法属圭亚那",
    "根西",
    "加纳",
    "直布罗陀",
    "格陵兰",
    "冈比亚",
    "几内亚",
    "瓜德罗普",
    "赤道几内亚",
    "希腊",
    "南乔治亚和南桑威奇群岛",
    "危地马拉",
    "关岛",
    "几内亚比绍",
    "圭亚那",
    "香港",
    "赫德岛和麦克唐纳群岛",
    "洪都拉斯",
    "克罗地亚",
    "海地",
    "匈牙利",
    "印尼",
    "爱尔兰",
    "以色列",
    "马恩岛",
    "印度",
    "英属印度洋领地",
    "伊拉克",
    "伊朗",
    "冰岛",
    "意大利",
    "泽西",
    "牙买加",
    "约旦",
    "日本",
    "肯尼亚",
    "吉尔吉斯斯坦",
    "柬埔寨",
    "基里巴斯",
    "科摩罗",
    "圣基茨和尼维斯",
    "朝鲜",
    "韩国",
    "科威特",
    "开曼群岛",
    "哈萨克斯坦",
    "老挝",
    "黎巴嫩",
    "圣卢西亚",
    "列支敦士登",
    "斯里兰卡",
    "利比里亚",
    "莱索托",
    "立陶宛",
    "卢森堡",
    "拉脱维亚",
    "利比亚",
    "摩洛哥",
    "摩纳哥",
    "摩尔多瓦",
    "黑山",
    "法属圣马丁",
    "马达加斯加",
    "马绍尔群岛",
    "马其顿",
    "马里",
    "缅甸",
    "蒙古",
    "澳门",
    "北马里亚纳群岛",
    "马提尼克",
    "毛里塔尼亚",
    "蒙特塞拉特",
    "马耳他",
    "毛里求斯",
    "马尔代夫",
    "马拉维",
    "墨西哥",
    "马来西亚",
    "莫桑比克",
    "纳米比亚",
    "新喀里多尼亚",
    "尼日尔",
    "诺福克岛",
    "尼日利亚",
    "尼加拉瓜",
    "荷兰",
    "挪威",
    "尼泊尔",
    "瑙鲁",
    "纽埃",
    "新西兰",
    "阿曼",
    "巴拿马",
    "秘鲁",
    "法属波利尼西亚",
    "巴布亚新几内亚",
    "菲律宾",
    "巴基斯坦",
    "波兰",
    "圣皮埃尔和密克隆",
    "皮特凯恩群岛",
    "波多黎各",
    "巴勒斯坦",
    "葡萄牙",
    "帕劳",
    "巴拉圭",
    "卡塔尔",
    "留尼汪",
    "罗马尼亚",
    "塞尔维亚",
    "俄罗斯",
    "卢旺达",
    "沙特阿拉伯",
    "所罗门群岛",
    "塞舌尔",
    "苏丹",
    "瑞典",
    "新加坡",
    "圣赫勒拿",
    "斯洛文尼亚",
    "斯瓦尔巴群岛",
    "扬马延岛",
    "斯洛伐克",
    "塞拉利昂",
    "圣马力诺",
    "塞内加尔",
    "索马里",
    "苏里南",
    "南苏丹",
    "圣多美和普林西比",
    "萨尔瓦多",
    "荷属圣马丁",
    "叙利亚",
    "斯威士兰",
    "特克斯和凯科斯群岛",
    "乍得",
    "法属南部领地",
    "多哥",
    "泰国",
    "塔吉克斯坦",
    "托克劳",
    "东帝汶",
    "土库曼斯坦",
    "突尼斯",
    "汤加",
    "土耳其",
    "特立尼达和多巴哥",
    "图瓦卢",
    "台湾",
    "坦桑尼亚",
    "乌克兰",
    "乌干达",
    "美国本土外小岛屿",
    "美国",
    "乌拉圭",
    "乌兹别克斯坦",
    "梵蒂冈",
    "圣文森特和格林纳丁斯",
    "委内瑞拉",
    "英属维尔京群岛",
    "美属维尔京群岛",
    "越南",
    "瓦努阿图",
    "瓦利斯和富图纳",
    "萨摩亚",
    "也门",
    "马约特",
    "南非",
    "赞比亚",
    "津巴布韦"
]
