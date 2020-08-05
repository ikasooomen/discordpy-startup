import random

kuji=["大吉", "中吉", "小吉", "吉", "凶", "大凶", "トイレットペーパー吉", "いかそーめん吉", "うん吉"]

dai=["最高の一日になるね！！！",
     "みんなから好かれるよ！！",
     "今日は宝くじ当たるんじゃね？"
     ]
tyu=["まぁまぁええんやない？（煽り）",
     "今日デートしない？"
    ]
syo=["微妙やな...強く生きろよ",
     "頭上注意ね、しょんべんかけられるぞ"
    ]
kit=["おっ...。おっ...？",
     "ワンちゃん今日便秘解消されるかも...！？"
    ]
kyo=["だっさｗｗｗｗ",
     "犬の糞ついてね？クセェぞ。"
    ]
dak=["うわｗｗｗｗｗ草ｗｗｗｗｗｗ",
     "おまｗｗｗｗなにｗｗｗｗ出してんのｗｗｗｗださｗｗｗｗｗ"
    ]
til=["今日の晩飯はトイレットペーパーだぞ！やったね！",
     "お前のトイレットペーパーにうんこ混ぜといたぞ！"
    ]
ika=["ｲｶﾞｿﾞｫｫｫｫｫｫ~~~ﾒｪｪｪｪ~~~ﾝﾝ////",
     "君のことがｗｗｗｗﾃﾞｭﾌｗｗｗﾁｭｷｗｗｗｗｗ"
    ]
unk=["うんこ食え",
     "うんこウメェなこれぇ"
    ]

def omi():
  unsei=random.choice(kuji)
  if unsei=="大吉":
     msg=random.choice(dai)
     return "今日の運命は「"+unsei+"」："+ msg
     
  elif unsei=="中吉":
     msg=random.choice(tyu)
     return "今日の運命は「"+unsei+"」："+ msg 
  elif unsei=="小吉":
     msg=random.choice(syo)
     return "今日の運命は「"+unsei+"」："+ msg
  elif unsei=="吉":
     msg=random.choice(kit)
     return "今日の運命は「"+unsei+"」："+ msg 
  elif unsei=="凶":
     msg=random.choice(kyo)
     return "今日の運命は「"+unsei+"」："+ msg
  elif unsei=="大凶":
     msg=random.choice(dak)
     return "今日の運命は「"+unsei+"」："+ msg
  elif unsei=="トイレットペーパー吉":
     msg=random.choice(til)
     return "今日の運命は「"+unsei+"」："+ msg
  elif unsei=="いかそーめん吉":
     msg=random.choice(ika)
     return "今日の運命は「"+unsei+"」："+ msg
  elif unsei=="うん吉":
     msg=random.choice(unk)
     return "今日の運命は「"+unsei+"」："+ msg
