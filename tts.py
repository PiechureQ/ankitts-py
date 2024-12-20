import os
from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

ELEVEN_API_KEY = os.getenv('ELEVEN_API_KEY')

dont_generate = False

client = ElevenLabs(
    # Defaults to ELEVEN_API_KEY or ELEVENLABS_API_KEY
    api_key=ELEVEN_API_KEY,
)


def generate_tts_for_cards(cards):
    print("Generate tss for cards")
    for card in cards:
        if dont_generate is False:
            print("generowanie {name}".format(name=card[0]))
            generate_tts(card[2], card[0])
        card[4] = "[sound:{name}.mp3]".format(name=card[0])

    return cards


def generate_tts(text, file):
    file_name = "generated/{name}.mp3".format(name=file)
    if dont_generate is False:
        audio = client.generate(
            text=text,
            model="eleven_multilingual_v2",
            voice=Voice(
                # Radio
                voice_id="v1jVu1Ky28piIPEJqRrm",
                # Grandfather
                # voice_id="5ON5Fnz24cnOozEQfGAm",
                # June
                # voice_id="3MTvEr8xCMCC2mL9ujrI",
                settings=VoiceSettings(
                    stability=0.75,
                    similarity_boost=0.8,
                    style=0.0,
                    use_speaker_boost=True
                )
            )
        )
        save(audio, file_name)
    return file_name
