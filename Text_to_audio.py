from gtts import gTTS

# Define the script
script = """
Technology defines the world we live in. It powers our devices, drives our innovations, and shapes the future.
But for many, the potential of technology remains just out of reach. At Pritech Vior Camp, we believe it’s time to change that.

Pritech Vior Camp isn’t just a place to learn—it’s a movement. A place where curiosity meets opportunity. Where individuals are empowered to understand, create, and innovate.
"""

# Generate the audio using 'en-us' (English - US, which may use a male voice depending on the locale)
audio = gTTS(text=script, lang='en', slow=False)

# Save the file
audio.save("Pritech_Vior_Camp_Introduction.mp3")

print("Audio file saved as Pritech_Vior_Camp_Introduction.mp3")
