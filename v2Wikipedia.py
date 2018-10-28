import wikipedia
import wolframalpha
app_id = "L4RJL5-LXGEWXRRAH"
while True:
    input = raw_input("Question: ")
    try:
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        print wikipedia.summary(input, sentences = 2)
