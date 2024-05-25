from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# download and load all models
preload_models()

text_prompt = """
这是历史的开始。 如果您想听更多，请继续。
"""
audio_array = generate_audio(text_prompt, prompt="博士_prompt")

write_wav("./result/test_cloned.wav", SAMPLE_RATE, audio_array)