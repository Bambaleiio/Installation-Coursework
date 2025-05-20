from __future__ import annotations

import re
import json
import pydantic

from yandex_cloud_ml_sdk import YCloudML


class LLMHandlerEXT:
    def __init__(self, ownerComp):
        self.ownerComp = ownerComp
        self.sdk = YCloudML(
            folder_id=ownerComp.par.Folderid.eval(),
            auth=ownerComp.par.Auth.eval()
        )


    def SendToLLM(self, text):
        if not text.strip():
            debug("Ошибка: Пустой ввод, обработка не будет выполнена.")
            return
        
        opEmotion = op('text_emotion')
        opEmotion.clear()

        opSentences = op('table_sentences')
        opSentences.clear()

        emotion = self.getEmotion(text)
        opEmotion.text = emotion

        sentences = self.generateSentences(text, self.ownerComp.par.Sentencesnum)

        for sentence in sentences.splitlines():
            sentence = re.sub("^[1-9]+:", "", sentence).strip()
            opSentences.appendRow(sentence)


        debug(sentences)

        op.StateManager.Call_Preset(emotion)
        op.CONVERTSTR.UpdateString()        


    def getEmotion(self, text) -> str:
        # emotions = ["Грусть", "Радость", "Злость", "Нейтральное", "Отвращение", "Скука"]
        # emotions = ["neutral", "fear", "anger", "calm", "sadness", "joy"]
        emotions = ["neutral", "fear", "anger", "calm", "sadness", "joy", "surprize", "disgust"]

        model = self.sdk.models.text_classifiers("yandexgpt").configure(
            task_description="определи эмоцию текста",
            labels=emotions
        )

        result = model.run(text)
        
        highestConfidence = -1
        emotion = None
        
        for prediction in result:
            if prediction.confidence > highestConfidence:
                highestConfidence = prediction.confidence
                emotion = prediction.label
                
        return emotion

        
    def generateSentences(self, text, num_sentences=1) -> str:
        systemPrompt = f"Придумай {num_sentences} предложений, сохраняя эмоцию и атмосферу. Ответь в формате: номер предложения: предложение, новая строка "
        model = self.sdk.models.completions("yandexgpt", model_version="latest")

        result = model.run(
            [ 
                {
                    "role": "system",
                    "text": systemPrompt
                },
                {
                    "role": "user", 
                    "text": text
                }
            ]
        ) 

        return result[0].text.strip()