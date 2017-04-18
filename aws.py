import boto3

lex = boto3.client('lex-runtime')

response = lex.post_text(
    botName='HeyOffice',
    botAlias='$LATEST',
    userId='1122334455',
    sessionAttributes={},
    inputText=b'Order some craft beer'
)

print response
