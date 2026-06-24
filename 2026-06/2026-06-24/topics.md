# 2026-06-24 选题清单

> 来源：`topics/2026-06-24/selected.json`  
> Run ID：`2026-06-24_0231`  
> 生成时间：2026-06-24T02:32:13.093413+00:00

---

## 01 [92] 九年了，中国超算重回世界第一：深圳'灵晟'纯CPU冲上2.2 ExaFLOPS登顶TOP500

- **slug**: `lingsheng-cpu-top500-china-supercomputer`
- **分类**: 科技
- **独立 review**: [90] keep
- **写作角度**: 不写'厉害了我的国'式跑分复述,而从'封锁倒逼出CPU路线、这条路反而更难被制裁'这个产业逻辑切入,叠加图灵奖得主Dongarra背书+AI4Science新架构
- **写作思路** [串点+换轴]:
    - 核心结论 D: GPU出口被卡死,中国超算被逼着走了一条纯CPU+片上矩阵加速的冷门路线,结果这台没有一颗GPU的机器反而登顶全球、还顺手拿下最看重真实应用的HPCG第一——封锁没挡住,反而逼出了一条用全可控国产部件就能堆到顶尖的、更难被二次制裁的技术栈。
    - 串点: 灵晟2.198 EFlops登顶,比第二名El Capitan快20%+ + 纯CPU架构(1379万核/304核LX2,无GPU),首台CPU-only破2 EFlops + GPU/先进制程被出口管制卡住是这条路线的起点 + 图灵奖得主Dongarra(TOP500联合创始人)亲口'他们用不依赖GPU的系统超过了我们' + 同时拿下HPCG(真实应用)第一,但HPL-MxP(混合精度/AI向)仅第四——长板短板都清楚
    - 换轴: 大家都在写'中国重回第一/算力多猛'的民族叙事,本篇换到'技术路线'轴:为什么是纯CPU、这条路的代价与好处、它在AI时代意味着什么
    - 反直觉: 表面是一次扬眉吐气的速度登顶,实际是被封锁逼出来的'非主流架构',且它的优势恰恰在于'全部部件可国产、更难被再次卡脖子'
    - 增量在哪: 读者读完能分清'登顶'背后的两件事:一是封锁如何反向塑造了技术路线,二是纯CPU路线在科学计算赢了、在AI混合精度上仍有差距——既不妄自菲薄也不盲目吹,看懂这台机器到底强在哪、短在哪
- **关键数据**: 2.2, 500
- **合规提示**: 见 rules/compliance.md
- **素材链接**:
  - https://www.top500.org/news/lineshine-debuts-no-1-top500-enters-new-global-exascale-era/
  - https://www.top500.org/lists/top500/2026/06/
  - https://www.datacenterdynamics.com/en/news/lineshine-all-cpu-chinese-supercomputer-named-worlds-most-powerful/
  - https://news.cctv.com/2026/06/24/ARTIzgNeSyRyqMhNxuDNorwy260623.shtml

## 02 [85] 企业第一次'开新项目先选Claude'：5万家公司刷卡数据显示Anthropic反超OpenAI——反超点不在聊天，在编程

- **slug**: `anthropic-enterprise-passes-openai-claude`
- **分类**: 商业
- **写作角度**: 不写谁估值高/谁先IPO，而从'企业刷卡数据'这个被忽略的真实采购信号切入，讲消费冠军≠企业冠军
- **写作思路** [换轴]:
    - 核心结论 D: 衡量AI谁赢，收入看的是'过去',而企业'开新项目先掏谁'看的是'下一个十年'——Ramp的刷卡数据显示这个先行指标第一次翻盘:Anthropic靠'长上下文+指令忠实+能进生产'补上了OpenAI忙着做消费花活时漏掉的洞，反超恰恰发生在编程这个最吃可靠性的场景。
    - 串点: Ramp指数:Anthropic 34.4% vs OpenAI 32.3%(5万+公司账单) + Anthropic新客户70%首选、一年采用率翻两番 + 约16%公司同时给两家付费(多模型栈) + 反超集中在coding场景 + 隐患:token计费在预算收紧时招成本审查、春季现可靠性投诉
    - 换轴: 大家都盯估值/IPO/融资额，本篇换到'企业刷卡采购数据'这个真实需求信号
    - 反直觉: 表面OpenAI总收入仍领先，实际'下一个项目选谁'的话语权已经交给Claude
    - 增量在哪: 读者拿到一个看AI竞争的新尺子(企业首选率>收入),并理解'消费爆款'和'企业默认'是两件事
- **关键数据**: 5万
- **合规提示**: 见 rules/compliance.md
- **素材链接**:
  - https://www.forbes.com/sites/sandycarter/2026/06/05/claude-becomes-the-enterprise-favorite-as-anthropic-passes-openai/
  - https://thehill.com/policy/technology/5900111-anthropic-valuation-openai-race/

## 03 [83] 模型打不过就用'入口'打：开源战略撤退后，扎克伯格把翻身赌注押在'让27亿人把Facebook当搜索引擎'

