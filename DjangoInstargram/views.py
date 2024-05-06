from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("겟으로 출력")
        return render(request, "instargram/main.html")

    def post(self, request):
        print("포스트로 출력")
        return render(request, "instargram/main.html")
