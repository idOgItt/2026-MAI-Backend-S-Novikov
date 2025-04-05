#! /usr/bin/env python

import os
import sys

import boto3

def main():
    access_key_id = os.environ.get('ACCESS_KEY_ID')
    secret_key_id = os.environ.get('SECRET_KEY_ID')
    bucket_name = os.environ.get('BUCKET_NAME')
    session = boto3.session.Session()
    s3_client = session.client(service_name='s3', aws_access_key_id=access_key_id, \
                               aws_secret_access_key=secret_key_id,  endpoint_url='http://hb.bizmrg.com')
    print('Клиент для s3 создан успешно!')
    content = open('200px-Cat03.jpg', 'rb').read()
    key = 'mai/cat.jpg'
    s3_client.put_object(Bucket=bucket_name, Key=key, Body=content)
    print('Отправили на s3-сервер')
    url = s3_client.generate_presigned_url(
                                            'get_object',
                                            Params = {
                                                'Bucket': bucket_name,
                                                'Key': key
                                            },
                                            ExpiresIn=3600
    )
    print(f"URL для картинки с котиком: {url}")

if __name__ == "__main__":
    main()