- **slug**: `meta-entry-point-weaponize-search`
- **分类**: 产品
- **写作角度**: 不写'Meta又出AI功能',而从'模型拼不过就改打自己最强的分发牌'这个竞争策略切入
- **写作思路** [串点+换轴]:
    - 核心结论 D: Meta在'比模型'这条赛道已经认输(Llama4 flop、放弃开源、闭源转Muse Spark);它的翻身策略是换战场——不跟OpenAI/Google拼模型强弱，而是把自己唯一无可比拟的资产(27亿人的分发入口)武器化，让Facebook搜索变成答题机，用流量正面切Google的搜索蛋糕。
    - 串点: Llama 4家族flop、Meta大体放弃开源战略 + $143亿投Scale AI、挖来Alexandr Wang建Superintelligence Labs + 闭源Muse Spark成首个MSL模型 + Facebook Search上线AI Mode直接答题(抓Groups/Reels公开内容) + Morgan Stanley:留存10亿用户+变现10%查询=年入百亿美元 + Meta股价YTD仍-8%、投资人对烧钱观望
    - 换轴: 大家都写'Meta又加了个AI功能',本篇换到'打不过模型就改打入口'的竞争策略
    - 反直觉: 表面是搜索功能更新，实际是Meta承认正面拼模型已落后、改用分发入口迂回包抄Google
    - 增量在哪: 读者get到的是大厂AI竞争的另一种打法(用分发而非模型取胜),以及Meta把劣势(模型弱)绕成优势(入口强)的逻辑
- **关键数据**: 27亿
- **合规提示**: 见 rules/compliance.md
- **素材链接**:
  - https://www.forbes.com/sites/maryroeloffs/2026/06/15/facebook-launches-search-engine-ai-tool-that-could-make-meta-10-billion-a-year-analyst-says/

## 04 [84] 司法部下场救马斯克：为保Grok运转，要法院驳回黑人社区的污染诉讼——理由是Grok在伊朗战4天打了2000个目标

- **slug**: `doj-grok-xai-memphis-warmachine`
- **分类**: 商业
- **独立 review**: [79.5] keep
- **写作角度**: AI'卖铲子/算力'之外的另一面：当一个商用聊天机器人被政府定性为战争武器+战略资产，环境正义、公民诉讼权、AI军事化三件事在一个法庭上对撞。不是马斯克造芯(06-22已写)，是马斯克的AI被国家收编当武器。
- **写作思路** [串点+换轴]:
    - 核心结论 D: 当一个商用聊天机器人被政府正式写进'战争关键基础设施'，它就不再只是消费品——xAI孟菲斯数据中心的排污官司之所以惊动司法部下场要求驳回，真正原因是Grok已被国防部认定为战争资产，于是环境正义、公民诉讼权、AI军事化三件本不相干的事第一次在同一个法庭对撞。
    - 串点: NAACP告xAI孟菲斯数据中心无证排污、紧挨黑人社区 + 司法部罕见介入要求驳回 + 理由是国防部作证Grok让美军96小时打2000个目标 + 私有聊天机器人第一次被定性为战争关键基础设施
    - 换轴: 大家写AI都在卖铲子/算力/估值，本篇换到'AI军事化+国家收编'这个轴——不是马斯克造芯,是马斯克的AI被国家当武器收编后,连带豁免了民事追责
    - 反直觉: 表面是一桩环保排污诉讼,实际是私有AI被国家武器化后、公民连告它污染的权利都被国安理由盖过
    - 增量在哪: 读者get到一条没人串起来的链:商用AI一旦被写进战争机器,它的工厂就获得了普通企业没有的法律豁免——AI军事化的代价不只在战场,在你家旁边的数据中心
- **关键数据**: 4, 2000个
- **合规提示**: 见 rules/compliance.md

## 05 [86] Oracle年内裁2.1万人，AI首次被白纸黑字写进SEC文件当裁员理由

- **slug**: `oracle-sec-filing-ai-layoffs`
- **分类**: 商业
- **独立 review**: [77.5] keep
- **写作角度**: 不是又一条裁员新闻，而是'举证责任'反转：第一份在联邦监管文件里、用法律语言承认AI=裁员的megacap。Altman/Sløk们说'零证据'，Oracle说'证据在这，盖了公章'。
- **写作思路** [换轴]:
    - 核心结论 D: AI杀岗位的争论一直卡在'拿不出证据'，Oracle这份10-K第一次把'AI导致裁员'用法律语言写进联邦监管文件、由律师在伪证罪下签字——举证责任就此反转：不再是打工人证明自己被AI取代，而是巨头自己盖章承认了。
    - 串点: Oracle 10-K原话承认AI已致裁员 + 2.1万人(13%)+遣散费18亿(去年5倍) + 砍人省下的钱全砸进AI数据中心(capex+162%) + Altman/经济学家整年说'零证据'
    - 换轴: 大家都把它当'又一条裁员新闻'写惨状，本篇从'举证责任反转'这个法律/认识论角度切入——证据这次不在宏观数据里，在SEC公章上
    - 反直觉: 表面是Oracle省成本裁员，实际是第一份让'AI=裁员'从口水仗变成白纸黑字法律事实的文件
    - 增量在哪: 读者读完明白：判断AI是否在杀岗位，以后不用再吵'有没有证据'，因为巨头已经自己在监管文件里承认了——而且承认的同时把省下的钱投回AI，闭环讲清了
- **关键数据**: 2.1万
- **合规提示**: 见 rules/compliance.md
