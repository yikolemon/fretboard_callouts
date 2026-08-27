import asyncio
import os
import edge_tts

VOICE_ZH = "zh-CN-XiaoxiaoNeural"
VOICE_EN = "en-US-JennyNeural"
OUT = "audio"
os.makedirs(OUT, exist_ok=True)


async def gen(text, voice, name):
    path = os.path.join(OUT, name)
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(path)
    print(f"generated {path}  ({text} @ {voice})")


async def main():
    # 弦号：中文音色念「一弦」~「六弦」
    nums = {
        "1": "一弦",
        "2": "二弦",
        "3": "三弦",
        "4": "四弦",
        "5": "五弦",
        "6": "六弦",
    }
    for k, v in nums.items():
        await gen(v, VOICE_ZH, f"{k}.mp3")

    # 自然音名：英文音色念字母
    for n in ["C", "D", "E", "F", "G", "A", "B"]:
        await gen(n, VOICE_EN, f"{n}.mp3")

    # 升号音：英文音色念「X sharp」
    for n in ["C", "D", "F", "G", "A"]:
        await gen(f"{n} sharp", VOICE_EN, f"{n}s.mp3")


asyncio.run(main())
