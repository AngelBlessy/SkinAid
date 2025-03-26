from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout

from django.contrib.auth.models import User

import json
from datetime import datetime

from .forms import UploadFileForm

from .models import Appointment, Doctor

from .scripts.OTP_sender import send_otp
from .scripts.detectionbackend import predict


user = None


# Create your views here.
# def home(request):
#   return HttpResponse("Hello World!")
# render=show
# a view is a function or class that takes a web request and returns a web response
def index(request):
    return render(request, "landing_page.html")  # return/shows  the webpage


def login(request):
    return render(request, "login.html")


def Signin(request):
    return render(request, "Signin.html")


def Detectionscreen(request):
    return render(request, "Detectionscreen.html")


def api2(request):
    return render(request, "api2.html")


def contact(request):
    return render(request, "contact.html")


def forgotpassword(request):
    return render(request, "forgotpassword.html")


def idk(request):
    return render(request, "idk.html")


def info2(request):
    return render(request, "info2.html")


def myappointment(request):
    context = {
        "name": "",
        "age": "",
        "gender": "",
        "date": "",
        "time": "",
        "doctorname": "",
        "appointments": [],
    }

    # Check if user is authenticated
    if request.user.is_authenticated:
        # Get appointments for this user using the ForeignKey
        user_appointments = Appointment.objects.filter(user=request.user)
        context["appointments"] = user_appointments

    # Process appointment form submission
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        date = request.POST.get("date")
        time = request.POST.get("time")
        doctorname = request.POST.get("doctorname")

        context.update(
            {
                "name": name,
                "age": age,
                "gender": gender,
                "date": date,
                "time": time,
                "doctorname": doctorname,
            }
        )

        if time and request.user.is_authenticated:
            try:
                time_obj = datetime.strptime(time, "%I:%M %p")
                time_24hr = time_obj.strftime("%H:%M")

                # Create appointment and link to the current user
                appointment_obj = Appointment(
                    patientname=name,
                    patientage=age,
                    patientgender=gender,
                    date=date,
                    time=time_24hr,
                    doctorname=doctorname,
                    user=request.user,  # Link to the current user
                )
                appointment_obj.save()

                # Refresh appointments
                context["appointments"] = Appointment.objects.filter(user=request.user)
            except Exception as e:
                print(f"Error saving appointment: {e}")
                context["error"] = (
                    "There was an error saving your appointment. Please try again."
                )

    return render(request, "myappointment.html", context)


def newappointment(request):
    return render(request, "newappointment.html")


def newprofile(request):
    return render(request, "newprofile.html")


def sup(request):
    return render(request, "sup.html")


def drdeepak(request):
    return render(request, "drdeepak.html")


def drdinesh(request):
    return render(request, "drdinesh.html")


def dreswari(request):
    return render(request, "dreswari.html")


def drharish(request):
    return render(request, "drharish.html")


def drneha(request):
    return render(request, "drneha.html")


def drparthasarathi(request):
    return render(request, "drparthasarathi.html")


def drsavitha(request):
    return render(request, "drsavitha.html")


def drshashidar(request):
    return render(request, "drshashidar.html")


def drsheelavathi(request):
    return render(request, "drsheelavathi.html")


def drshishira(request):
    return render(request, "drshishira.html")


