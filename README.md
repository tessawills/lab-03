# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Tessa Wills
- Caroline Dworken

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
https://aws.amazon.com/what-is/restful-api/ 
RESTful APIs are scalable because the servers are stateless, and they do not store information related to requests that clients have made in the past. This means that it is a more efficient system and can be scaled more easily. 


Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

The mail server acts as a mail service and provides the following information to the client: the mail ID, the recipient of the mail, the sender of the mail, and the contents of the messages/mail. It can also do some simple searching of all the mail it has on the server, and provide a list of all of the information listed above for the mail that was sent or received to a particular user. 

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method? 

We did not use the “POST” method to send data in our mail server, so if we wanted to use that then we could reconfigure the “send” command we use so that we can use POST instead, since it serves a similar purpose of sending information to the server. 
We also did not use an authentication method in our mail server, so it is not particularly secure. If we wanted to make it more secure, or have an easier way of tracking users, then we could set up our server to use API keys or another authentication method. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

API keys are useful for two main reasons: one, from a security standpoint they help the API authenticate who is accessing the server, and two, from a very practical standpoint, they help the API keep track of different users and their permissions to access different information / services. This makes it easy for people who make APIs to charge for their services, by giving clients API keys when they purchase them, which gives them access to specific pieces of information / services that they provide, and locks them out of others. They also make it easy to track different users, the requests that they make, the permissions they have, and any other information that may be useful. 

Information taken from: https://blog.hubspot.com/website/api-keys 

BONUS code is in the repo under “jokes.py”

