from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
from collections import Counter


class Handler(SimpleHTTPRequestHandler):

        def do_GET(self):
            SimpleHTTPRequestHandler.do_GET(self)
            self.wfile.write(b"Hello there!")

        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            #reading receiving data
            content_length = int(self.headers['Content-Length']) 
            post_data = self.rfile.read(content_length)  
            

            #output
            response_body = {"wordCount":"" , "letters":"" , "longest":"" , "avgLength":"" , "duration":"" , "medianWordLength":"" , "medianWord":"" ,"mostCommon":"", "language":""}

            #to fix punctuation
            punctuation = {"text=":""    ,    "+":" "    ,   "%2C":","    ,     "%E2%80%99":"'"    ,    "%0A":"\n"     ,   "%27":"'"    ,   "%29":")"   ,    "%28":"("    ,    ".":" "}
            post_data = post_data.decode("utf-8")
            for x in range(9):                    
                post_data = post_data.replace(list(punctuation.keys())[x],list(punctuation.values())[x])
            
            
            temp = post_data

            #Word count
            for x in range(2,9):
                if list(punctuation.values())[x] == " ":
                    continue
                temp = temp.replace(list(punctuation.values())[x],"")
            wordCount = len(temp.split())
            wordCount = str(wordCount)
            temp = post_data
            response_body.update({"wordCount":wordCount})




            #Number of Letters
            for x in range(9):
                if list(punctuation.values())[x] == " ":
                    continue
                temp = temp.replace(list(punctuation.values())[x],"")
            letters = len(temp)
            letters = str(letters)
            temp = post_data
            response_body.update({"letters":letters})



            #Longest word
            for x in range(2,9):
                if list(punctuation.values())[x] == " ":
                    continue
                temp = temp.replace(list(punctuation.values())[x]," ")
            longest = max(temp.split(),key=len)
            longest = str(longest)
            temp = post_data
            response_body.update({"longest":longest})



            #Average word length
            sum = 0
            for x in range(2,9):
                if list(punctuation.values())[x] == " ":
                    continue
                temp = temp.replace(list(punctuation.values())[x]," ")
            for x in temp.split():
                sum+=len(x)
            avgLength = sum/len(temp.split())
            avgLength = str(avgLength)
            temp = post_data
            response_body.update({"avgLength":avgLength})



            #Reading Duration in Seconds
            response_body.update({"duration":str(int(wordCount)*60)})



            #Median word
            temp = temp.split()
            medianWord = temp[(int(wordCount)-1)//2]
            temp = post_data
            response_body.update({"medianWord":medianWord})



           #Median word length
            response_body.update({"medianWordLength":str(len(medianWord))})

           #Top 5 most common words
            temp = temp.split()
            counter = Counter(temp)
            temp = post_data
            response_body.update({"mostCommon":str(counter.most_common(5))})
            

            for x,y in response_body.items():
                self.wfile.write(x.encode("ascii")+b":"+y.encode("ascii")+b"\n")
                self.wfile.write(b"\n")
            
            return



def run(server_class=HTTPServer, handler_class=Handler,server_address = ('', 8080)):
    httpd = server_class(server_address, handler_class)
    print("*******[SERVER IS ONLINE]*******")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