def login_api(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            # Use Django's authenticate function to verify credentials
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # This is crucial - it establishes the session
                auth_login(request, user)
                return redirect("/Detectionscreen/")
            else:
                # Authentication failed
                return redirect("/login/?error=invalid_credentials")

    return redirect("/login/")


def signin_api(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            # Return to signup page with error parameter
            return redirect("/Signin/?error=username_exists")

        if User.objects.filter(email=email).exists():
            # Return to signup page with error parameter
            return redirect("/Signin/?error=email_exists")

        if username and password:
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            return redirect("/login/")

    return redirect("/login/")


def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect to the login page
    return redirect("/login/")


@csrf_exempt
# This decorator is used to exempt the view from CSRF verification
def send_otp_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        otp = data.get("otp")

        try:
            if User.objects.get(email=email):

                print(email, otp)

                if email and otp:
                    send_otp(email, otp)

                return JsonResponse({"status": "success"})

        except User.DoesNotExist:
            return JsonResponse({"status": "User does not exist"})

    return JsonResponse({"status": "failed"})


@csrf_exempt
def reset_password_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()

            return JsonResponse({"status": "success"})

        except User.DoesNotExist:
            return JsonResponse({"status": "User does not exist"})

    return JsonResponse({"status": "failed"})


@csrf_exempt
def predict_result_api(request):
    """
    API endpoint to handle image uploads and return prediction results.
    Enhanced with better error handling for mobile devices.
    """
    if request.method == "POST":
        response_data = {"status": "failed", "message": "Unknown error occurred"}

        try:
            # Check if we received any files
            if "file" not in request.FILES:
                response_data["message"] = "No file uploaded"
                return JsonResponse(response_data)

            # Get the uploaded file
            uploaded_file = request.FILES["file"]

            # Log file information
            print(
                f"Received file: {uploaded_file.name}, Size: {uploaded_file.size} bytes, Content-Type: {uploaded_file.content_type}"
            )

            # Verify the file has content
            if uploaded_file.size == 0:
                response_data["message"] = "Uploaded file is empty"
                return JsonResponse(response_data)

            # Check file type
            if not uploaded_file.content_type.startswith("image/"):
                response_data["message"] = (
                    f"Invalid file type: {uploaded_file.content_type}"
                )
                return JsonResponse(response_data)

            # Check file size (5MB limit)
            if uploaded_file.size > 5 * 1024 * 1024:  # 5MB
                response_data["message"] = "File too large (max 5MB)"
                return JsonResponse(response_data)

            # Save temp file
            temp_path = "temp.jpg"
            with open(temp_path, "wb") as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            print(f"Temporary file saved to {temp_path}")

            # Process the image and get prediction
            try:
                model_path = "app/scripts/skin_lesion_model.pth"
                print(
                    f"Calling predict function with model: {model_path}, image: {temp_path}"
                )
                result = predict(model_path, temp_path)

                print(f"Prediction result: {result}")
                return JsonResponse({"status": "success", "result": result})

            except Exception as e:
                import traceback

                traceback_str = traceback.format_exc()
                error_message = str(e)
                print(f"Error during prediction: {error_message}")
                print(f"Traceback: {traceback_str}")
                response_data["message"] = f"Prediction error: {error_message}"
                return JsonResponse(response_data)

        except Exception as e:
            import traceback

            traceback_str = traceback.format_exc()
            error_message = str(e)
            print(f"General error: {error_message}")
            print(f"Traceback: {traceback_str}")
            response_data["message"] = f"Server error: {error_message}"
            return JsonResponse(response_data)

    return JsonResponse({"status": "failed", "message": "Invalid request method"})


def add_doctor_dict(request):
    sampleDoctors = [
        {
            id: 1,
            "name": "Dr. Deepak Devakar",
            "location": "Jayanagar, Bangalore",
            "picture": "dr-deepak-devakar.jpg",
            "detailsLink": "drdeepak",
        },
        {
            id: 2,
            "name": "Dr. Dinesh Gowda",
            "location": "Sahakaranagar, Bangalore",
            "picture": "dr-dinesh-gowda.jpg",
            "detailsLink": "drdinesh",
        },
        {
            id: 3,
            "name": "Dr. Eswari",
            "location": "Jayanagar 4 Block, Bangalore",
            "picture": "dr-eswari.jpg",
            "detailsLink": "dreswari",
        },
        {
            id: 4,
            "name": "Dr. Harish Prasad",
            "location": "BTM Layout, Bangalore",
            "picture": "dr-harish-prasad.jpg",
            "detailsLink": "drharish",
        },
        {
            id: 5,
            "name": "Dr. Neha Gupta",
            "location": "HSR Layout, Bangalore",
            "picture": "dr-neha-gupta.jpg",
            "detailsLink": "drneha",
        },
        {
            id: 6,
            "name": "Dr. Parthasarathi Dutta Roy",
            "location": "Magrath Road, Bangalore",
            "picture": "dr-parthasarathi-dutta-roy.jpg",
            "detailsLink": "drparthasarathi",
        },
        {
            id: 7,
            "name": "Dr. Savitha A S",
            "location": "Indiranagar, Bangalore",
            "picture": "dr-savitha-a-s.jpg",
            "detailsLink": "drsavitha",
        },
        {
            id: 8,
            "name": "Dr. Shashidhar T",
            "location": "Jayanagar 4 Block, Bangalore",
            "picture": "dr-shashidhar-t.jpg",
            "detailsLink": "drshashidar",
        },
        {
            id: 9,
            "name": "Dr. Sheelavathi Natraj",
            "location": "Koramangala 6 Block, Bangalore",
            "picture": "dr-sheelavathi-natraj.jpg",
            "detailsLink": "drsheelavathi",
        },
        {
            id: 10,
            "name": "Dr. Shishira R J",
            "location": "HSR Layout, Bangalore",
            "picture": "dr-shishira-r-j.jpg",
            "detailsLink": "drshishira",
        },
    ]
    print(sampleDoctors)
    for doctor in sampleDoctors:
        doctor_obj = Doctor(
            doctorname=doctor["name"],
            location=doctor["location"],
            picture=doctor["picture"],
            detailshtml=doctor["detailsLink"],
        )
        doctor_obj.save()

    return JsonResponse({"status": "success"})
