# from utils.generation import SAMPLE_RATE, generate_audio, preload_models
# from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# # download and load all models
# preload_models()

# # generate audio from text
# text_prompt = """
# Hello, my name is Nose. And uh, and I like hamburger. Hahaha... But I also have other interests such as playing tactic toast.
# """
# audio_array = generate_audio(text_prompt)

# # save audio to disk
# write_wav("vallex_generation.wav", SAMPLE_RATE, audio_array)

# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)

from utils.prompt_making import make_prompt

### Alternatively, use whisper
make_prompt(name="ayaka_prompt", audio_prompt_path="D:/逢甲大學/畢業專題/V33_Merged_Chinese_Wav/Merged_Chinese_Wav/VO_AQ/VO_ayaka/vo_DQAQ004_4_ayaka_04.wav")



