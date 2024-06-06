from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from utils.prompt_making import make_prompt
import os
#進度條
import time
from tqdm import tqdm, trange

#簡體中文轉繁體中文
from opencc import OpenCC
cc = OpenCC('s2twp')
#中文
if __name__ == '__main__':
    raw_audio_dir = "D:/逢甲大學/畢業專題/voice_data/「博士」-zh/"
    filelist = list(os.walk(raw_audio_dir))[0][2]
    preload_models()
    print(filelist[5])
    with open(f"{raw_audio_dir}{filelist[4]}" , 'r', encoding='utf-8') as f:
        make_prompt(name="博士-zh_prompt", audio_prompt_path=f"{raw_audio_dir}{filelist[5]}",transcript=cc.convert(f.read()))
    count = 1
    # num = 0
    for filename in tqdm(filelist):
        print(filename)
        # print(f"目前筆數:{num}/{len(filelist)}")
        # num += 1
        if filename.endswith('.lab'):
            with open(f"{raw_audio_dir}{filename}" , 'r', encoding='utf-8') as f:
                text = f.read()
                print("轉換前: "+ text)
                text = cc.convert(text)
                print("轉換後: "+ text)
                #print(f"File name: {raw_audio_dir}{filename}")
                audio_array = generate_audio(text, prompt="博士-zh_prompt")#,language='zh'
                write_wav(f"./result/博士-zh/博士_cloned{count}.wav", SAMPLE_RATE, audio_array)
                count += 1

# #英文
# if __name__ == '__main__':
#     raw_audio_dir = "D:/逢甲大學/畢業專題/voice_data/「博士」-en/"
#     filelist = list(os.walk(raw_audio_dir))[0][2]
#     preload_models()
#     #print(filelist[3])
#     with open(f"{raw_audio_dir}{filelist[4]}" , 'r', encoding='utf-8') as f:
#        make_prompt(name="博士-en_prompt", audio_prompt_path=f"{raw_audio_dir}{filelist[5]}",transcript=f.read())
#     count = 0
#     num = 0
#     for filename in filelist:
#         print(filename)
#         print(f"目前筆數:{num}/{len(filelist)}")
#         num += 1
#         if filename.endswith('.lab'):
#             with open(f"{raw_audio_dir}{filename}" , 'r', encoding='utf-8') as f:
#                 text = f.read()
#                 print(text)
#                 #print(f"File name: {raw_audio_dir}{filename}")
#                 audio_array = generate_audio(text, prompt="博士_prompt",language='en')
#                 write_wav(f"./result/博士/博士-en_cloned{count}.wav", SAMPLE_RATE, audio_array)
#                 count += 1