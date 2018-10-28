import wolframalpha
app_id = "XXXXX-XXXXXXXXXX"
client = wolframalpha.Client(app_id)
my_input = raw_input("Question: ")
res = client.query(my_input)
answer = next(res.results).text 
print(answer)

