import cv2
import mediapipe as mp
import pyautogui
import speech_recognition as sr
import pyttsx3

# Initialize webcam and face mesh
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Initialize speech recognition and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Variables for click and drag
click_drag_active = False


def recognize_voice_command():
    with sr.Microphone() as source:
        print("Listening for voice commands...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            return None


def execute_voice_command(command):
    if "open browser" in command:
        pyautogui.hotkey('ctrl', 't')
        engine.say("Opening browser")
        engine.runAndWait()
    elif "close window" in command:
        pyautogui.hotkey('alt', 'f4')
        engine.say("Closing window")
        engine.runAndWait()
    elif "type text" in command:
        pyautogui.typewrite("Hello, this is an automated message!")
        engine.say("Typing text")
        engine.runAndWait()
    else:
        engine.say("Command not recognized")
        engine.runAndWait()


while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Control mouse pointer with eye landmarks
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Blink detection for click and double-click
        left_eye_top = landmarks[159]
        left_eye_bottom = landmarks[145]
        if (left_eye_bottom.y - left_eye_top.y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(0.5)
        if (left_eye_bottom.y - left_eye_top.y) < 0.002:
            pyautogui.doubleClick()
            pyautogui.sleep(0.5)

        # Click and drag functionality
        if not click_drag_active and (landmarks[145].y - landmarks[159].y) > 0.01:
            click_drag_active = True
            pyautogui.mouseDown()
        elif click_drag_active and (landmarks[145].y - landmarks[159].y) < 0.01:
            click_drag_active = False
            pyautogui.mouseUp()

        # Scrolling with eye movements
        if landmarks[159].y < 0.4:
            pyautogui.scroll(10)
        elif landmarks[159].y > 0.6:
            pyautogui.scroll(-10)

    # Voice command processing
    if cv2.waitKey(1) & 0xFF == ord('v'):
        command = recognize_voice_command()
        if command:
            execute_voice_command(command)

    cv2.imshow('Advanced Eye-Controlled Mouse with Voice Commands', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
