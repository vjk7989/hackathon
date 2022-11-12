from flask import  request, Flask
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/bot', methods =['POST'])
def bot():
    user_msg = request.values.get('Body','').lower()
    #user_msg1 = request.values.get('Body', '').lower()
    bot_response = MessagingResponse()
    msg = bot_response.message()
    wish = ['hello','hi','hey']
    if user_msg in wish:
        s1 = ''' a)Visit us.
 b) Exam information (like paper pattern, mode)
 c)Previous year question papers
 d)Expected dates of Exam 
 e)Admin contact info'''
        msg.body("At your service!!\nHow may I help you?\n"+s1)

    elif "a" in user_msg:
        s1= ''' Vit-ap : https://www.google.com/maps?ll=16.496278,80.500668&z=14&t=m&hl=en&gl=US&mapclient=embed&cid=1481942445012129872
        '''
        msg.body(s1)
    elif "b" in user_msg:
        msg.body('https://freeimage.host/i/yMIXG1')
        #msg.body(s1)
    elif "c" in user_msg:
        ls1 = ["Pyhsics","Math","Chemistry","English","Aptitude"]
        ls2 = ["https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2022/06/20183622/Physics-sample-paper.pdf "+"\n\n\n",
               "https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2022/06/20183744/Maths-sample-paper.pdf "+"\n\n\n",
               "https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2022/06/20184029/English-sample-paper_wyLh37l.pdf"+"\n\n\n",
               "https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2022/06/20184529/VITEEE-2019-chemistry-Sample-Paper-1.pdf"+"\n\n\n",
               "https://cache.careers360.mobi/media/uploads/froala_editor/files/Aptitude-Sample-paper.pdf"]
        for i in range(len (ls1)):
            s1 = ls1[i] + " : \n"+ls2[i]
            msg.body(s1)

    elif "d" in user_msg:
        s1 = ''' VITEEE will be conducted between 15 and 21 April 2023 (Tentative) '''
        msg.body(s1)
    elif "e" in user_msg:
        ls1 = ["Director Admissions", "The Registrar", "VIT-AP University Admin.Office"]
        ls2 = [" admission@vitap.ac.in", "info@vitap.ac.in", " adminoffice@vitap.ac.in"]
        ls3 = ["0863 2370444", "-", "7901311658"]
        for i in range(len(ls1)):
            s1 = ls1[i]+"\nMail : "+ls2[i]+"\nContact info "+ls3[i]
            msg.body(s1)


    
    return str(bot_response)

if __name__=="__main__":
    app.run()
