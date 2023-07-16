import translate
from translate import Translator
import json

def lambda_handler(event, context):
    # TODO implement
    translator= Translator(to_lang=event["to_lang"], from_lang=event["from_lang"])
    translation = translator.translate(event["msg"])

    print("from_lang: ", event["from_lang"])
    print("to_lang: ", event["to_lang"])
    print("msg: ", event["msg"])
    print("translation: ", translation)

    return {
        'statusCode': 200,
        'body': translation
    }