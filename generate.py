from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from utils.prompt_making import make_prompt
import os


# from opencc import OpenCC
# cc = OpenCC('s2twp')
# if  __name__ == '__main__':
#     # download and load all models
#     preload_models()
#     raw_audio_dir = "D:/逢甲大學/畢業專題/voice_data/「博士」-zh/"
#     with open(f"{raw_audio_dir}vo_LLZAQ001_12_dottore_02.lab" , 'r', encoding='utf-8') as f:
#         text_prompt = f.read()
#         print("原始文本: " + text_prompt)
#         text_prompt = cc.convert(text_prompt)
#         print("轉換後: "+text_prompt)

#         #製作聲音特徵
#         make_prompt(name="博士-zh_prompt", audio_prompt_path=f"{raw_audio_dir}vo_LLZAQ001_12_dottore_02.wav",transcript=text_prompt)

#         #生成音訊
#         audio_array = generate_audio(text_prompt, prompt="博士-zh_prompt")

#         write_wav("./result/test_cloned.wav", SAMPLE_RATE, audio_array)


#英文
if __name__ == '__main__':
    preload_models()
    raw_audio_dir = "D:/逢甲大學/畢業專題/voice_data/「博士」-zh/"
    with open(f"D:/逢甲大學/畢業專題/voice_data/「博士」-en/vo_LLZAQ001_12_dottore_07.lab" , 'r', encoding='utf-8') as f:
        #製作聲音特徵
        text_prompt = f.read()
        make_prompt(name="博士-en_prompt", audio_prompt_path="D:/逢甲大學/畢業專題/voice_data/「博士」-en/vo_LLZAQ001_12_dottore_07.wav",transcript=text_prompt)

    with open(f"{raw_audio_dir}vo_LLZAQ001_12_dottore_07.lab" , 'r', encoding='utf-8') as f:
        text_prompt = f.read()
        print("原始文本: " + text_prompt)

        #生成音訊
        audio_array = generate_audio(text_prompt, prompt="博士-en_prompt")
        write_wav("./result/test_cloned-crossLingual-zh2en.wav", SAMPLE_RATE, audio_array)