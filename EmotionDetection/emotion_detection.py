import requests
import json

def emotion_detector(text_to_analyze):
    # Configurazione dell'endpoint e degli header richiesti
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Struttura del payload JSON di input
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Invio della richiesta POST
    response = requests.post(url, json=myobj, headers=headers)
    
    # Conversione della risposta testuale (JSON) in un dizionario Python
    formatted_response = json.loads(response.text)
    
    # Estrazione del dizionario delle emozioni dalla struttura di Watson
    # La struttura tipica è: formatted_response['emotionPredictions'][0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Estrazione dei singoli punteggi
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logica per trovare l'emozione dominante
    # max(emotions, key=emotions.get) restituisce la chiave (nome emozione) con il valore più alto
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Creazione del dizionario finale richiesto dall'esercizio
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result