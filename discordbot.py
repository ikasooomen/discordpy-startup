from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# APEXに関する配列
randomweapons = ["ウィングマン", "マスティフ", "モザンビーク", "R99", "R301", "P2020", "モザンビーク", "EVA8", "ハボック", "Lスター", "オルタネータ", "RE45", "ヘムロック", "フラットライン", "スピットファイア", "プラウラー", "トリプルテイク", "ロングボウ", "センチネル", "チャージライフル"]
randomkingscanyon = ["スラムレイク", "ランオフ", "ザ・ピット", "バンカー", "航空基地", "ガントレット", "サルベージ", "マーケット", "水処理施設", "ザ・ケージ", "キャパシター", "砲台", "収容所", "研究所", "ハイドロダム", "リパルサー", "沼沢", "ザ・リグ"]
randomworldsedge = ["試練", "掘削場", "ミラージュボヤージュ", "スカイフック", "溶岩溝", "ハーベスター", "火力発電所", "ザ・ツリー", "仕分け工場", "ザ・ドーム", "ラバシティ", "間欠泉", "列車庫", "調査キャンプ", "製錬所", "フラグメントイースト", "フラグメントウエスト", "展望", "エピセンター"]
randomlegends = ["レイス", "オクタン", "ミラージュ", "コースティック", "バンガロール", "パスファインダー", "ライフライン", "ジブラルタル", "ブラッドハウンド", "ワットソン", "クリプト", "レヴナント", "ローバ"]
iikaesi = ["は？死ねよ", "うんち^q^", "トイレットペーパーって美味しいよね！", "お前...誰だ？", "もしもしポリスメン？", "お前童貞臭いぞ...", "ﾃﾞｭﾌﾃﾞｭﾌwww"]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
# APEXランダム    
@bot.command()
async def weapons(ctx):
    await ctx.send(random.sample(randomweapons, 2))
@bot.command()
async def kc(ctx):
    await ctx.send(random.choice(randomkingscanyon) + "に行け！")
@bot.command()
async def we(ctx):
    await ctx.send(random.choice(randomworldsedge) + "に行け！")
@bot.command()
async def legends(ctx):
    await ctx.send(random.choice(randomlegends) + "を使え！")   
    
@bot.command()
async def talk(ctx):
    await ctx.send(random.choice(iikaesi))       

bot.run(token)
