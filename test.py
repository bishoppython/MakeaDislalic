import assemblyai as aai
import time

# Sua chave de API da AssemblyAI
aai.settings.api_key = "33e1b036f3864beea9ff733fabb28e64"

# Inicializando o transcritor
transcriber = aai.Transcriber()

# Caminho do arquivo local de áudio
audio_file = rf"D:\MESTRADO\PESQUISA\eu.ogg"

# Configuração de transcrição (com labels de falantes)
config = aai.TranscriptionConfig(speaker_labels=True)

# Solicitar transcrição
transcript = transcriber.transcribe(audio_file, config)

# Função para esperar a transcrição ser concluída
def wait_for_transcription(transcript):
    while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
        print(f"Transcription status: {transcript.status}. Waiting for completion...")
        time.sleep(5)  # Aguardar 5 segundos antes de checar novamente
        transcript = transcriber.get_transcription(transcript.id)  # Verificar status atualizado
    return transcript

# Verificar o status e aguardar a conclusão
transcript = wait_for_transcription(transcript)

# Verificar se houve erro na transcrição
if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcription failed: {transcript.error}")
    exit(1)

# Imprimir o texto completo da transcrição
print("Texto Transcrito:")
print(transcript.text)

# Verificar e imprimir os falantes e suas falas
if transcript.utterances:
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")
else:
    print("Nenhum 'utterance' encontrado.")
