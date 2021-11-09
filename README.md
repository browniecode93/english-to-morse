# english-to-morse
A micro service app that translate English message to Morse code and publish the message to the queue.

## Built With

* Django Rest Framework
* Flask
* RabbitMQ

<!-- GETTING STARTED -->
## Getting Started

Clone the repo in your local machine.

### Prerequisites

* Install Docker Desktop

<!-- USAGE EXAMPLE -->
## Usage

- cd admin and run docker-compose up
- cd consumer and run docker-compose up

CREATE message:
 POST http://localhost:8000/api/message including your message as 
 {
    "eng_msg": "HOW ARE YOU TODA?"
 }
 Response will be the base64 encoded message and Morse code

LIST messages:
GET http://localhost:8000/api/message will list all the messages that have been sent to the server
Response will be the base64 encoded messages and Morse codes

GET a message:
GET http://localhost:8000/api/message/id
Response will be the base64 encoded message and Morse code

DELETE a message:
DELETE http://localhost:8000/api/message/id

Each message will be sent to the consumer service via RabbitMQ, you will be able to see it on docker log each time you create a message

![alt text](https://ibb.co/fxsPKv5)
![alt text](https://ibb.co/TrJ6FbM)
