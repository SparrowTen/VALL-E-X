from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from utils.prompt_making import make_prompt

import os

# make_prompt(name="ayaka_prompt", audio_prompt_path="D:/逢甲大學/畢業專題/V33_Merged_Chinese_Wav/Merged_Chinese_Wav/VO_AQ/VO_ayaka/vo_DQAQ004_4_ayaka_04.wav")
# preload_models()
# audio_array = generate_audio(text_prompt, prompt="ayaka_prompt")
# write_wav("./result/ayaka_cloned.wav", SAMPLE_RATE, audio_array)

if __name__ == '__main__':
    raw_audio_dir = "D:/逢甲大學/畢業專題/voice_data/「博士」/"
    filelist = list(os.walk(raw_audio_dir))[0][2]
    preload_models()
    #print(filelist[3])
    #make_prompt(name="博士_prompt", audio_prompt_path=f"{raw_audio_dir}{filelist[3]}",transcript=f"{raw_audio_dir}{filelist[2]}")
    count = 0
    num = 0
    for filename in filelist:
        print(filename)
        print(f"目前筆數:{num}/{len(filelist)}")
        num += 1
        if filename.endswith('.lab'):
            with open(f"{raw_audio_dir}{filename}" , 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
                #print(f"File name: {raw_audio_dir}{filename}")
                audio_array = generate_audio(text, prompt="博士_prompt",language='ja')
                write_wav(f"./result/博士/博士_cloned{count}.wav", SAMPLE_RATE, audio_array)
                count += 1