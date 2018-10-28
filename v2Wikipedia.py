import wikipedia
import wolframalpha
app_id = "XXXXX-XXXXXXXXXX"
while True:
    input = raw_input("Question: ")
    try:
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        print wikipedia.summary(input, sentences = 2)
