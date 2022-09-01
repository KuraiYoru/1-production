from django.shortcuts import render


def my_example(requests):
    return render(requests, 'example/new.html')