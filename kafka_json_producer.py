#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# A simple example demonstrating use of JSONSerializer.

import argparse
from uuid import uuid4
from six.moves import input
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
#from confluent_kafka.schema_registry import *
import pandas as pd
from typing import List
import mysql.connector
import time
from mysql.connector import Error

print("step1")
FILE_PATH = 'SELECT * FROM demo1'
columns=['id', 'name']

API_KEY = '4H54N4V2CTGYZH3E'
ENDPOINT_SCHEMA_URL  = 'https://psrc-0xx5p.us-central1.gcp.confluent.cloud'
API_SECRET_KEY = 'nrCxLuZOu7YMKT7Gmb7y0tbtOBOuUcT6LgWGjuwk1mycY6TdOBdDG2LIqv9tfAv9'
BOOTSTRAP_SERVER = 'pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092'
SECURITY_PROTOCOL = 'SASL_SSL'
SSL_MACHENISM = 'PLAIN'
SCHEMA_REGISTRY_API_KEY = 'RCNO5F5XPGNOWHFH'
SCHEMA_REGISTRY_API_SECRET = 'zjB42uTpl2ALM56fib6KSr6TrIwVsZZOH53Uj8s5Lm+zjW07j4Amczv+O8k8Bs01'

try: 
    connection = mysql.connector.connect(
        host='localhost',
        user='your_user',
        password='your_password',
        database='your_database'
    )

except Error as e:
    print("Error while connecting to MySQL", e)
cursor = connection.cursor()
print("step2")

def sasl_conf():
    print("step3")
    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print("step4")
    return sasl_conf



def schema_config():
    print("step5")
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }


class Car:
    print("step6")   
    def __init__(self,record:dict):
        print("step15")
        for k,v in record.items():
            setattr(self,k,v)
        
        self.record=record
   
    @staticmethod
    def dict_to_car(data:dict,ctx):
        print("step14")
        return Car(record=data)

    def __str__(self):
        print("step7")
        return f"{self.record}"


def get_car_instance(file_path):
    print("step8")
    cursor.execute(file_path)
    rows = cursor.fetchall()
    df = pd.DataFrame([tuple(row) for row in rows], columns=[column[0] for column in cursor.description])
    cursor.close()
    connection.close()
    df=df.iloc[:,:]
    print(df)
    cars:List[Car]=[]
    for data in df.values:
        car=Car(dict(zip(columns,data)))
        cars.append(car)
        yield car
    print("step9")

def car_to_dict(car:Car, ctx):
    print("step10")
    """
    Returns a dict representation of a User instance for serialization.
    Args:
        user (User): User instance.
        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.
    Returns:
        dict: Dict populated with user attributes to be serialized.
    """

    # User._address must not be serialized; omit from dict
    return car.record


def delivery_report(err, msg):
    print("step11")
    """
    Reports the success or failure of a message delivery.
    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    """

    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


def main(topic):
    print("step12")
    schema_registry_conf = schema_config()
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    # subjects = schema_registry_client.get_subjects()
    # print(subjects)
    subject = topic+'-value'

    schema = schema_registry_client.get_latest_version(subject)
    schema_str=schema.schema.schema_str

    string_serializer = StringSerializer('utf_8')
    json_serializer = JSONSerializer(schema_str, schema_registry_client, car_to_dict)

    producer = Producer(sasl_conf())

    print("Producing user records to topic {}. ^C to exit.".format(topic))
    #while True:
        # Serve on_delivery callbacks from previous calls to produce()
    producer.poll(0.0)
    try:

        for car in get_car_instance(file_path=FILE_PATH):
            print(car)
            producer.produce(topic=topic,
                            key=string_serializer(str(uuid4())),
                            value=json_serializer(car, SerializationContext(topic, MessageField.VALUE)),
                            on_delivery=delivery_report)
            break
    except KeyboardInterrupt:
        pass
    except ValueError:
        print("Invalid input, discarding record...")
        pass

    print("\nFlushing records...")
    producer.flush()
print("step13")
main("car_topic")
