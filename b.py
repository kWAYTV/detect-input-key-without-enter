import keyboard, os

try:
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            print(f"Pressed {key}")
            if key == "1":
                print(f"Triggered defined key: {key}")
except KeyboardInterrupt():
    print("Program interrupted")
    exit()
except Exception as e:
    print(f"Error: {e}")