from django.contrib.auth.models import User
from django.db import DatabaseError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import App, Subscription, Plan


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createApp(request):
    try:
        appName = request.data['name']
        appDesc = request.data['description']
        userID = request.data['user_id']
    except KeyError:
        return Response({"Error": "Invalid Request Keys"}, status=406)

    try:
        appCreation = App.objects.create(
            name=appName,
            appDesc=appDesc,
            user_id=User.objects.filter(id=userID).first()
        )
        Subscription.objects.create(
            active=True,
            app_id=appCreation,
            plan_id=Plan.objects.filter(name='Free')
        )
    except DatabaseError:
        return Response({"Error": "Unable to complete request"}, status=500)

    return Response({"Success": "App Created"})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addSubscription(request):
    try:
        appID = request.data['app_id']
        userID = request.data['user_id']
        planID = request.data['plan_id']
    except KeyError:
        return Response({"Error": "Invalid Request Keys"}, status=406)

    queryset = Subscription.objects.filter(plan_id=planID, user=userID)

    if not queryset.exists():
        return Response({"Error": "Subscription already exists"}, status=404)

    else:
        if App.objects.filter(id=appID).exists():
            if Plan.objects.filter(id=planID).exists():
                Subscription.objects.create(app_id=appID, user_id=userID, plan_id=planID)
                return Response("Success")

        return Response({"Error": "Invalid subscription details"}, status=406)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateSubscription(request):
    try:
        userID = request.data['user_id']
        subID = request.data['sub_id']
        planID = request.data['plan_id']
    except KeyError:
        return Response({"Error": "Invalid Request Keys"}, status=406)

    queryset = Subscription.objects.filter(id=subID, user=userID)

    if not queryset.exists():
        return Response({"Error": "Invalid subscription details"}, status=404)

    else:
        checkPlan = Plan.objects.filter(id=planID).exists()
        if checkPlan:
            queryset.update(plan_id=planID)
            return Response("Success")
        else:
            return Response({"Error": "Invalid plan details"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancelSubscription(request):
    try:
        userID = request.data['user_id']
        subID = request.data['sub_id']
    except KeyError:
        return Response({"Error": "Invalid Request Keys"}, status=406)

    queryset = Subscription.objects.filter(id=subID, user=userID)

    if not queryset.exists():
        return Response({"Error": "Invalid subscription details"}, status=404)

    else:
        queryset.update(active=False)
        return Response("Success")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def listSubscription(request):
    try:
        userID = request.data['user_id']
    except KeyError:
        return Response({"Error": "Invalid Request Keys"}, status=406)

    queryset = Subscription.objects.filter(user=userID, active=True)

    if queryset.exists():
        queryset = queryset.values()
        return queryset
    else:
        return Response({"Error": "User not found with active apps"}, status=404)

