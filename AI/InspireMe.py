import openai
import schedule
import time

Mo=[""]

def Motivate():
	openai.api_key = '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'
	messages = [ {"role": "system", "content":
			"You are an intelligent assistant."} ]
	
	message = "Write a quote"
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	chat['choices'][0]['message']['content']
	reply = chat.choices[0].message.content
	if reply in Mo:
		Motivate()
	else :
		Mo.append(reply)
	print(reply)
	Voice(reply)
	Notify(reply)

def Voice(reply):
	from gtts import gTTS
	import os
	language = 'en'
	myobj = gTTS(text=reply, lang=language, slow=False)
	myobj.save("InspireMe.mp3")
	os.system("InspireMe.mp3")

def Notify(reply):
	from plyer import notification
	if __name__=="__main__":

		notification.notify(
			title = "InspireMe",
			message= reply ,
		
			timeout=3
		)
		time.sleep(7)


schedule.every(4).hours.do(Motivate)
schedule.every().day.at("08:30").do(Motivate)


while True:
    schedule.run_pending()
    time.sleep(1)