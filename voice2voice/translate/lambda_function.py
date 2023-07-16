import translate
from translate import Translator
import json

def lambda_handler(event, context):
    # TODO implement
    translator= Translator(to_lang="en", from_lang="zh")
    translation = translator.translate("你好")
    print(translation)

    return {
        'statusCode': 200,
        'body': translation
    }

lambda_handler({},{})