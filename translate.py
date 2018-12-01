from watson_developer_cloud import LanguageTranslatorV3
import os

WATSON_KEY2 = os.getenv('WATSON_KEY2', None)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey=WATSON_KEY2,
    url='https://gateway.watsonplatform.net/language-translator/api'
)

#翻訳
def translate(text):
    language = language_translator.identify(text).get_result()["languages"][0]["language"]
    if language == "ja":
        model_id = language + '-en'
    elif language == "en":
        model_id = language + '-ja'
    else:
        model_id = language + '-en'
        text = language_translator.translate(text=text,model_id=model_id).get_result()["translations"][0]["translation"]
        model_id = 'en-ja'
    return language_translator.translate(text=text,model_id=model_id).get_result()["translations"][0]["translation"]

#言語特定
def language_identify(text):
    return language_translator.identify(text).get_result()["languages"][0]["language"]