"""Ushbu modul quyidagi sayt orqali turli xil quotalarni va
ularning tarjimasini chiqarib beradi"""
import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()["slip"]["advice"]
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest="uz")
print(tarjima.text)