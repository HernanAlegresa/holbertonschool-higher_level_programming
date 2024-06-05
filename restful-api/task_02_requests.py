#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    """
    Envía una solicitud GET, imprime el código de estado,
    analiza y muestra los títulos de las publicaciones.
    """
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for titles in posts:
            print(titles['title'])


def fetch_and_save_posts():
    """
    Envía una solicitud GET, analiza los datos JSON y
    guarda los datos en un archivo CSV.
    """
    
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            data = [{'id': post['id'], 'title': post['title'], 'body': post['body']}]

        with open('posts.csv', 'w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            csv_writer.writeheader()
            csv_writer.writerows(data)
